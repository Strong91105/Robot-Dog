import os
import signal
import subprocess
import rclpy
import py_trees
import py_trees_ros
from std_msgs.msg import Float32
from go2_interfaces.srv import Mode 

# --- 1. Lava Subscriber ---
class LavaSubscriber(py_trees.behaviour.Behaviour):
    def __init__(self, name="Lava Check", topic_name="/camera/lava_distance_float", threshold=40):
        super().__init__(name)
        self.topic_name = topic_name
        self.threshold = threshold
        self.current_distance = float('inf')
        self.node = None

    def setup(self, **kwargs):
        self.node = kwargs.get('node')
        self.node.create_subscription(Float32, self.topic_name, self._cb, 10)
        return True

    def _cb(self, msg):
        self.current_distance = msg.data

    def update(self):
        # Debug Logging: Compare current vs threshold
        self.logger.info(f"Lava Dist: {self.current_distance:.2f} | Threshold: {self.threshold}")
        
        if self.current_distance <= self.threshold:
            return py_trees.common.Status.SUCCESS
        return py_trees.common.Status.FAILURE

# --- 2. Walking Script Manager ---
class WalkingProcess(py_trees.behaviour.Behaviour):
    def __init__(self, name="Centering Controller", script_path="./centering_controller.py"):
        super().__init__(name)
        self.script_path = script_path
        self.process = None

    def update(self):
        if self.process is None or self.process.poll() is not None:
            self.logger.info(f"Starting centering controller: {self.script_path}")
            self.process = subprocess.Popen(["python3", self.script_path], preexec_fn=os.setsid)
        return py_trees.common.Status.RUNNING

    def terminate(self, new_status):
        if self.process and self.process.poll() is None:
            self.logger.info("Killing centering controller for Jump sequence...")
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process.wait()
            self.process = None

# --- 3. Tree Construction ---
def create_tree(node):
    root = py_trees.composites.Selector(name="Root Selector", memory=False)

    # --- JUMP BRANCH ---
    # memory=True ensures we finish the delays once the jump is triggered
    jump_sequence = py_trees.composites.Sequence(name="Jump Branch", memory=True)
    
    lava_check = LavaSubscriber(threshold=40) # Ensure this matches your sensor units!
    
    # 5-second delay to ensure WalkingProcess.terminate() has finished
    pre_jump_delay = py_trees.timers.Timer("Pre-Jump Kill-Sync", duration=5.0)
    
    jump_request = Mode.Request()
    jump_request.mode = "FrontJump"
    call_jump = py_trees_ros.service.Client(
        name="FrontJump Service",
        service_type=Mode,
        service_name="/mode",
        node=node,
        request=jump_request
    )

    post_jump_delay = py_trees.timers.Timer("Post-Jump Stabilization", duration=3.0)

    # Sequence: 1. See Lava -> 2. Wait 5s (Walking dies) -> 3. Jump -> 4. Wait 3s
    jump_sequence.add_children([lava_check, pre_jump_delay, call_jump, post_jump_delay])

    # --- WALKING BRANCH ---
    walk_action = WalkingProcess(script_path="./centering_controller.py")

    root.add_children([jump_sequence, walk_action])
    return root

def main():
    rclpy.init()
    node = rclpy.create_node('go2_bt_logic')
    
    root = create_tree(node)
    bt = py_trees_ros.trees.BehaviourTree(root, unicode_tree_debug=True)
    bt.setup(timeout=15, node=node)
    
    # Tick at 10Hz
    bt.tick_tock(period_ms=100)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        bt.shutdown()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()