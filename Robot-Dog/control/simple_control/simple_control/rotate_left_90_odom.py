
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
class RotateLeft90Odom(Node):
    def __init__(self):
        super().__init__('rotate_left_90_odom')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscriber to odom topic
        self.subscriber_ = self.create_subscription(
            Odometry, # Topic type
            '/odom', # Topic name
            self.odom_cb,
            10)
        
        self.speed_yaw = 0.5 # Rotating speed
        self.set_target = False # Indicate when target orientation is set
        self.finished = False # Indicate when the movement is finished
        self.target = math.pi/2 # Target
        self.tolerance = 0.09 # Tolerance
        self.target_yaw = None

        
        self.get_logger().info('Rotate Left 90 started: Start Rotating!')




    def odom_cb(self, msg):
        q = msg.pose.pose.orientation
        yaw = self.quaternion_to_euler(q)
        if not self.set_target:
            # self.initial_yaw = yaw
            self.target_yaw = yaw + self.target
            self.set_target = True

        diff = abs(yaw - self.target_yaw) # Difference between current orientation and target orientation

        if diff > math.pi*2:
            diff -= 2*math.pi # 

        if diff > self.tolerance and not self.finished:
            self.get_logger().info(f'Remaining angle to rotate: {diff} rad')
            vel_msg = Twist()
            vel_msg.angular.z = self.speed_yaw
            self.publisher_.publish(vel_msg)
        else:
            self.finished = True


    def quaternion_to_euler(self, q):
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return yaw

        
def main(args=None):
    rclpy.init(args=args)
    node = RotateLeft90Odom()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()