import math

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from go2_interfaces.srv import Mode  # ensure this package is sourced/installed


class LavaWatcher(Node):
    def __init__(self):
        super().__init__('lava_watcher')

        self.target = "lava"
        self.initial_lava_distance_m = None
        self.initial_lava_time = None

        self.sub = self.create_subscription(
            String,
            '/camera/detected_labels_distance',
            self.on_labels_distance,
            10
        )

        self.get_logger().info("LavaWatcher started. Will store initial lava distance once.")

        # ---- Walking stuff you provided ----
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_cb,
            10
        )

        # Movement Parameters
        self.speed_linear = 0.2    # meters per second
        self.target_distance = None  # set once lava distance is stored
        self.tolerance = 0.05      # distance tolerance

        # State Variables
        self.start_x = None
        self.start_y = None
        self.set_start = False
        self.finished = False

        # ---- Jump command client (from initial script) ----
        self.mode_client = self.create_client(Mode, '/mode')

    def on_labels_distance(self, msg: String):
        # One-shot: already stored -> ignore all future messages
        if self.initial_lava_distance_m is not None:
            return

        raw = (msg.data or "").strip().lower()
        if not raw or raw == "none":
            return

        items = [s.strip() for s in raw.split(",") if s.strip()]
        for item in items:
            if ":" not in item:
                continue

            label, dist_str = item.split(":", 1)
            label = label.strip()
            dist_str = dist_str.strip()

            if label != self.target:
                continue

            try:
                d = float(dist_str)
            except ValueError:
                continue

            if not (d == d) or d in (float("inf"), float("-inf")):
                continue

            self.initial_lava_distance_m = d
            self.initial_lava_time = self.get_clock().now()

            # Hook into your walking logic
            self.target_distance = self.initial_lava_distance_m-0.15
            self.finished = False
            self.set_start = False
            self.start_x = None
            self.start_y = None

            self.get_logger().info(
                f"Stored initial lava distance: {d:.3f} m "
                f"(t={self.initial_lava_time.nanoseconds / 1e9:.3f}s)."
            )
            self.get_logger().info(f"Moving forward {self.target_distance:.3f} meters...")
            return

    def odom_cb(self, msg):
        # Don’t do anything until we have a target distance from lava detection
        if self.target_distance is None:
            return

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
            self.get_logger().info(
                f"Travelled: {distance_travelled:.2f}m | Remaining: {remaining_distance:.2f}m",
                throttle_duration_sec=0.5
            )
            vel_msg = Twist()
            vel_msg.linear.x = self.speed_linear
            self.publisher_.publish(vel_msg)
        else:
            # Stop the robot
            self.publisher_.publish(Twist())
            self.finished = True
            self.get_logger().info("Target reached! Stopping.")

            # ---- Added: jump AFTER reaching target ----
            self.jump_front()

    # Jump command from the initial script
    def jump_front(self):
        if not self.mode_client.service_is_ready():
            self.get_logger().warn("Service /mode not available yet.")
            return

        req = Mode.Request()
        req.mode = "front_jump"
        future = self.mode_client.call_async(req)
        future.add_done_callback(self._on_mode_response)

    def _on_mode_response(self, future):
        try:
            resp = future.result()
            self.get_logger().info(f"/mode response: success={resp.success}, message='{resp.message}'")
        except Exception as e:
            self.get_logger().error(f"/mode call failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = LavaWatcher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
