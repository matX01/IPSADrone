from djitellopy import tello
import numpy as np


def StartBackend():
    pass


class IPSADronePathSimulator():






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

    ##FIXME KEEPALIVE