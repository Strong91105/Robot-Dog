import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from geometry_msgs.msg import Twist

class WallFollower(Node):
    def __init__(self):
        super().__init__('wall_follower_controller')
        
        # Subscribe to  LIDAR output
        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/wall_data',
            self.listener_callback,
            10)
        
        # Publish to the robot's velocity topic
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        
        self.kp_lateral = 0.35   # How hard to push back to center CHANGE
        self.kp_angular = 4.5   # How hard to steer straight CHANGE
        
        self.get_logger().info('Centering Controller Online:')

    def listener_callback(self, msg):
        # msg.data[0] is angle (yaw)
        # msg.data[1] is wall_distance (lateral error)
        angle_error = msg.data[0]
        lateral_error = msg.data[1]

        cmd = Twist()

        
        cmd.linear.y = self.kp_lateral * lateral_error

        
        # If the robot is slanted, rotate it back to 0
        cmd.angular.z = -(self.kp_angular * angle_error)

        # 3. FORWARD SPEED (CAREFUL)
        cmd.linear.x = 0.2
 

        # SAFETY: Limit max speeds
        cmd.linear.y = max(min(cmd.linear.y, 0.4), -0.4)
        cmd.angular.z = max(min(cmd.angular.z, 0.5), -0.5)

        self.publisher_.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    node = WallFollower()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()