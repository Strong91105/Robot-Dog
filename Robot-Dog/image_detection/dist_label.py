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

        self.conf_thres = 0.40
        self.iou_thres = 0.45

        # Latest depth frame (numpy) + encoding
        self.depth_img = None
        self.depth_encoding = None
        self.depth_window = 5  # odd window size for median depth

        # RGB subscription
        self.rgb_sub = self.create_subscription(
            Image,
            '/camera/camera/color/image_raw',
            self.image_cb,
            10
        )

        # Depth subscription
        self.depth_sub = self.create_subscription(
            Image,
            '/camera/camera/depth/image_rect_raw',
            self.depth_cb,
            10
        )

        # Labels only (CSV)
        self.labels_pub = self.create_publisher(
            String,
            '/camera/detected_labels',
            10
        )

        # Labels + distance (CSV: "lava:1.23,wall:0.88")
        self.labels_dist_pub = self.create_publisher(
            String,
            '/camera/detected_labels_distance',
            10
        )

        self.get_logger().info('Image Processor Node started (publishing labels + depth).')

    def depth_cb(self, msg: Image):
        try:
            # Preserve native depth type (often 16UC1 or 32FC1)
            self.depth_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            self.depth_encoding = msg.encoding
        except Exception as e:
            self.get_logger().error(f'Failed to decode depth image: {e}')
            self.depth_img = None
            self.depth_encoding = None

    def _depth_at(self, u: int, v: int) -> float:
        """
        Depth in meters at pixel (u,v), using median over a small window.
        Handles:
          - 16UC1: usually millimeters
          - 32FC1: meters
        Returns NaN if unavailable/invalid.
        """
        if self.depth_img is None:
            return float('nan')

        h, w = self.depth_img.shape[:2]
        if u < 0 or v < 0 or u >= w or v >= h:
            return float('nan')

        k = self.depth_window // 2
        x0, x1 = max(0, u - k), min(w, u + k + 1)
        y0, y1 = max(0, v - k), min(h, v + k + 1)

        patch = self.depth_img[y0:y1, x0:x1].astype(np.float32).reshape(-1)

        # Filter invalids
        patch = patch[~np.isnan(patch)]
        patch = patch[patch > 0.0]  # RealSense often uses 0 for invalid depth

        if patch.size == 0:
            return float('nan')

        d = float(np.median(patch))

        # Convert to meters depending on encoding
        enc = (self.depth_encoding or "").lower()
        if "16u" in enc or "mono16" in enc:
            d *= 0.001  # mm -> m
        # 32FC1 already meters

        return d

    def image_cb(self, msg: Image):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            results = self.model.predict(
                cv_image,
                verbose=False,
                conf=self.conf_thres,
                iou=self.iou_thres
            )
            r = results[0]

            labels = []
            label_dist_pairs = []

            if r.boxes is not None and len(r.boxes) > 0:
                boxes_xyxy = r.boxes.xyxy.detach().cpu().numpy()
                cls_ids = r.boxes.cls.detach().cpu().numpy().astype(int)

                for (x1, y1, x2, y2), cid in zip(boxes_xyxy, cls_ids):
                    name = r.names[int(cid)]
                    labels.append(name)

                    # center pixel of the box
                    u = int((x1 + x2) * 0.5)
                    v = int((y1 + y2) * 0.5)

                    d_m = self._depth_at(u, v)
                    if np.isfinite(d_m):
                        label_dist_pairs.append(f"{name}:{d_m:.2f}")
                    else:
                        label_dist_pairs.append(f"{name}:nan")

                labels = sorted(set(labels))

            self.labels_pub.publish(String(data=",".join(labels) if labels else "none"))
            self.labels_dist_pub.publish(
                String(data=",".join(label_dist_pairs) if label_dist_pairs else "none")
            )

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
