import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2
import os


class LavaDetector(Node):
    def __init__(self):
        super().__init__('lava_detector')

        self.bridge = CvBridge()
        # 1. Fix: Dynamic Pathing for best.pt
        script_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(script_dir, "best.pt")
        
        self.get_logger().info(f"Loading YOLO model from: {model_path}")
        self.model = YOLO(model_path)

        # Camera subscriber
        self.subscription = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.image_cb,
            10
        )

        # Debug image publisher
        self.image_pub = self.create_publisher(
            Image,
            '/camera/image_processed',
            10
        )

        # Lava jump signal publisher
        self.jump_pub = self.create_publisher(
            Bool,
            '/lava_jump_required',
            10
        )

        self.get_logger().info("Lava Detector Node Started")

    def image_cb(self, msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            results = self.model(cv_image)

            lava_close = False
            image_height = cv_image.shape[0]

            for box in results[0].boxes:
                class_id = int(box.cls[0])
                class_name = self.model.names[class_id]

                if class_name == "lava":
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    lava_bottom = y2

                    # Distance heuristic (camera-based)
                    if lava_bottom > image_height * 0.65:
                        lava_close = True

            # Publish jump signal
            msg_out = Bool()
            msg_out.data = lava_close
            self.jump_pub.publish(msg_out)

            if lava_close:
                self.get_logger().info("LAVA CLOSE → REQUEST JUMP")

            # Publish debug image
            debug_img = results[0].plot()
            debug_msg = self.bridge.cv2_to_imgmsg(debug_img, encoding='bgr8')
            self.image_pub.publish(debug_msg)

        except Exception as e:
            self.get_logger().error(f"Image processing failed: {e}")


def main(args=None):
    rclpy.init(args=args)
    node = LavaDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
