
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class ForwardNode(Node):
    def __init__(self):
        super().__init__('go_forward')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.2, self.publish_forward) # publish a message every 0.2s
        self.get_logger().info('Forward Node started: Moving forward!')

        self.speed_x = 0.1 # Forward speed (m/s)
        self.const_time_to_run = 43
        self.counter = 0

    def publish_forward(self):
        msg = Twist()
        if self.counter < self.const_time_to_run:
            msg.linear.x = self.speed_x  # Forward speed (m/s)
            self.counter += 1
            self.publisher_.publish(msg)
            self.get_logger().info('Robot is moving forward')

        else:
            self.get_logger().info('Robot stops')

def main(args=None):
    rclpy.init(args=args)
    node = ForwardNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()