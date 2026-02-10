import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import subprocess
import time
import signal

TIMEOUT = 1.5 # seconds

class CenteringControllerManager(Node):

    def __init__(self):
        super().__init__('centering_controller_manager')

        self.last_call_time = None
        self.process = None

        self.srv = self.create_service(
            Trigger,
            'keep_centering_controller_alive',
            self.keep_alive_callback
        )

        self.timer = self.create_timer(0.05, self.watchdog_check)

        self.get_logger().info("Centering controller manager started")

    def keep_alive_callback(self, request, response):
        self.last_call_time = time.monotonic()

        if self.process is None or self.process.poll() is not None:
            self.start_process()

        response.success = True
        response.message = "Centering controller kept alive"
        return response

    def start_process(self):
        self.get_logger().info("Starting centering_controller.py")

        self.process = subprocess.Popen([
            'python3',
            '/home/nuc-lassie/practical_course/group_ws/src/Robot-Dog/control/centering_manager/centering_manager/centering_controller.py'
        ],
            preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_IGN)
        )

    def stop_process(self):
        if self.process is not None and self.process.poll() is None:
            self.get_logger().info("Stopping centering_controller.py")
            self.process.terminate()

            try:
                self.process.wait(timeout=0.2)
            except subprocess.TimeoutExpired:
                self.get_logger().warn("Force killing centering_controller.py")
                self.process.kill()

        self.process = None

    def watchdog_check(self):
        if self.last_call_time is None:
            return

        elapsed = time.monotonic() - self.last_call_time

        if elapsed > TIMEOUT:
            self.stop_process()
            self.last_call_time = None


def main():
    rclpy.init()
    node = CenteringControllerManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
