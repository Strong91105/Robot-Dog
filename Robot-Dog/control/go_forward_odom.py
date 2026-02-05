import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math

class MoveForwardOdom(Node):
    def __init__(self):
        super().__init__('move_forward_odom')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(
            Odometry, 
            '/odom', 
            self.odom_cb, 
            10)
        
        # Movement Parameters
        self.speed_linear = 0.2    # meters per second
        self.target_distance = 1.0 # meters to travel
        self.tolerance = 0.05      # distance tolerance
        
        # State Variables
        self.start_x = None
        self.start_y = None
        self.set_start = False
        self.finished = False

        self.get_logger().info(f'Moving forward {self.target_distance} meters...')

    def odom_cb(self, msg):
        if self.finished:
            return

        # Get current position
        curr_x = msg.pose.pose.position.x
        curr_y = msg.pose.pose.position.y

        # Initialize start position once
        if not self.set_start:
            self.start_x = curr_x
            self.start_y = curr_y
            self.set_start = True
            return

        # Calculate Euclidean distance: sqrt((x2-x1)^2 + (y2-y1)^2)
        distance_travelled = math.sqrt(
            (curr_x - self.start_x)**2 + (curr_y - self.start_y)**2
        )

        remaining_distance = self.target_distance - distance_travelled

        if remaining_distance > self.tolerance:
            self.get_logger().info(f'Travelled: {distance_travelled:.2f}m | Remaining: {remaining_distance:.2f}m', throttle_duration_sec=0.5)
            vel_msg = Twist()
            vel_msg.linear.x = self.speed_linear
            self.publisher_.publish(vel_msg)
        else:
            # Stop the robot
            self.publisher_.publish(Twist()) 
            self.finished = True
            self.get_logger().info('Target reached! Stopping.')

def main(args=None):
    rclpy.init(args=args)
    node = MoveForwardOdom()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()