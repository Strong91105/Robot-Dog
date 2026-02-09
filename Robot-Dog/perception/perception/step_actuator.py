import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from unitree_go.msg import SportModeCmd
import time

class StepActuator(Node):
    def __init__(self):
        super().__init__('step_actuator')
        self.subscription = self.create_subscription(
            String,
            '/climb_mode',
            self.mode_cb,
            10
        )
        self.cmd_pub = self.create_publisher(
            SportModeCmd,
            '/sportmodestate_cmd',
            10
        )
        self.last_action_time = 0.0
        self.action_cooldown = 3.0  # seconds
        self.get_logger().info('StepActuator started, listening to /climb_mode')

    def mode_cb(self, msg):
        mode = msg.data
        now = time.time()
        if now - self.last_action_time < self.action_cooldown:
            return
        if mode == 'climb_up':
            self.send_climb_up()
            self.last_action_time = now
        elif mode == 'climb_down':
            self.send_climb_down()
            self.last_action_time = now
        # Optionally handle 'on_pallet' or 'idle' for stability

    def send_climb_up(self):
        cmd = SportModeCmd()
        cmd.mode = 6  # Example: CLIMB UP MODE
        cmd.step_height = 0.18  # Adjust for pallet
        cmd.step_distance = 0.3
        self.cmd_pub.publish(cmd)
        self.get_logger().info('CLIMB UP COMMAND SENT')

    def send_climb_down(self):
        cmd = SportModeCmd()
        cmd.mode = 7  # Example: CLIMB DOWN MODE
        cmd.step_height = 0.18
        cmd.step_distance = 0.3
        self.cmd_pub.publish(cmd)
        self.get_logger().info('CLIMB DOWN COMMAND SENT')


def main(args=None):
    rclpy.init(args=args)
    node = StepActuator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
