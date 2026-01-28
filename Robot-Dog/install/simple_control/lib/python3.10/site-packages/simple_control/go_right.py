
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RightNode(Node):
    def __init__(self):
        super().__init__('go_right')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.2, self.publish_right) # publish a message every 0.2s
        self.get_logger().info('Right Node started: Moving right!')

        self.speed_y = -0.1 # Left speed (m/s)
        self.const_time_to_run = 10
        self.counter = 0

    def publish_right(self):
        msg = Twist()
        if self.counter < self.const_time_to_run:
            msg.linear.y = self.speed_y  # Forward speed (m/s)
            self.counter += 1
            self.publisher_.publish(msg)
            self.get_logger().info('Robot is moving rightward')

        else:
            self.get_logger().info('Robot stops')

def main(args=None):
    rclpy.init(args=args)
    node = RightNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()