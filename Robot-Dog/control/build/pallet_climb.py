import time
from unitree_sdk2.go2.sport.sport_client import SportClient

class PalletAutoSwitch:
    def __init__(self):
        # Initialize the Sport Client
        self.client = SportClient()
        self.client.Init()
        
        # Detection Thresholds
        self.PALLET_HEIGHT = 0.12  # Meters
        self.PITCH_TOLERANCE = 0.08 # Radians (approx 4.5 degrees)
        self.WAIT_TIME = 5.0        # Seconds
        
        # State Control
        self.ground_z = 0.0
        self.state = "CALIBRATING"

    def get_state(self):
        """
        Fetches position and orientation from the robot state.
        In a real implementation, ensure your SDK2 environment 
        is correctly receiving 'sport_state' messages.
        """
        state = self.client.GetState()
        if state:
            return state.position[2], state.imu_state.rpy[1]
        return None, None

    def run(self):
        print("--- Go2 Pallet State Machine Started ---")
        
        while True:
            curr_z, curr_pitch = self.get_state()
            if curr_z is None:
                continue

            # STATE 1: CALIBRATE GROUND
            if self.state == "CALIBRATING":
                self.ground_z = curr_z
                print(f"Ground calibrated at: {self.ground_z:.3f}m")
                self.state = "MONITORING_CLIMB"

            # STATE 2: DETECT TOP OF PALLET
            elif self.state == "MONITORING_CLIMB":
                rel_height = curr_z - self.ground_z
                
                # Check if height is reached and body is level
                if rel_height > self.PALLET_HEIGHT and abs(curr_pitch) < self.PITCH_TOLERANCE:
                    print(f"Pallet detected! Height: {rel_height:.3f}m. Pitch: {curr_pitch:.3f}")
                    print(f"Waiting {self.WAIT_TIME} seconds before switching gaits...")
                    self.state = "WAITING"
                    self.start_timer = time.time()

            # STATE 3: DELAY
            elif self.state == "WAITING":
                elapsed = time.time() - self.start_timer
                if elapsed >= self.WAIT_TIME:
                    self.state = "SWITCH_GAIT"

            # STATE 4: COMMAND GAIT CHANGE
            elif self.state == "SWITCH_GAIT":
                print("Switching to Stair/Descending Gait (Gait Type 3)...")
                
                # GaitType 3 is the obstacle-clearing/stair mode
                self.client.GaitType(3)
                
                # Visual confirmation
                print("Gait Switch Complete. Ready for descent.")
                self.state = "FINISHED"
                break

            time.sleep(0.1)

if __name__ == "__main__":
    node = PalletAutoSwitch()
    node.run()