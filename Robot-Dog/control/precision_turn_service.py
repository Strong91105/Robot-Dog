import rclpy
from rclpy.node import Node
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from std_srvs.srv import Trigger
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import time

class PrecisionTurnService(Node):
    def __init__(self):
        super().__init__('precision_turn_service')
        
        # ReentrantCallbackGroup allows the executor to run odom_callback 
        # while the handle_turn service is still active.
        self.group = ReentrantCallbackGroup()
        
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        self.odom_sub = self.create_subscription(
            Odometry, 
            '/odom', 
            self.odom_callback, 
            10,
            callback_group=self.group
        )
        
        self.left_srv = self.create_service(
            Trigger, 
            'left_90_deg_turn', 
            self.handle_left_turn,
            callback_group=self.group
        )
        
        self.right_srv = self.create_service(
            Trigger, 
            'right_90_deg_turn', 
            self.handle_right_turn,
            callback_group=self.group
        )
        
        self.current_yaw = 0.0
        self.get_logger().info("90-Degree Turn Service Ready and listening...")

    def odom_callback(self, msg):
        # Convert Quaternion to Euler (Yaw)
        q = msg.pose.pose.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.current_yaw = math.atan2(siny_cosp, cosy_cosp)

    def handle_left_turn(self, request, response):
        self.get_logger().info("Received Left Turn Request")
        success = self.perform_precise_turn(target_relative_angle=math.pi / 2) 
        response.success = success
        response.message = "Left turn completed" if success else "Turn failed"
        return response

    def handle_right_turn(self, request, response):
        self.get_logger().info("Received Right Turn Request")
        success = self.perform_precise_turn(target_relative_angle=-math.pi / 2) 
        response.success = success
        response.message = "Right turn completed" if success else "Turn failed"
        return response

    def perform_precise_turn(self, target_relative_angle):
        start_yaw = self.current_yaw
        target_yaw = self.normalize_angle(start_yaw + target_relative_angle)
        
        msg = Twist()
        # Rotation speed: +ve for left (CCW), -ve for right (CW)
        speed = 0.4 if target_relative_angle > 0 else -0.4
        
        self.get_logger().info(f"Current Yaw: {start_yaw:.2f} | Target: {target_yaw:.2f}")

        try:
            # Control Loop - MultiThreadedExecutor keeps odom_callback running in background
            while rclpy.ok():
                remaining_angle = self.normalize_angle(target_yaw - self.current_yaw)
                
                # If we are within ~3 degrees of target
                if abs(remaining_angle) < 0.05: 
                    break
                    
                msg.angular.z = speed
                self.cmd_vel_pub.publish(msg)
                
                # Small sleep to prevent CPU hogging
                time.sleep(0.02)

            # Stop the robot
            msg.angular.z = 0.0
            self.cmd_vel_pub.publish(msg)
            self.get_logger().info("Turn Complete.")
            return True

        except Exception as e:
            self.get_logger().error(f"Error during turn: {e}")
            # Emergency Stop
            msg.angular.z = 0.0
            self.cmd_vel_pub.publish(msg)
            return False

    def normalize_angle(self, angle):
        while angle > math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    node = PrecisionTurnService()
    
    # Use MultiThreadedExecutor so services and subscriptions don't block each other
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    
    try:
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info("Shutting down node...")
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()