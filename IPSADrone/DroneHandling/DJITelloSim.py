import djitellopy as tello
import time
from .DroneMvtSim import DroneMovement
class TelloSim(tello.Tello):
    __DroneMovementSim = DroneMovement()

    ## CONSTANTS

    __FASTMODE = True

    __TAKEOFF_TIME = 5
    __TAKEOFF_ALTITUDE = 100
    __LAND_TIME = 3
    __TRANSLATE_COEF = 0.02
    __ROTATE_COEF = 1 / 90

    def __int__(self):

        super().__init__()

        if (self.__FASTMODE):

            self.__TAKEOFF_TIME = 0.1
            self.__LAND_TIME = 0.1
            self.__TRANSLATE_COEF = 0.0005
            self.__ROTATE_COEF = 1 / 900

    def move_left(self, x: int):
        print("[SIM] Moving LEFT")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveLeft(x)

        self.__DroneMovementSim.PrintPos()

    def move_right(self, x: int):
        print("[SIM] Moving RIGHT")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveRight(x)

        self.__DroneMovementSim.PrintPos()

    def move_back(self, x: int):
        print("[SIM] Moving BACK")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveBackward(x)

        self.__DroneMovementSim.PrintPos()

    def move_forward(self, x: int):
        print("[SIM] Moving FORWARD")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return

        time.sleep(self.__TRANSLATE_COEF * x)

        self.__DroneMovementSim.MoveForward(x)

        self.__DroneMovementSim.PrintPos()

    def rotate_clockwise(self, x: int):
        print("[SIM] Rotating CW")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__ROTATE_COEF * x)

        self.__DroneMovementSim.RotateCW(x)

        self.__DroneMovementSim.PrintPos()

    def rotate_counter_clockwise(self, x: int):
        print("[SIM] Rotating CCW")
        if(not self.is_flying):
            print("[SIM] -WARN- Drone is not flying")
            return
        time.sleep(self.__ROTATE_COEF * x)

        self.__DroneMovementSim.RotateCCW(x)

        self.__DroneMovementSim.PrintPos()

    def takeoff(self):
        print("[SIM] TAKEOFF")
        time.sleep(self.__TAKEOFF_TIME)

        self.__DroneMovementSim.SetHeight(self.__TAKEOFF_ALTITUDE)

        self.is_flying = True

    def land(self):
        print("[SIM] LAND")
        time.sleep(self.__LAND_TIME)

        self.__DroneMovementSim.SetHeight(0)

        self.is_flying = False

