import rclpy
from rclpy.node import Node
from std_msgs.msg import String


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

            self.get_logger().info(
                f"Stored initial lava distance: {d:.3f} m "
                f"(t={self.initial_lava_time.nanoseconds / 1e9:.3f}s)."
            )
            return


def main(args=None):
    rclpy.init(args=args)
    node = LavaWatcher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
