#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
import numpy as np
import open3d as o3d
import sensor_msgs_py.point_cloud2 as pc2
from scipy.spatial.transform import Rotation as R
from robot_interfaces.msg import Stair
from numpy.lib import recfunctions as rfn
from collections import defaultdict

class LidarStepDetector(Node):
    def __init__(self):
        super().__init__('lidar_step_detector')

        # Publisher for step detection
        self.step_detection_publisher = self.create_publisher(Stair, 'stair_detection', 1)
        
        # Subscribe to the LIDAR point cloud topic
        self.subscription = self.create_subscription(
            PointCloud2,
            '/go2/Lidar',
            self.lidar_callback,
            1
        )

        # Publishers for ground and obstacle point clouds
        self.ground_pub = self.create_publisher(PointCloud2, '/ground_cloud', 10)  # Ground points
        self.obstacle_pub = self.create_publisher(PointCloud2, '/obstacle_cloud', 10)  # Obstacle points
        self.step_pub = self.create_publisher(PointCloud2, '/step_cloud', 10)  # Detected step points
        
        self.cloud_accumulation = []
        self.accumulation_limit = 5

    def lidar_callback(self, msg):
        # Convert PointCloud2 message to numpy array
        point_cloud_np = self.convert_pointcloud2_to_numpy(msg)

        if point_cloud_np.size == 0:
            self.get_logger().info("The point cloud is empty.")
            return

        self.cloud_accumulation.append(point_cloud_np)

        if len(self.cloud_accumulation) >= self.accumulation_limit:
             
             combined_point_cloud = np.concatenate(self.cloud_accumulation, axis=0)

             self.process_point_cloud(combined_point_cloud, msg.header)

             # Reset accumulation
             self.cloud_accumulation = []

    def crop_point_cloud(self, point_cloud):
        """
        Crop the point cloud to limit detection to points in front of the LIDAR and within a specified range.
        """

        # Define boundaries for STEP detection (for example, only keep points within 0.4m to 2m in front of the robot)
        x_min, x_max = 0.3, 1.5  # Distance in the X direction (in front of the LIDAR)
        y_min, y_max = -0.4, 0.4  # Limit in the Y direction (left and right of LIDAR)
        z_min, z_max = -2.0, 0.5  # Height limits (focus on step height range)
        # Apply the cropping condition
        mask = (point_cloud[:, 0] > x_min) & (point_cloud[:, 0] < x_max) & \
            (point_cloud[:, 1] > y_min) & (point_cloud[:, 1] < y_max) & \
            (point_cloud[:, 2] > z_min) & (point_cloud[:, 2] < z_max)
        
        return point_cloud[mask]
    
    def process_point_cloud(self, point_cloud, header):
         
        # Use Open3D for RANSAC-based segmentation of ground and ground obstacles
        ground_cloud, obstacle_cloud, step_cloud, upstairs = self.segment_ground_and_obstacles(point_cloud)

        # Convert Open3D clouds to ROS PointCloud2 and publish
        self.publish_clouds(ground_cloud, obstacle_cloud, step_cloud, header)
        
        stair_msg = Stair()

        if step_cloud is not None and len(step_cloud.points) > 0:
            step_points = np.asarray(step_cloud.points)
            step_distance = self.compute_distance(step_points)
            
            if step_distance is not None:
    
                stair_msg.detected = True
                if upstairs == 1:
                    stair_msg.upstairs = True
                elif upstairs == 2:
                    stair_msg.upstairs = False
                stair_msg.distance = step_distance

        # Publish custom message
        self.step_detection_publisher.publish(stair_msg)

    def convert_pointcloud2_to_numpy(self, cloud_msg):

        # Convert ROS2 PointCloud2 to a numpy array (x, y, z)
        points = np.array(list(pc2.read_points(cloud_msg, field_names=("x", "y", "z"), skip_nans=True)))
        xyz = rfn.structured_to_unstructured(points)

        return xyz
    
    def segment_ground_and_obstacles(self, point_cloud_np):
        """
        Segments the ground and obstacles using Open3D's RANSAC plane segmentation.
        """
        # Crop point cloud
        cropped_point_cloud = self.crop_point_cloud(point_cloud_np)
        
        # Convert numpy array to Open3D point cloud
        cloud_o3d = o3d.geometry.PointCloud()
        cloud_o3d.points = o3d.utility.Vector3dVector(cropped_point_cloud[:, :3])  # Use x, y, z
        
        # Apply RANSAC plane segmentation
        plane_model, inliers = cloud_o3d.segment_plane(
            distance_threshold=0.02,  # Adjust based on your sensor
            ransac_n=3,
            num_iterations=1000
        )
        
        # Extract ground points (inliers) and obstacle points (outliers)
        ground_cloud = cloud_o3d.select_by_index(inliers)  # Points considered part of the ground plane
        obstacle_cloud = cloud_o3d.select_by_index(inliers, invert=True)  # Points not part of the ground plane
        
        step_cloud = None
        upstairs = None
        
        step_inliers, _, upstairs = self.detect_steps(obstacle_cloud) # Possible step clouds
        
        if step_inliers is not None:
            step_cloud = obstacle_cloud.select_by_index(step_inliers)

        return ground_cloud, obstacle_cloud, step_cloud, upstairs
    
    def detect_steps(self, point_cloud, distance_threshold=0.05, ransac_n=10, num_iterations=1000, min_up_step_height=-0.26, max_up_step_height=-0.10, min_down_step_height=-1.0,
                     max_down_step_height=-0.4, depth_tolerance=0.09):
         """
         Detect steps in the point cloud using RANSAC to fit horizontal planes.
        
         Parameters:
         - point_cloud: Open3D point cloud object.
         - distance_threshold: Maximum distance a point can be from the plane to be considered an inlier.
         - ransac_n: Number of points to sample for RANSAC.
         - num_iterations: Number of iterations for RANSAC.
         - min_up_step_height: Minimum height difference between steps and ground or other objects. 
         - max_up_step_height: Maximum height difference (to exclude objects that are too tall to be steps). 
         - min_down_step_height: Minimum height difference between downward steps and ground or other objects. 
         - max_down_step_height: Maximum height difference (to exclude objects that are too tall to be steps).
        
         Returns:
         - up_inliers: Indices of points that belong to the detected upward step plane.
         - down_inliers: Indices of points that belong to the detected downward step plane.
         - up_plane_model: The coefficients of the plane (a, b, c, d) such that ax + by + cz + d = 0.
         - down_plane_model: The coefficients of the plane (a, b, c, d) such that ax + by + cz + d = 0.
         """
         
         points = np.asarray(point_cloud.points)

         # If not enough points, return early
         if len(points) < 10:
            #  self.get_logger().info("Not enough points in the step range. Skipping step detection.")
             return None, None, None

         # Perform RANSAC to detect planes in the point cloud
         plane_model, inliers = point_cloud.segment_plane(
             distance_threshold=distance_threshold,
             ransac_n=ransac_n,
             num_iterations=num_iterations
         )

         # Extract the normal vector of the detected plane
         normal_vector = plane_model[:3]

         # Check if the plane is horizontal (normal vector close to Z-axis)
         if np.abs(normal_vector[2]) > 0.90: 
            
             inlier_cloud = point_cloud.select_by_index(inliers)
             points = np.asarray(inlier_cloud.points)

             # Check the height of the plane (steps should not be too low or too high)
             z_coordinates = points[:, 2]
             sorted_indices = np.argsort(z_coordinates)
             top_indices = sorted_indices[-max(1, int(len(z_coordinates) * 0.15)):]    # Select top X% points
             top_heights = z_coordinates[top_indices]
             bottom_indices = sorted_indices[:max(1, int(len(z_coordinates) * 0.05))]  # Select bottom X% points
             bottom_heights = z_coordinates[bottom_indices]
             up_step_height = np.mean(top_heights)
             down_step_height = np.mean(bottom_heights)

             # Initialize inliers
             up_inliers, down_inliers = None, None
             # Flag for custom msg
             up_or_down = 0
            
             # UPSTAIRS
             if min_up_step_height < up_step_height < max_up_step_height:
                 # Apply DBSCAN clustering to group nearby points
                 labels = np.array(inlier_cloud.cluster_dbscan(eps=0.02, min_points=5, print_progress=False))
                 valid_labels = labels[labels != -1]
   
                 if valid_labels.size > 0:

                    # Find the largest clusterAfter filtering the objects which are not relevant to our function, the image will look like this.
                    unique_labels, counts = np.unique(labels, return_counts=True)
                    largest_cluster_label = unique_labels[np.argmax(counts)]
                    largest_cluster_indices = np.where(labels == largest_cluster_label)[0]

                    if len(largest_cluster_indices) > 0:

                        # Planarity test
                        cluster_points = np.asarray(inlier_cloud.select_by_index(largest_cluster_indices).points)
                        z_variance = np.var(cluster_points[:, 2])
                        if z_variance < 0.01:

                            up_inliers = largest_cluster_indices.tolist()
                            self.get_logger().info(f"Upward Step Detected !!!")
                            up_or_down = 1
                            return up_inliers, plane_model, up_or_down  # Step detected 
    
             # DOWNSTAIRS
             if min_down_step_height < down_step_height < max_down_step_height:
                 # Apply DBSCAN clustering to group nearby points
                 labels = np.array(inlier_cloud.cluster_dbscan(eps=0.05, min_points=20, print_progress=False))
                 valid_labels = labels[labels != -1]

                 if valid_labels.size:

                    # Find the largest cluster
                    unique_labels, counts = np.unique(labels, return_counts=True)
                    largest_cluster_label = unique_labels[np.argmax(counts)]
                    largest_cluster_indices = np.where(labels == largest_cluster_label)[0]

                    if len(largest_cluster_indices) > 0:
                        # Planarity test
                        cluster_points = np.asarray(inlier_cloud.select_by_index(largest_cluster_indices).points)
                        z_variance = np.var(cluster_points[:, 2])

                        if z_variance < 0.01:
                            # Depth consistency check
                            x_to_z_values = defaultdict(list)

                            for x, _, z in cluster_points:
                                x_to_z_values[round(x, 2)].append(z)

                            is_consistent_depth = True
                            for z_values in x_to_z_values.values():
                                unique_heights = np.unique(z_values)
                                if len(unique_heights) > 5 and np.ptp(unique_heights) > depth_tolerance:
                                    is_consistent_depth = False
                                    break
                            if is_consistent_depth:
                                down_inliers = largest_cluster_indices.tolist()
                                self.get_logger().info(f"Downward Step Detected !!!")
                                up_or_down = 2
                                return down_inliers, plane_model, up_or_down  # Step detected 
                        
         # Return None if the detected plane is not horizontal
         self.get_logger().info(f"No step detected...")
         return None, None, None

    def compute_distance(self, step_points, num_closest_points=5):
        """
        Compute the distance along x from the LIDAR (or the robot's base) to the centroid of the obstacle.
        
        Parameters:
        - step_points: Nx3 numpy array of obstacle points (x, y, z).
        
        Returns:
        - distance: Distance from the LIDAR (or robot's reference frame) to the obstacle.
        """
        if len(step_points) == 0:
            self.get_logger().info("No obstacle points available to compute distance.")
            return None

        # Use only x-coordinate
        x_distances = step_points[:, 0]

        # Calculate Z-scores to filter out outliers
        mean_x = np.mean(x_distances)
        std_x = np.std(x_distances)
        z_scores = (x_distances - mean_x) / std_x

        # Filter points with a Z-score less than a threshold 
        filtered_points = step_points[np.abs(z_scores) < 2]

        if len(filtered_points) == 0:
            self.get_logger().info("No points left after outlier removal.")
            return None
            
        # Get the indices of the `num_closest_points` closest points
        closest_indices = np.argsort(np.abs(filtered_points[:, 0]))[:num_closest_points]

        # Compute the centroid of the closest points
        closest_x = filtered_points[closest_indices, 0].mean()

        # Compute the distance from the LIDAR/robot to the centroid of the closest points
        distance = np.abs(closest_x)  

        self.get_logger().info(f"Distance to obstacle: {distance:.2f} meters (centroid of closest points at {closest_x}).")

        return distance
    
    def publish_clouds(self, ground_cloud, obstacle_cloud, step_cloud, header):
            """
            Publish the ground and obstacles point clouds as ROS PointCloud2 messages.
            """
            ground_points = np.asarray(ground_cloud.points)
            obstacle_points = np.asarray(obstacle_cloud.points)
            
            if step_cloud is not None:
                step_points = np.asarray(step_cloud.points)
            else:
                step_points = []

            if len(ground_points) > 0:
                ground_msg = self.create_pointcloud2(ground_points, header)
                self.ground_pub.publish(ground_msg)

            if len(obstacle_points) > 0:
                obstacle_msg = self.create_pointcloud2(obstacle_points, header)  
                self.obstacle_pub.publish(obstacle_msg)

            if len(step_points) > 0:
                step_msg = self.create_pointcloud2(step_points, header)  
                self.step_pub.publish(step_msg)

    def create_pointcloud2(self, points, header):
        """
        Convert a numpy array of points (Nx3) into a ROS PointCloud2 message.
        """
        point_cloud_msg = pc2.create_cloud_xyz32(header, points.tolist())
        return point_cloud_msg

def main(args=None):
    rclpy.init(args=args)
    lidar_obstacle_detector = LidarStepDetector()
    rclpy.spin(lidar_obstacle_detector)
    lidar_obstacle_detector.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()