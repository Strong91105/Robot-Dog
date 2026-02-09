import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from go2_interfaces.srv import Mode

class LavaWatcher(Node):
    def __init__(self):
        super().__init__('lava_watcher')

        # Target Tracking
        self.target = "lava"
        self.initial_lava_distance_m = None

        # Movement Parameters
        self.speed_linear = 0.2    
        self.target_distance = None 
        self.tolerance = 0.05      

        # State Variables
        self.start_x = None
        self.start_y = None
        self.set_start = False
        self.finished = False
        self.jump_timer = None  # To hold the timer object

        # Subscriptions & Publishers
        self.sub_dist = self.create_subscription(
            String,
            '/camera/detected_labels_distance',
            self.on_labels_distance,
            10
        )
        self.sub_odom = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_cb,
            10
        )
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)

        # Service Client
        self.mode_client = self.create_client(Mode, '/mode')

        self.get_logger().info("LavaWatcher active. Waiting for lava detection...")

    def on_labels_distance(self, msg: String):
        if self.initial_lava_distance_m is not None:
            return

        raw = (msg.data or "").strip().lower()
        if not raw or raw == "none":
            return

        items = [s.strip() for s in raw.split(",") if s.strip()]
        for item in items:
            if ":" not in item: continue
            label, dist_str = item.split(":", 1)
            if label.strip() != self.target: continue

            try:
                d = float(dist_str.strip())
                if d != d or d == float('inf'): continue
                
                self.initial_lava_distance_m = d + 1
                self.target_distance = max(0.0, d +0.10)
                self.get_logger().info(f"Lava at {d:.2f}m. Target move: {self.target_distance:.2f}m.")
            except ValueError:
                continue

    def odom_cb(self, msg):
        if self.target_distance is None or self.finished:
            return

        curr_x = msg.pose.pose.position.x
        curr_y = msg.pose.pose.position.y

        if not self.set_start:
            self.start_x, self.start_y = curr_x, curr_y
            self.set_start = True
            return

        distance_travelled = math.sqrt((curr_x - self.start_x)**2 + (curr_y - self.start_y)**2)
        remaining_distance = self.target_distance - distance_travelled

        if remaining_distance > self.tolerance:
            vel_msg = Twist()
            vel_msg.linear.x = self.speed_linear
            self.publisher_.publish(vel_msg)
            self.get_logger().info(f"Remaining: {remaining_distance:.2f}m", throttle_duration_sec=0.5)
        else:
            # STOP
            self.publisher_.publish(Twist())
            self.finished = True
            self.get_logger().info("Target reached. Settling for 1.5s...")
            
            # Create a standard timer (runs every 1.5s)
            self.jump_timer = self.create_timer(1.5, self.execute_jump)

    def execute_jump(self):
        # Immediately cancel the timer so it only runs ONCE
        if self.jump_timer is not None:
            self.jump_timer.cancel()
            self.jump_timer = None

        if not self.mode_client.service_is_ready():
            self.get_logger().error("Service /mode not ready!")
            return

        self.get_logger().info("Executing Front Jump!")
        req = Mode.Request()
        req.mode = "front_jump"
        future = self.mode_client.call_async(req)
        future.add_done_callback(self._on_mode_response)

    def _on_mode_response(self, future):
        try:
            resp = future.result()
            self.get_logger().info(f"Jump Success: {resp.success}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = LavaWatcher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()