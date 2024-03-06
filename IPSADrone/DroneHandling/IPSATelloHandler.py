from djitellopy import tello
import numpy as np
import time
from .DJITelloSim import TelloSim

from .DronePathSim import IPSADronePathSimulator

def StartBackend():
    pass





class IPSADrone:

    __TelloDrone = None

    __IsFlying = False

    __PathSim = IPSADronePathSimulator()

    __Available = False

    def IsAvailable(self) -> bool:
        
        return self.__Available

    def __init__(self,SIM = False) -> None:

        self.__PathSim.LoadFlightEnveloppe("FIXME")

        if(SIM):
            self.TelloDrone = TelloSim(False,True)

        else:
            self.TelloDrone = tello.Tello()

        try:
            self.TelloDrone.connect()
        except Exception:
        
            self.__Available = False
            return

        self.__Available = True

    # === Décollage atterisssage === 

    def TakeOff(self) -> None:

        if(not self.IsAvailable()):
            return
        self.TelloDrone.takeoff()
        self.__PathSim.SetHeight(100)   #FIXME Magic value
        self.__IsFlying = True

    def Land(self) -> None:
        if(not self.IsAvailable()):
            return

        self.TelloDrone.land()
        self.__PathSim.SetHeight(0)
        self.__IsFlying = False

    def MoveLeft(self,Distance: int) -> None:
        if(not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.move_left(Distance)
        self.__PathSim.MoveLeft(Distance)

    def MoveRight(self,Distance: int) -> None:
        if(not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.move_right(Distance)
        self.__PathSim.MoveRight(Distance)


    def MoveForward(self,Distance: int):
        if(not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.move_forward(Distance)

        self.__PathSim.MoveForward(Distance)

    def MoveBackward(self,Distance: int):
        if (not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.move_back(Distance)
        self.__PathSim.MoveBackward(Distance)

    def RotateCW(self,Angle: int):
        if (not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.rotate_clockwise(-Angle)
        self.__PathSim.RotateCW(Angle)

    def RotateCCW(self, Angle: int):
        if (not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")
            return

        self.TelloDrone.rotate_counter_clockwise(Angle)
        self.__PathSim.RotateCCW(Angle)

    def EMERGENCY(self):
        if (not self.IsAvailable()):
            return

        if (not self.__IsFlying):
            print("[TELLO] -WARN- Drone is not flying !")

        self.TelloDrone.emergency()

    def GetPathSim(self) -> IPSADronePathSimulator:

        return self.__PathSim

    ##FIXME KEEPALIVE