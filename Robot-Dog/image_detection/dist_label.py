import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge
from ultralytics import YOLO
import numpy as np


class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')

        self.bridge = CvBridge()
        self.model = YOLO("best.pt")  # load once

        # Confidence threshold (tune this)
        self.conf_thres = 0.40

        self.subscription = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.image_cb,
            10
        )

        self.image_pub = self.create_publisher(
            Image,
            '/camera/image_processed',
            10
        )

        # Publish labels (CSV)
        self.labels_pub = self.create_publisher(
            String,
            '/camera/detected_labels',
            10
        )

        # Optional: publish label+confidence (debug)
        self.labels_debug_pub = self.create_publisher(
            String,
            '/camera/detected_labels_debug',
            10
        )

        self.get_logger().info('Image Processor Node started.')

    def image_cb(self, msg: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            results = self.model.predict(cv_image, verbose=False)
            r = results[0]

            labels = []
            debug_pairs = []

            if r.boxes is not None and len(r.boxes) > 0:
                confs = r.boxes.conf.detach().cpu().numpy()
                cls_ids = r.boxes.cls.detach().cpu().numpy().astype(int)

                keep = confs >= self.conf_thres
                confs = confs[keep]
                cls_ids = cls_ids[keep]

                # Convert class ids -> names
                names = [r.names[c] for c in cls_ids]

                # Unique labels (recommended)
                labels = sorted(set(names))

                # Optional debug list: "label:0.83"
                debug_pairs = [f"{r.names[c]}:{float(conf):.2f}" for c, conf in zip(cls_ids, confs)]

            # Publish labels as CSV (empty -> "none")
            self.labels_pub.publish(String(data=",".join(labels) if labels else "none"))
            self.labels_debug_pub.publish(String(data=",".join(debug_pairs) if debug_pairs else "none"))

            # Annotated image output
            annotated = r.plot()
            processed_msg = self.bridge.cv2_to_imgmsg(annotated, encoding='bgr8')
            processed_msg.header = msg.header
            self.image_pub.publish(processed_msg)

        except Exception as e:
            self.get_logger().error(f'Failed to process image: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
