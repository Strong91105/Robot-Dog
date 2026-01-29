import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import message_filters
from std_srvs.srv import Trigger
import os
import numpy as np

class ArrowDetector(Node):
    def __init__(self):
        super().__init__('arrow_detector')
        
        self.bridge = CvBridge()
        
        # 1. Fix: Dynamic Pathing for best.pt
        script_dir = os.path.dirname(os.path.realpath(__file__))
        model_path = os.path.join(script_dir, "best.pt")
        
        self.get_logger().info(f"Loading YOLO model from: {model_path}")
        self.model = YOLO(model_path)
        
        # 2. Service Clients
        self.left_turn_client = self.create_client(Trigger, 'left_90_deg_turn')
        self.right_turn_client = self.create_client(Trigger, 'right_90_deg_turn')
        
        self.get_logger().info("Waiting for rotation services...")
        self.left_turn_client.wait_for_service(timeout_sec=5.0)
        self.right_turn_client.wait_for_service(timeout_sec=5.0)

        # 3. Fix: Corrected Depth Topic Name
        self.color_sub = message_filters.Subscriber(self, Image, '/camera/camera/color/image_raw')
        self.depth_sub = message_filters.Subscriber(self, Image, '/camera/camera/depth/image_rect_raw')
        
        # 4. Syncing with a slightly larger slop for network/processing lag
        self.ts = message_filters.ApproximateTimeSynchronizer(
            [self.color_sub, self.depth_sub], queue_size=10, slop=0.2
        )
        self.ts.registerCallback(self.process_frame)

        self.processing_turn = False
        self.get_logger().info('--- Arrow Detector with Depth Sensing Active ---')

    def process_frame(self, color_msg, depth_msg):
        if self.processing_turn:
            return

        try:
            # Convert ROS to OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(color_msg, desired_encoding='bgr8')
            # Depth is usually 16-bit unsigned (millimeters)
            depth_image = self.bridge.imgmsg_to_cv2(depth_msg, desired_encoding='passthrough')

            results = self.model(cv_image, verbose=False)

            for r in results:
                for box in r.boxes:
                    conf = box.conf[0]
                    if conf < 0.5: continue  # Skip low confidence

                    # Bounding Box Coordinates
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    
                    # 5. Fix: Handle potential resolution mismatch between Color and Depth
                    # We scale the center point to match depth image dimensions
                    v_scale = depth_image.shape[0] / cv_image.shape[0]
                    h_scale = depth_image.shape[1] / cv_image.shape[1]
                    d_cx, d_cy = int(cx * h_scale), int(cy * v_scale)

                    # 6. Extract Depth and filter out invalid 0 values (too close/reflecting)
                    dist_mm = depth_image[d_cy, d_cx]
                    if dist_mm == 0:
                        # If center is 0, check a small window around center for a valid reading
                        patch = depth_image[max(0, d_cy-5):d_cy+5, max(0, d_cx-5):d_cx+5]
                        dist_mm = np.median(patch[patch > 0]) if np.any(patch > 0) else 0

                    dist_m = float(dist_mm) / 1000.0
                    label = self.model.names[int(box.cls[0])]

                    # 7. Logic: Detection Distance Gate
                    # Tuned for robot dog walking speed
                    if 0.2 < dist_m < 0.8: 
                        self.get_logger().info(f"!!! {label.upper()} at {dist_m:.2f}m !!!")
                        self.call_turn_service(label)

        except Exception as e:
            self.get_logger().error(f'Processing Error: {e}')

    def call_turn_service(self, direction):
        self.processing_turn = True
        request = Trigger.Request()
        
        # Determine service based on label
        if 'left' in direction.lower():
            self.get_logger().info("Sending Left Turn Request...")
            future = self.left_turn_client.call_async(request)
        else:
            self.get_logger().info("Sending Right Turn Request...")
            future = self.right_turn_client.call_async(request)
            
        future.add_done_callback(self.turn_finished_callback)

    def turn_finished_callback(self, future):
        try:
            response = future.result()
            if response.success:
                self.get_logger().info("Turn finished! Resuming detection...")
            else:
                self.get_logger().warn(f"Service returned failure: {response.message}")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")
        
        # Ensure we unlock detection even if the service failed
        self.processing_turn = False

def main(args=None):
    rclpy.init(args=args)
    node = ArrowDetector()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()