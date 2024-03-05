from djitellopy import tello
import numpy as np
import time

def StartBackend():
    pass


class IPSADronePathSimulator():

    pass




class TelloSim(tello.Tello):
    __Position = np.array([0,0,0])
    __ForwardVect = np.array([1,0,0])

    ## CONSTANTS

    __TAKEOFF_TIME = 5
    __TAKEOFF_ALTITUDE = 100

    __LAND_TIME = 3
    __TRANSLATE_COEF = 0.01
    __ROTATE_COEF = 1/90

    def __int__(self, Pos = np.array([0,0,0]), ForwardVector = np.array([1,0,0])):
        super().__init__()
        self.__Position = Pos
        self.__ForwardVect = ForwardVector


    def move_left(self, x: int):

        print("[SIM] Moving LEFT")
        time.sleep(self.__TRANSLATE_COEF * x)

        #TODO ALGEBRA

    def move_right(self, x: int):
        print("[SIM] Moving RIGHT")
        time.sleep(self.__TRANSLATE_COEF * x)

        #TODO ALGEBRA


    def move_back(self, x: int):
        print("[SIM] Moving BACK")
        time.sleep(self.__TRANSLATE_COEF * x)

        #TODO ALGEBRA


    def move_forward(self, x: int):
        print("[SIM] Moving FORWARD")
        time.sleep(self.__TRANSLATE_COEF * x)

        #TODO ALGEBRA


    def rotate_clockwise(self, x: int):
        print("[SIM] Rotating CW")
        time.sleep(self.__ROTATE_COEF * x)

        #TODO ALGEBRA


    def rotate_counter_clockwise(self, x: int):
        print("[SIM] Rotating CCW")
        time.sleep(self.__ROTATE_COEF * x)

        #TODO ALGEBRA


    def takeoff(self):
        print("[SIM] TAKEOFF")
        time.sleep(self.__TAKEOFF_TIME)

        self.__Position[2] = self.__TAKEOFF_ALTITUDE

        self.is_flying = True

    def land(self):
        print("[SIM] LAND")
        time.sleep(self.__LAND_TIME)

        self.__Position[2] = 0

        self.is_flying = False


class IPSADrone:

    __TelloDrone = None

    __CurrentPosition = np.array([0,0,0])

    __Available = False

    def IsAvailable(self) -> bool:
        
        return self.__Available

    def __init__(self,SIM = False) -> None:

        self.TelloDrone = tello.Tello()
        if(not SIM):
            try:
                self.TelloDrone.connect()
            except Exception:
        
                self.__Available = False
                return
        else:

            self.TelloDrone = TelloSim()


        self.__Available = True

    # === Décollage atterisssage === 

    def TakeOff(self) -> None:

        if(not self.IsAvailable()):
            return
        self.TelloDrone.takeoff()

    def Land(self) -> None:
        if(not self.IsAvailable()):
            return

        self.TelloDrone.land()

    def MoveLeft(self,Distance) -> None:
        if(not self.IsAvailable()):
            return

        self.TelloDrone.move_left(Distance)

    def MoveRight(self,Distance) -> None:
        if(not self.IsAvailable()):
            return

        self.TelloDrone.move_right(Distance)


    def MoveForward(self,Distance):
        if(not self.IsAvailable()):
            return

        self.TelloDrone.move_forward(Distance)

    def MoveBackward(self,Distance):
        if (not self.IsAvailable()):
            return

        self.TelloDrone.move_back(Distance)

    def RotateCW(self,Angle):
        if (not self.IsAvailable()):
            return

        self.TelloDrone.rotate_clockwise(Angle)

    def RotateCCW(self, Angle):
        if (not self.IsAvailable()):
            return

        self.TelloDrone.rotate_counter_clockwise(Angle)

    def EMERGENCY(self):
        if (not self.IsAvailable()):
            return

        self.TelloDrone.emergency()


    ##FIXME KEEPALIVE