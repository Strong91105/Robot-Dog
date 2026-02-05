import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class LavaWatcher(Node):
    def __init__(self):
        super().__init__('lava_watcher')

        self.target = "lava"

        self.sub = self.create_subscription(
            String,
            '/camera/detected_labels_distance',
            self.on_labels,
            10
        )

        self.get_logger().info("LavaWatcher started. Listening on /camera/detected_labels")

    def on_labels(self, msg: String):
        raw = (msg.data or "").strip().lower()

        if not raw or raw == "none":
            return

        labels = {s.strip() for s in raw.split(",") if s.strip()}

        if self.target in labels:
            self.on_lava_detected(labels)

    def on_lava_detected(self, labels):
        self.get_logger().warn(f"🔥 LAVA DETECTED! labels={sorted(labels)}")
        self.execute_lava_function()

    def execute_lava_function(self):
        # Replace with your actual behavior
        self.get_logger().info("Executing lava response function...")


def main(args=None):
    rclpy.init(args=args)
    node = LavaWatcher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
