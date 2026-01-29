import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool, Float32MultiArray
from cv_bridge import CvBridge


class LavaDetector(Node):
    def __init__(self):
        super().__init__('lava_detector')

        self.bridge = CvBridge()
        self.latest_detections = None
        self.image_height = None

        # Processed image (visual only)
        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_processed',
            self.image_cb,
            10
        )

        # YOLO detection data
        self.detection_sub = self.create_subscription(
            Float32MultiArray,
            '/camera/detected_labels',
            self.detection_cb,
            10
        )

        # Jump command
        self.jump_pub = self.create_publisher(
            Bool,
            '/lava_jump_required',
            10
        )

        self.class_names = ["lava"]  # match your YOLO classes
        self.get_logger().info("Lava Detector Node Started")

    def detection_cb(self, msg):
        self.latest_detections = msg.data

    def image_cb(self, msg):
     
        lava_close = False
        data = self.latest_detections

        while True:
            if self.latest_detections == "lava":
                self.get_logger().info("Lava seen")
                self.jump_pub.pusblish(jump_msg)

        jump_msg = Bool()
        jump_msg.data = lava_close
        self.jump_pub.publish(jump_msg)

        if lava_close:
            self.get_logger().info("🔥 LAVA CLOSE → JUMP")


def main(args=None):
    rclpy.init(args=args)
    node = LavaDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
