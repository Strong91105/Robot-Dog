import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from unitree_go.msg import SportModeCmd
import time


class Go2JumpController(Node):
    def __init__(self):
        super().__init__('go2_jump_controller')

        self.subscription = self.create_subscription(
            Bool,
            '/lava_jump_required',
            self.jump_cb,
            10
        )

        self.cmd_pub = self.create_publisher(
            SportModeCmd,
            '/sportmodestate_cmd',
            10
        )

        self.last_jump_time = 0.0
        self.jump_cooldown = 3.0  # seconds

        self.get_logger().info("GO2 Jump Controller Started")

    def jump_cb(self, msg):
        if not msg.data:
            return

        now = time.time()
        if now - self.last_jump_time < self.jump_cooldown:
            return

        self.last_jump_time = now
        self.execute_jump()

    def execute_jump(self):
        cmd = SportModeCmd()
        cmd.mode = 5  # JUMP MODE (GO2)
        cmd.jump_height = 0.25
        cmd.jump_distance = 0.4

        self.cmd_pub.publish(cmd)
        self.get_logger().info("JUMP COMMAND SENT")


def main(args=None):
    rclpy.init(args=args)
    node = Go2JumpController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
