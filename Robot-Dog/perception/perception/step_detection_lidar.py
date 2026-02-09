#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import numpy as np
import open3d as o3d

from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Float32MultiArray
import sensor_msgs_py.point_cloud2 as pc2
from numpy.lib import recfunctions as rfn


class PalletDetector(Node):
    """
    Goal: detect a pallet directly in front of the robot.

    Pipeline (simple + robust):
      1) Crop ROI in front of robot
      2) Fit ground plane once via RANSAC
      3) Compute height-above-ground for ROI points
      4) Pallet = enough points in a height band (e.g. 10–25 cm) with enough span
      5) Distance = closest x among pallet-band points

    Publishes:
      - /pallet_detection (Float32MultiArray): [detected(0/1), distance_m, height_m]
      - /ground_cloud (PointCloud2): ground inliers (for RViz)
      - /obstacle_cloud (PointCloud2): non-ground points (for RViz)
      - /pallet_cloud (PointCloud2): pallet-band points (for RViz)
    """

    def __init__(self):
        super().__init__("pallet_detector")

        # --- Sub ---
        self.sub = self.create_subscription(
            PointCloud2,
            "/utlidar/cloud",
            self.lidar_callback,
            1
        )

        # --- Pubs ---
        self.det_pub = self.create_publisher(Float32MultiArray, "/pallet_detection", 10)
        self.ground_pub = self.create_publisher(PointCloud2, "/ground_cloud", 10)
        self.obstacle_pub = self.create_publisher(PointCloud2, "/obstacle_cloud", 10)
        self.pallet_pub = self.create_publisher(PointCloud2, "/pallet_cloud", 10)

        # --- Accumulation (optional smoothing) ---
        self.cloud_accumulation = []
        self.accumulation_limit = 3  # lower latency than 5; tune to taste

        # --- Tunables: ROI in lidar frame ---
        self.x_min, self.x_max = 0.30, 1.50
        self.y_min, self.y_max = -0.45, 0.45
        self.z_min, self.z_max = -1.50, 1.00

        # --- Ground plane RANSAC ---
        self.ground_dist_thresh = 0.02
        self.ground_ransac_n = 3
        self.ground_iters = 500
        self.min_roi_points = 200

        # --- Pallet band height above ground (meters) ---
        self.pallet_h_min = 0.10
        self.pallet_h_max = 0.25

        # --- Pallet validation thresholds ---
        self.min_band_points = 150       # must have enough points in the band
        self.min_y_span = 0.25           # pallet should span some width
        self.min_x_span = 0.15           # and some depth (avoid tiny false positives)

    # ---------------- ROS callbacks ----------------

    def lidar_callback(self, msg: PointCloud2):
        pts = self.pointcloud2_to_xyz(msg)
        if pts.size == 0:
            self.publish_detection(False, 0.0, 0.0)
            return

        self.cloud_accumulation.append(pts)

        if len(self.cloud_accumulation) < self.accumulation_limit:
            return

        combined = np.concatenate(self.cloud_accumulation, axis=0)
        self.cloud_accumulation = []

        detected, dist, height, ground_pts, obstacle_pts, pallet_pts = self.detect_pallet(combined)

        # Publish debug clouds
        if ground_pts is not None and ground_pts.shape[0] > 0:
            self.ground_pub.publish(self.xyz_to_pointcloud2(ground_pts, msg.header))
        if obstacle_pts is not None and obstacle_pts.shape[0] > 0:
            self.obstacle_pub.publish(self.xyz_to_pointcloud2(obstacle_pts, msg.header))
        if pallet_pts is not None and pallet_pts.shape[0] > 0:
            self.pallet_pub.publish(self.xyz_to_pointcloud2(pallet_pts, msg.header))

        # Publish compact detection
        self.publish_detection(detected, dist, height)

    # ---------------- Core logic ----------------

    def detect_pallet(self, point_cloud_np: np.ndarray):
        """
        Returns:
          detected(bool), distance(float), height(float),
          ground_pts(Nx3), obstacle_pts(Nx3), pallet_pts(Nx3)
        """
        # 1) ROI crop
        roi = self.crop_roi(point_cloud_np)
        if roi.shape[0] < self.min_roi_points:
            return False, 0.0, 0.0, None, None, None

        # 2) Fit ground plane with RANSAC
        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(roi)

        plane_model, inliers = cloud.segment_plane(
            distance_threshold=self.ground_dist_thresh,
            ransac_n=self.ground_ransac_n,
            num_iterations=self.ground_iters
        )

        a, b, c, d = plane_model
        n = np.array([a, b, c], dtype=np.float32)
        n_norm = float(np.linalg.norm(n))
        if n_norm < 1e-6:
            return False, 0.0, 0.0, None, None, None

        # Ground should be roughly horizontal: normal close to Z axis.
        # If this fails often, your lidar frame axis convention might differ.
        if abs(c) < 0.90:
            return False, 0.0, 0.0, None, None, None

        ground_cloud = cloud.select_by_index(inliers)
        obstacle_cloud = cloud.select_by_index(inliers, invert=True)
        ground_pts = np.asarray(ground_cloud.points) if len(ground_cloud.points) else None
        obstacle_pts = np.asarray(obstacle_cloud.points) if len(obstacle_cloud.points) else None

        # 3) Height above plane for ALL ROI points (signed distance)
        # h = (a x + b y + c z + d) / ||n||
        h = (roi @ n + d) / n_norm

        # Make "above ground" positive consistently:
        # if most ROI points end up negative, flip sign.
        if np.median(h) < 0:
            h = -h

        # 4) Pallet band filter
        band_mask = (h > self.pallet_h_min) & (h < self.pallet_h_max)
        pallet_pts = roi[band_mask]

        if pallet_pts.shape[0] < self.min_band_points:
            return False, 0.0, 0.0, ground_pts, obstacle_pts, None

        # 5) Simple geometric sanity checks to kill false positives
        y_span = float(pallet_pts[:, 1].max() - pallet_pts[:, 1].min())
        x_span = float(pallet_pts[:, 0].max() - pallet_pts[:, 0].min())

        if y_span < self.min_y_span or x_span < self.min_x_span:
            return False, 0.0, 0.0, ground_pts, obstacle_pts, None

        # 6) Distance = closest x in the band (since ROI x is "in front")
        distance = float(np.min(pallet_pts[:, 0]))
        height_est = float(np.median(h[band_mask]))

        return True, distance, height_est, ground_pts, obstacle_pts, pallet_pts

    # ---------------- Helpers ----------------

    def crop_roi(self, pts: np.ndarray) -> np.ndarray:
        m = (
            (pts[:, 0] > self.x_min) & (pts[:, 0] < self.x_max) &
            (pts[:, 1] > self.y_min) & (pts[:, 1] < self.y_max) &
            (pts[:, 2] > self.z_min) & (pts[:, 2] < self.z_max)
        )
        return pts[m]

    def publish_detection(self, detected: bool, distance: float, height: float):
        msg = Float32MultiArray()
        msg.data = [1.0 if detected else 0.0, float(distance), float(height)]
        self.det_pub.publish(msg)

        # Keep logs lightweight (spam can be brutal at lidar rates)
        if detected:
            self.get_logger().info(f"Pallet: YES | dist={distance:.2f} m | h={height:.2f} m")
        # else:
        #     self.get_logger().debug("Pallet: no")

    def pointcloud2_to_xyz(self, cloud_msg: PointCloud2) -> np.ndarray:
        pts = np.array(list(pc2.read_points(
            cloud_msg,
            field_names=("x", "y", "z"),
            skip_nans=True
        )))
        if pts.size == 0:
            return np.empty((0, 3), dtype=np.float32)

        xyz = rfn.structured_to_unstructured(pts).astype(np.float32)
        return xyz

    def xyz_to_pointcloud2(self, points_xyz: np.ndarray, header) -> PointCloud2:
        # points_xyz: Nx3 float array
        return pc2.create_cloud_xyz32(header, points_xyz.tolist())


def main(args=None):
    rclpy.init(args=args)
    node = PalletDetector()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
