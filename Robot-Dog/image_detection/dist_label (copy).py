import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String, Float32  # Using Float32 for decimal accuracy
from cv_bridge import CvBridge
from ultralytics import YOLO
import numpy as np
import os

class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')

        self.bridge = CvBridge()
        
        # --- Model Setup ---
        script_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(script_dir, "best.pt")
        self.get_logger().info(f"Loading YOLO model from: {model_path}")
        self.model = YOLO(model_path)

        # Detection Parameters
        self.conf_thres = 0.40
        self.iou_thres = 0.45
        self.target_label = "lava"

        # Depth Data Storage
        self.depth_img = None
        self.depth_encoding = None
        self.depth_window = 5  # 5x5 pixel window for median depth calculation

        # --- Subscriptions ---
        self.rgb_sub = self.create_subscription(
            Image, 
            '/camera/camera/color/image_raw', 
            self.image_cb, 
            10
        )
        self.depth_sub = self.create_subscription(
            Image, 
            '/camera/camera/depth/image_rect_raw', 
            self.depth_cb, 
            10
        )

        # --- Publishers ---
        # 1. Original String Publisher (for debugging/all labels)
        self.labels_dist_pub = self.create_publisher(
            String, 
            '/camera/detected_labels_distance_meters', 
            10
        )

        # 2. NEW: Precise Float Publisher (for the Lava Watcher script)
        self.lava_float_pub = self.create_publisher(
            Float32, 
            '/camera/lava_distance_float', 
            10
        )

        self.lava_target = self.create_publisher(
            Float32, 
            '/camera/lava_target', 
            10
        )

        self.get_logger().info(f'Image Processor started. Target: {self.target_label}')

    def depth_cb(self, msg: Image):
        try:
            self.depth_img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
            self.depth_encoding = msg.encoding
        except Exception as e:
            self.get_logger().error(f'Depth decode failed: {e}')

    def _depth_at(self, u: int, v: int) -> float:
        """Calculates median depth in meters from a window around pixel (u,v)."""
        if self.depth_img is None:
            return float('nan')
        
        h, w = self.depth_img.shape[:2]
        if u < 0 or v < 0 or u >= w or v >= h:
            return float('nan')

        k = self.depth_window // 2
        y0, y1 = max(0, v - k), min(h, v + k + 1)
        x0, x1 = max(0, u - k), min(w, u + k + 1)
        
        patch = self.depth_img[y0:y1, x0:x1].astype(np.float32).reshape(-1)
        patch = patch[~np.isnan(patch)]
        patch = patch[patch > 0.0]  # Filter out 0 (invalid depth)

        if patch.size == 0:
            return float('nan')

        d = float(np.median(patch))

        # Handle mm to m conversion if encoding is 16-bit
        enc = (self.depth_encoding or "").lower()
        if "16u" in enc or "mono16" in enc:
            d *= 0.001 
            
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

            label_dist_pairs = []
            lava_dist = None
            target = 50

            if r.boxes is not None:
                boxes_xyxy = r.boxes.xyxy.cpu().numpy()
                cls_ids = r.boxes.cls.cpu().numpy().astype(int)

                for box, cid in zip(boxes_xyxy, cls_ids):
                    name = r.names[int(cid)]
                    
                    # Calculate center pixel of bounding box
                    u = int((box[0] + box[2]) * 0.5)
                    v = int((box[1] + box[3]) * 0.5)
                    
                    d_m = self._depth_at(u, v)

                    if np.isfinite(d_m):
                        label_dist_pairs.append(f"{name}:{d_m:.2f}")
                        # If we found lava, store the distance
                        if name.lower() == self.target_label:
                            lava_dist = d_m
                    else:
                        label_dist_pairs.append(f"{name}:nan")

            # --- Publish String Data ---
            data_str = ",".join(label_dist_pairs) if label_dist_pairs else "none"
            self.labels_dist_pub.publish(String(data=data_str))

            # --- Publish Lava Float Data ---
            if lava_dist is not None:
                float_msg = Float32()
                float_msg.data = float(lava_dist)
                self.lava_float_pub.publish(float_msg)
                self.lava_target.publish(target)

        except Exception as e:
            self.get_logger().error(f'Image processing error: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()