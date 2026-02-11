#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import numpy as np
import open3d as o3d
import sensor_msgs_py.point_cloud2 as pc2
from numpy.lib import recfunctions as rfn
from collections import defaultdict

from sensor_msgs.msg import PointCloud2
from robot_interfaces.msg import Stair


class LidarStepDetector(Node):
    """
    Detect the top surface (horizontal plane) of a pallet using RANSAC + DBSCAN.

    Key assumptions:
    - LiDAR is mounted UPSIDE DOWN at 30-degree angle on the robot
    - Incoming PointCloud2 is in raw LiDAR sensor frame (NOT gravity-aligned)
    - Target pallet height is ~0.14 m above ground (post-transformation)
    
    Core logic:
    1) Transform points from sensor frame to gravity-aligned frame (180° X-flip + 30° Y-pitch)
    2) Crop ROI directly in front
    3) Fit ground plane using RANSAC
    4) Fit horizontal plane (step) using RANSAC
    5) Apply DBSCAN clustering to nearby inlier points
    6) Validate using planarity check and depth consistency
    7) Publish detection + debug clouds
    """

    def __init__(self):
        super().__init__("lidar_step_detector")

        # ---- ROS I/O ----
        self.sub = self.create_subscription(PointCloud2, "/go2/Lidar", self.lidar_callback, 1)

        self.det_pub = self.create_publisher(Stair, "stair_detection", 1)
        self.ground_pub = self.create_publisher(PointCloud2, "/ground_cloud", 10)
        self.obstacle_pub = self.create_publisher(PointCloud2, "/obstacle_cloud", 10)
        self.step_pub = self.create_publisher(PointCloud2, "/step_cloud", 10)

        # ---- ROI in front (tuned for pallet detection) ----
        # Now in gravity-aligned frame after transformation
        self.x_min, self.x_max = 0.45, 1.50     # meters in front
        self.y_min, self.y_max = -0.60, 0.60    # meters left/right
        self.z_min, self.z_max = 0.00, 0.80     # positive Z = up (gravity aligned)

        # ---- Ground plane segmentation (RANSAC) ----
        self.ground_dist_thresh = 0.05
        self.ground_ransac_n = 3
        self.ground_iters = 1000

        # ---- Step detection (horizontal plane) ----
        # Pallet at ~0.14m height above ground (post-transformation)
        self.min_step_height = 0.10    # minimum Z for step detection
        self.max_step_height = 0.20    # maximum Z for step detection (pallet height)
        
        self.step_dist_thresh = 0.02
        self.step_ransac_n = 3
        self.step_iters = 1000
        
        # ---- Horizontal plane criteria ----
        # Normal vector should point mostly in Z direction (horizontal plane)
        self.horizontal_min_nz = 0.90

        # ---- DBSCAN clustering params ----
        self.dbscan_eps = 0.05
        self.dbscan_min_points = 5

        # ---- Validation thresholds ----
        self.min_inliers = 50
        self.min_cluster_points = 30
        self.max_z_variance = 0.01      # planarity check
        self.depth_tolerance = 0.09     # depth consistency check

    def lidar_callback(self, msg: PointCloud2):
        pts = self.pointcloud2_to_xyz(msg)
        if pts.size == 0:
            self.publish_detection(False, 0.0, False)
            return

        # Transform from sensor frame to gravity-aligned frame
        pts = self.align_to_base_frame(pts)

        roi = self.crop_roi(pts)
        if roi.shape[0] < 200:
            self.publish_detection(False, 0.0, False)
            return

        # Convert to Open3D point cloud
        cloud = o3d.geometry.PointCloud()
        cloud.points = o3d.utility.Vector3dVector(roi)

        # Segment ground plane from the entire ROI
        ground_cloud, ground_model, obstacle_cloud = self.segment_ground_and_obstacles(cloud)

        # Publish debug clouds
        if np.asarray(ground_cloud.points).shape[0] > 0:
            self.ground_pub.publish(self.xyz_to_pointcloud2(
                np.asarray(ground_cloud.points), msg.header))
        if np.asarray(obstacle_cloud.points).shape[0] > 0:
            self.obstacle_pub.publish(self.xyz_to_pointcloud2(
                np.asarray(obstacle_cloud.points), msg.header))

        # Detect step (horizontal plane) in the obstacle cloud
        detected, distance, step_cloud = self.detect_step(obstacle_cloud)

        if detected and step_cloud is not None:
            step_pts = np.asarray(step_cloud.points)
            if step_pts.shape[0] > 0:
                self.step_pub.publish(self.xyz_to_pointcloud2(step_pts, msg.header))

        self.publish_detection(detected, distance, detected)  # upstairs=detected

    def crop_roi(self, pts: np.ndarray) -> np.ndarray:
        m = (
            (pts[:, 0] >= self.x_min) & (pts[:, 0] <= self.x_max) &
            (pts[:, 1] >= self.y_min) & (pts[:, 1] <= self.y_max) &
            (pts[:, 2] >= self.z_min) & (pts[:, 2] <= self.z_max)
        )
        return pts[m]

    def align_to_base_frame(self, points: np.ndarray) -> np.ndarray:
        """
        Transform point cloud from LiDAR sensor frame to gravity-aligned base frame.
        
        LiDAR mounting configuration:
        - 180° rotation about X-axis (upside down)
        - 30° downward pitch about Y-axis
        
        Final rotation: R = R_pitch_y @ R_flip_x
        
        Parameters:
        - points: Nx3 array of points in sensor frame (float32)
        
        Returns:
        - Nx3 array of points in gravity-aligned frame (float32)
        """
        # Convert rotation angles to radians
        angle_flip_x = np.pi  # 180 degrees
        angle_pitch_y = np.radians(30)  # 30 degrees
        
        # Rotation matrix for 180° about X-axis (flip upside down)
        cos_fx = np.cos(angle_flip_x)
        sin_fx = np.sin(angle_flip_x)
        R_flip_x = np.array([
            [1.0,    0.0,    0.0],
            [0.0,  cos_fx, -sin_fx],
            [0.0,  sin_fx,  cos_fx]
        ], dtype=np.float32)
        
        # Rotation matrix for 30° about Y-axis (downward pitch)
        cos_py = np.cos(angle_pitch_y)
        sin_py = np.sin(angle_pitch_y)
        R_pitch_y = np.array([
            [cos_py,  0.0, sin_py],
            [0.0,     1.0,   0.0],
            [-sin_py, 0.0, cos_py]
        ], dtype=np.float32)
        
        # Combined rotation: apply flip first, then pitch
        R_combined = R_pitch_y @ R_flip_x
        
        # Apply rotation to all points
        rotated_points = points @ R_combined.T
        
        return rotated_points

    def segment_ground_and_obstacles(self, point_cloud):
        """
        Segment ground plane and potential obstacles using RANSAC.
        
        Parameters:
        - point_cloud: Open3D point cloud object
        
        Returns:
        - ground_cloud: Ground plane points
        - plane_model: Ground plane model coefficients
        - obstacle_cloud: Non-ground points
        """
        plane_model, inliers = point_cloud.segment_plane(
            distance_threshold=self.ground_dist_thresh,
            ransac_n=self.ground_ransac_n,
            num_iterations=self.ground_iters
        )

        ground_cloud = point_cloud.select_by_index(inliers)
        obstacle_cloud = point_cloud.select_by_index(inliers, invert=True)

        return ground_cloud, plane_model, obstacle_cloud

    def detect_step(self, point_cloud):
        """
        Detect horizontal step (pallet top surface) using RANSAC + DBSCAN + validation.
        
        Parameters:
        - point_cloud: Open3D point cloud of obstacles
        
        Returns:
        - (detected: bool, distance_m: float, step_cloud: PointCloud or None)
        """
        points = np.asarray(point_cloud.points)

        # Need minimum points to detect
        if len(points) < 10:
            return False, 0.0, None

        # Fit horizontal plane using RANSAC
        plane_model, inliers = point_cloud.segment_plane(
            distance_threshold=self.step_dist_thresh,
            ransac_n=self.step_ransac_n,
            num_iterations=self.step_iters
        )

        # Check if plane is horizontal (normal mostly in Z direction)
        normal_vector = plane_model[:3]
        if np.abs(normal_vector[2]) <= self.horizontal_min_nz:
            return False, 0.0, None

        if len(inliers) < self.min_inliers:
            return False, 0.0, None

        # Extract inlier cloud
        inlier_cloud = point_cloud.select_by_index(inliers)
        inlier_points = np.asarray(inlier_cloud.points)

        # Check if plane height is in expected range for pallet
        z_coords = inlier_points[:, 2]
        sorted_indices = np.argsort(z_coords)
        top_indices = sorted_indices[-max(1, int(len(z_coords) * 0.15)):]
        top_heights = z_coords[top_indices]
        step_height = np.mean(top_heights)

        if not (self.min_step_height < step_height < self.max_step_height):
            return False, 0.0, None

        # Apply DBSCAN clustering to group nearby inlier points
        labels = np.array(inlier_cloud.cluster_dbscan(
            eps=self.dbscan_eps,
            min_points=self.dbscan_min_points,
            print_progress=False
        ))

        valid_labels = labels[labels != -1]
        if valid_labels.size == 0:
            return False, 0.0, None

        # Find largest cluster
        unique_labels, counts = np.unique(labels, return_counts=True)
        largest_cluster_label = unique_labels[np.argmax(counts)]
        largest_cluster_indices = np.where(labels == largest_cluster_label)[0]

        if len(largest_cluster_indices) < self.min_cluster_points:
            return False, 0.0, None

        # Planarity check
        cluster_points = np.asarray(inlier_cloud.select_by_index(largest_cluster_indices).points)
        z_variance = np.var(cluster_points[:, 2])

        if z_variance > self.max_z_variance:
            return False, 0.0, None

        # Depth consistency check
        x_to_z_values = defaultdict(list)
        for x, _, z in cluster_points:
            x_to_z_values[round(x, 2)].append(z)

        is_consistent_depth = True
        for z_values in x_to_z_values.values():
            unique_heights = np.unique(z_values)
            if len(unique_heights) > 5 and np.ptp(unique_heights) > self.depth_tolerance:
                is_consistent_depth = False
                break

        if not is_consistent_depth:
            return False, 0.0, None

        # Successfully detected step
        step_cloud = inlier_cloud.select_by_index(largest_cluster_indices)
        distance = float(np.median(cluster_points[:, 0]))

        self.get_logger().info(f"Step detected! Height: {step_height:.3f} m, Distance: {distance:.2f} m")
        return True, distance, step_cloud

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
    node = LidarStepDetector()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
