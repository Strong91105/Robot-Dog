import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math


class MoveBackwardOdom(Node):
    def __init__(self):
        super().__init__('move_backward_odom')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_cb,
            10
        )

        self.speed_linear = -0.2        # Forward speed (m/s)
        self.target_distance = 0.5     # Distance to move forward (meters)
        self.tolerance = 0.05

        self.start_x = None
        self.start_y = None
        self.finished = False

        self.get_logger().info('Move Backward started: Moving backward!')

    def odom_cb(self, msg):
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        if self.start_x is None:
            self.start_x = x
            self.start_y = y
            return

        distance = math.sqrt(
            (x - self.start_x) ** 2 +
            (y - self.start_y) ** 2
        )

        remaining = self.target_distance - distance

        if remaining > self.tolerance and not self.finished:
            self.get_logger().info(f'Remaining distance: {remaining:.2f} m')
            vel_msg = Twist()
            vel_msg.linear.x = self.speed_linear
            self.publisher_.publish(vel_msg)
        else:
            self.finished = True
            vel_msg = Twist()  # stop robot
            self.publisher_.publish(vel_msg)
            self.get_logger().info('Target distance reached. Stopping.')


def main(args=None):
    rclpy.init(args=args)
    node = MoveBackwardOdom()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
