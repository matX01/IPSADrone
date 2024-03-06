import djitellopy as tello
import time
from .DroneMvtSim import DroneMovement
class TelloSim(tello.Tello):
    #__DroneMovementSim = DroneMovement()

    ## CONSTANTS

    __PromptPos = False

    __TAKEOFF_TIME = 5
    __TAKEOFF_ALTITUDE = 100
    __LAND_TIME = 3
    __TRANSLATE_COEF = 0.02
    __ROTATE_COEF = 1 / 90




    def __init__(self, PromptPos = False,FastMode = False):
        super().__init__()
        print("[SIM] Starting sim ...")

        self.__DroneMovementSim = DroneMovement()

        self.__PromptPos = PromptPos


        if (FastMode):
            self.__TAKEOFF_TIME = 0.1
            self.__LAND_TIME = 0.1
            self.__TRANSLATE_COEF = 0.0005
            self.__ROTATE_COEF = 1 / 900

    def connect(self, wait_for_state=True):
        pass

    def move_left(self, x: int):
        print("[SIM] Moving LEFT")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveLeft(x)

        if (self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def move_right(self, x: int):
        print("[SIM] Moving RIGHT")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveRight(x)

        if (self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def move_back(self, x: int):
        print("[SIM] Moving BACK")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveBackward(x)

        if (self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def move_forward(self, x: int):
        print("[SIM] Moving FORWARD")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveForward(x)

        if(self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def rotate_clockwise(self, x: int):
        print("[SIM] Rotating CW")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__ROTATE_COEF * x)

        self.__DroneMovementSim.RotateCW(x)

        if (self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def rotate_counter_clockwise(self, x: int):
        print("[SIM] Rotating CCW")

        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__ROTATE_COEF * x)

        self.__DroneMovementSim.RotateCCW(x)

        if (self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def takeoff(self):
        print("[SIM] TAKEOFF")
        time.sleep(self.__TAKEOFF_TIME)

        self.__DroneMovementSim.SetHeight(self.__TAKEOFF_ALTITUDE)

        self.is_flying = True
        if(self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

    def land(self):
        print("[SIM] LAND")
        time.sleep(self.__LAND_TIME)

        self.__DroneMovementSim.SetHeight(0)

        self.is_flying = False
        if(self.__PromptPos):
            self.__DroneMovementSim.PrintPos()

