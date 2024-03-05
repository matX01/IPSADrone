from djitellopy import tello
import numpy as np


def StartBackend():
    pass







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

    