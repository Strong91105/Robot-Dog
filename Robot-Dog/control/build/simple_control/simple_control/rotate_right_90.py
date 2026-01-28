
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class RotateRight90(Node):
    def __init__(self):
        super().__init__('rotate_right_90')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.09, self.publish_forward) # publish a message every 0.1s
        self.get_logger().info('Rotate right 90 started: Start Rotating!')

        self.speed_yaw = -0.5 # TODO try some other velocities, but maximum 0.5
        self.const_time_to_run = 31 # Number of times to publish the Twist message. TODO calculate this based on the angle and speed you want to rotate
        self.counter = 0

    def publish_forward(self):
        msg = Twist()
        if self.counter < self.const_time_to_run:
            msg.angular.z = self.speed_yaw
            self.counter += 1
            self.publisher_.publish(msg)
            self.get_logger().info('Robot is rotating')

        else:
            self.get_logger().info('Robot stops')

def main(args=None):
    rclpy.init(args=args)
    node = RotateRight90()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()