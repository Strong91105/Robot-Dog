import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2

import numpy as np
from numpy.lib import recfunctions as rfn
import matplotlib.pyplot as plt

from sklearn import linear_model
import time

class LidarSubscriber(Node):
    def __init__(self):
        super().__init__("wall_detection")
        # Subscribe to the LIDAR point cloud topic
        self.subscription = self.create_subscription(
            PointCloud2,
            '/utlidar/cloud',
            self.lidar_callback,
            1
        )
        self.publisher_wall_data = self.create_publisher(
            Float32MultiArray,
            "/wall_data",
            1
        )

        # Robustly fit linear model with RANSAC algorithm
        self.ransac_regressor_left = linear_model.RANSACRegressor()
        self.ransac_regressor_right = linear_model.RANSACRegressor()
        self.wall_data_msg = Float32MultiArray() # [yaw angle, y-axis distance] 
        plt.ion()

    def lidar_callback(self, msg):
        # convert point cloud message to numpy array
        point_cloud = pc2.read_points(msg)
        point_cloud = rfn.structured_to_unstructured(point_cloud[['x', 'y', 'z']])

        # filter the point cloud for the left and right wall points
        wall_points = point_cloud.copy()
        # TODO: filter the point cloud in x and z direction
        threshold_z_axis = -0.05# TODO
        threshold_x_axis = 0.52 #TODO
        wall_points = wall_points[wall_points[:, 2] > threshold_z_axis] # Z-axis
        wall_points = wall_points[(wall_points[:, 0] < threshold_x_axis) & (wall_points[:, 0] > -0.35)]  # X-axis
        #wall_points = wall_points[abs(wall_points[:, 0]) < threshold_x_axis] # X-axis

        left_wall = wall_points.copy()
        # TODO: filter the point cloud in y direction
        threshold_y_axis = 0.42 # TODO
        left_wall = left_wall[(left_wall[:, 1] > threshold_y_axis) & (left_wall[:, 1] < 0.58)]   # Y-axis
        right_wall = wall_points.copy()
        right_wall = right_wall[(right_wall[:, 1] < -threshold_y_axis) & (right_wall[:, 1] > -0.58)] # Y-axis
        
        if len(left_wall) > 1 and len(right_wall) > 1:

            self.ransac_regressor_left.fit(left_wall[:, 1].reshape(-1, 1), left_wall[:, 0])
            self.ransac_regressor_right.fit(right_wall[:, 1].reshape(-1, 1), right_wall[:, 0])

            slope_left = self.ransac_regressor_left.estimator_.coef_
            slope_right = self.ransac_regressor_right.estimator_.coef_

            intercept_l = self.ransac_regressor_left.estimator_.intercept_
            intercept_r = self.ransac_regressor_right.estimator_.intercept_

            angle_left = np.arctan2(slope_left, 1) # [rad]
            angle_right = np.arctan2(slope_right, 1) # [rad]
            angle = np.mean([angle_left, angle_right])

            plt.clf()
            plt.plot(left_wall[:, 1], intercept_l + slope_left*left_wall[:, 1], 'r-', label="RANSAC regressor left",)
            plt.plot(right_wall[:, 1], intercept_r + slope_right*right_wall[:, 1], 'r-', label="RANSAC regressor right",)
            plt.plot(wall_points[:, 1], wall_points[:, 0], 'b.', label="Point cloud")

            plt.title('Fitted Lines')
            plt.axvline(0, color='g', label='Middle')
            plt.ylim([-2.0, 2.0])
            plt.xlim([-2.0, 2.0])
            plt.gca().invert_xaxis()
            # plt.axis('equal')
            plt.legend(loc='lower right')
            plt.pause(0.01)

            wall_distance_l = - (intercept_l / slope_left)
            wall_distance_r = - (intercept_r / slope_right)
            wall_distance = abs(wall_distance_l) - abs(wall_distance_r)

            print(f"angle: {angle} [rad], wall_distance: {wall_distance.item()} [m]")

            self.wall_data_msg.data = [angle.item(), wall_distance.item()]
            self.publisher_wall_data.publish(self.wall_data_msg)
        
        else:
            
            print(f"Not enough points to interpolate!")

    def convert_pointcloud2_to_numpy(self, cloud_msg):

        # Convert ROS2 PointCloud2 to a numpy array (x, y, z)
        points = np.array(list(pc2.read_points(cloud_msg, field_names=("x", "y", "z"), skip_nans=True)))
        xyz = rfn.structured_to_unstructured(points)

        return xyz


def main(args=None):
    rclpy.init(args=args)
    lidar_subscriber = LidarSubscriber()
    plt.show()
    rclpy.spin(lidar_subscriber)
    lidar_subscriber.destroy_node()
    rclpy.shutdown()
    # pipeline.stop()


if __name__ == "__main__":
    main()
    