import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from unitree_go.msg import SportModeCmd
import math
import time

class PalletDebugSwitcher(Node):
    def __init__(self):
        super().__init__('pallet_debug_switcher')

        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_cb, 10)
        self.imu_sub = self.create_subscription(Imu, '/imu/data', self.imu_cb, 10)
        self.cmd_pub = self.create_publisher(SportModeCmd, '/sport_mode', 10)

        # Thresholds - Adjusted for sensitivity
        self.target_height = 0.11    # Lowered slightly to account for compression
        self.pitch_tolerance = 0.15  # Loosened to 8 degrees
        self.wait_duration = 5.0
        
        self.initial_z = None
        self.current_z = 0.0
        self.current_pitch = 0.0
        self.state = "CALIBRATING"
        
        # Timer for logging so we don't spam the terminal
        self.timer = self.create_timer(0.5, self.log_status)

    def odom_cb(self, msg):
        # Check if height is actually in Z. On some Go2 setups, check msg.pose.pose.position.y too.
        self.current_z = msg.pose.pose.position.z
        
        if self.state == "CALIBRATING" and self.current_z != 0.0:
            self.initial_z = self.current_z
            self.state = "MONITORING"
            self.get_logger().info(f"CALIBRATED. Initial Z: {self.initial_z:.3f}")

    def imu_cb(self, msg):
        q = msg.orientation
        # Standard Pitch calculation
        sinp = 2 * (q.w * q.y - q.z * q.x)
        self.current_pitch = math.asin(sinp) if abs(sinp) < 1 else math.copysign(math.pi/2, sinp)
        
        self.check_logic()

    def log_status(self):
        if self.state != "CALIBRATING" and self.initial_z is not None:
            height_diff = self.current_z - self.initial_z
            self.get_logger().info(
                f"STATUS: Height Diff: {height_diff:.3f}m | Pitch: {math.degrees(self.current_pitch):.1f}° | State: {self.state}"
            )

    def check_logic(self):
        if self.state == "MONITORING":
            height_diff = self.current_z - self.initial_z
            
            # The detection condition
            if height_diff > self.target_height and abs(self.current_pitch) < self.pitch_tolerance:
                self.get_logger().warn("!!! CLIMB DETECTED !!!")
                self.climb_detected_time = time.time()
                self.state = "WAITING"

        elif self.state == "WAITING":
            if time.time() - self.climb_detected_time >= self.wait_duration:
                self.switch_gait()
                self.state = "FINISHED"

    def switch_gait(self):
        msg = SportModeCmd()
        msg.gait_type = 3 
        self.cmd_pub.publish(msg)
        self.get_logger().error("GAIT SWITCHED TO STAIR MODE")

def main(args=None):
    rclpy.init(args=args)
    node = PalletDebugSwitcher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()