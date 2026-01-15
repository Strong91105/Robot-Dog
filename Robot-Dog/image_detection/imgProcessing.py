import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from ultralytics import YOLO




class ImageProcessor(Node):
    def __init__(self):
        super().__init__('image_processor')

        self.bridge = CvBridge()

        self.subscription = self.create_subscription(
            Image,
            '/go2/Image',
            self.image_cb,
            10
        )

        self.publisher = self.create_publisher(
            Image,
            '/camera/image_processed',
            10
        )

        self.get_logger().info('Image Processor Node started.')


    def image_cb(self, msg):
        model = YOLO("best.pt")
        try:
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8') #ROS to OpenCV
            
            results = model(cv_image)
            result = results[0].plot()
           ## gray_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
            
            processed_msg = self.bridge.cv2_to_imgmsg(result, encoding='bgr8') #Back to ROS Image messag

            self.publisher.publish(processed_msg)

        except Exception as e:
            self.get_logger().error(f'Failed to process image: {e}')

    
def main(args=None):
    rclpy.init(args=args)
    node = ImageProcessor()
    rclpy.spin(node)
    node.destroy_node
    rclpy.shutdown()



if __name__ == '__main__':
    main()