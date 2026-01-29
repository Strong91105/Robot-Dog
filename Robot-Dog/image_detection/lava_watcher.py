import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from go2_interfaces.srv import Mode  # ensure this package is sourced/installed


class LavaWatcher(Node):
    def __init__(self):
        super().__init__('lava_watcher')

        self.target = "lava"
        self.dist_threshold_m = 0.80  # 80 cm

        # Subscribe to labels+distance published by your detector:
        # e.g. "lava:0.72,wall:1.10" or "none"
        self.sub = self.create_subscription(
            String,
            '/camera/detected_labels_distance',
            self.on_labels_distance,
            10
        )

        # Service client for the jump command:
        # ros2 service call /mode go2_interfaces/srv/Mode "mode: 'front_jump'"
        self.mode_client = self.create_client(Mode, '/mode')

        self.get_logger().info("LavaWatcher started. Listening on /camera/detected_labels_distance")

    def on_labels_distance(self, msg: String):
        raw = (msg.data or "").strip().lower()
        if not raw or raw == "none":
            return

        # Parse "label:dist" CSV
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

            # Ignore nan/inf
            if not (d == d) or d == float("inf") or d == float("-inf"):
                continue

            # Trigger jump if lava is within 80 cm
            if d <= self.dist_threshold_m:
                self.jump_front()
                return  # one jump per message is enough

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
