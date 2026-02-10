#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import numpy as np
import open3d as o3d
import sensor_msgs_py.point_cloud2 as pc2
from numpy.lib import recfunctions as rfn

from sensor_msgs.msg import PointCloud2
from robot_interfaces.msg import Stair


class LidarPalletFaceDetector(Node):
    """
    Simple pallet FACE (vertical plane) detector.

    Assumptions you gave:
    - Forward direction is +X
    - Z is non-negative (z >= 0). So z=0 is the floor (or near it).
    - LiDAR is ~0.20 m above ground (not directly used here since z is ground-referenced)
    - Pallet height ~0.14 m (used as a sanity check for z span)

    Core logic:
    1) Crop ROI directly in front
    2) Remove ground points by a simple z threshold
    3) Fit ONE plane (RANSAC) to what's left
    4) Keep it only if the plane is vertical-ish (normal not pointing up)
    5) Validate by size (width in y, height in z) and distance in x
    6) Publish detection + debug clouds
    """

    def __init__(self):
        super().__init__("lidar_pallet_face_detector")

        # ---- ROS I/O ----
        self.sub = self.create_subscription(PointCloud2, "/go2/Lidar", self.lidar_callback, 1)

        self.det_pub = self.create_publisher(Stair, "stair_detection", 1)  # reused msg type
        self.ground_pub = self.create_publisher(PointCloud2, "/ground_cloud", 10)
        self.obstacle_pub = self.create_publisher(PointCloud2, "/obstacle_cloud", 10)
        self.face_pub = self.create_publisher(PointCloud2, "/pallet_face_cloud", 10)

        # ---- ROI in front (tune as needed) ----
        self.x_min, self.x_max = 0.25, 1.50     # meters in front
        self.y_min, self.y_max = -0.50, 0.50    # meters left/right
        self.z_min, self.z_max = 0.00, 0.80     # z is non-negative per your note

        # ---- Ground removal (simple) ----
        self.ground_z_thresh = 0.03  # points with z <= this treated as ground

        # ---- Plane fit params ----
        self.plane_dist_thresh = 0.02
        self.plane_ransac_n = 3
        self.plane_iters = 600

        # ---- Vertical plane criteria ----
        # For a vertical face, plane normal should have small Z component (nz ~ 0)
        self.vertical_max_abs_nz = 0.25

        # ---- Validation thresholds ----
        self.min_inliers = 120
        self.min_y_span = 0.30          # pallet face should be wide-ish
        self.min_z_span = 0.08          # pallet is ~0.14 m tall; allow partial view
        self.max_z_span = 0.40          # reject big walls if you want (still generous)

    def lidar_callback(self, msg: PointCloud2):
        pts = self.pointcloud2_to_xyz(msg)
        if pts.size == 0:
            self.publish_detection(False, 0.0, False)
            return

        roi = self.crop_roi(pts)
        if roi.shape[0] < 200:
            self.publish_detection(False, 0.0, False)
            return

        # Split ground vs non-ground with a simple z threshold
        ground_mask = roi[:, 2] <= self.ground_z_thresh
        ground_pts = roi[ground_mask]
        nonground_pts = roi[~ground_mask]

        # Publish debug clouds
        if ground_pts.shape[0] > 0:
            self.ground_pub.publish(self.xyz_to_pointcloud2(ground_pts, msg.header))
        if nonground_pts.shape[0] > 0:
            self.obstacle_pub.publish(self.xyz_to_pointcloud2(nonground_pts, msg.header))

        detected, distance, face_pts = self.detect_vertical_face(nonground_pts)

        if detected and face_pts is not None and face_pts.shape[0] > 0:
            self.face_pub.publish(self.xyz_to_pointcloud2(face_pts, msg.header))

        # Reuse Stair msg:
        # - detected: pallet face detected
        # - upstairs: not meaningful for pallet; set False
        # - distance: distance to face (median x)
        self.publish_detection(detected, distance, False)

    def crop_roi(self, pts: np.ndarray) -> np.ndarray:
        m = (
            (pts[:, 0] >= self.x_min) & (pts[:, 0] <= self.x_max) &
            (pts[:, 1] >= self.y_min) & (pts[:, 1] <= self.y_max) &
            (pts[:, 2] >= self.z_min) & (pts[:, 2] <= self.z_max)
        )
        return pts[m]

    def detect_vertical_face(self, pts: np.ndarray):
        """
        Fit a single plane and check if it looks like a vertical pallet face.

        Returns:
          (detected: bool, distance_m: float, face_pts: Nx3 or None)
        """
        if pts.shape[0] < 80:
            return False, 0.0, None

        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(pts)

        plane_model, inliers = cloud.segment_plane(
            distance_threshold=self.plane_dist_thresh,
            ransac_n=self.plane_ransac_n,
            num_iterations=self.plane_iters
        )

        if len(inliers) < self.min_inliers:
            return False, 0.0, None

        a, b, c, d = plane_model
        normal = np.array([a, b, c], dtype=np.float32)
        n_norm = float(np.linalg.norm(normal))
        if n_norm < 1e-6:
            return False, 0.0, None
        normal /= n_norm

        # Vertical plane => normal Z component near 0
        if abs(normal[2]) > self.vertical_max_abs_nz:
            return False, 0.0, None

        inlier_cloud = cloud.select_by_index(inliers)
        face_pts = np.asarray(inlier_cloud.points)
        if face_pts.shape[0] < self.min_inliers:
            return False, 0.0, None

        # Basic size checks to avoid tiny clutter
        y_span = float(face_pts[:, 1].max() - face_pts[:, 1].min())
        z_span = float(face_pts[:, 2].max() - face_pts[:, 2].min())

        if y_span < self.min_y_span:
            return False, 0.0, None
        if z_span < self.min_z_span or z_span > self.max_z_span:
            return False, 0.0, None

        # Distance: median X of the face points (stable)
        distance = float(np.median(face_pts[:, 0]))

        return True, distance, face_pts

    def publish_detection(self, detected: bool, distance: float, upstairs: bool):
        msg = Stair()
        msg.detected = bool(detected)
        msg.upstairs = bool(upstairs)  # not used here, kept for compatibility
        msg.distance = float(distance) if detected else 0.0
        self.det_pub.publish(msg)

        if detected:
            self.get_logger().info(f"Pallet face detected | distance={distance:.2f} m")

    def pointcloud2_to_xyz(self, cloud_msg: PointCloud2) -> np.ndarray:
        points = np.array(list(pc2.read_points(cloud_msg, field_names=("x", "y", "z"), skip_nans=True)))
        if points.size == 0:
            return np.empty((0, 3), dtype=np.float32)
        xyz = rfn.structured_to_unstructured(points).astype(np.float32)
        return xyz

    def xyz_to_pointcloud2(self, points_xyz: np.ndarray, header) -> PointCloud2:
        return pc2.create_cloud_xyz32(header, points_xyz.tolist())


def main(args=None):
    rclpy.init(args=args)
    node = LidarPalletFaceDetector()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
