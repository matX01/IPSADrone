from .IPSATelloEngine import IPSADrone
from .IPSATelloInterface import IPSATelloInterface

__Interface = IPSATelloInterface()
__Drone = IPSADrone(True)


def Decoller() -> None:
    __Drone.TakeOff()


def Atterir() -> None:
    __Drone.TakeOff()


def Translation(direction, distance: int) -> None:
    pass


def Rotation(angle: int) -> None:
    pass


def Change_Altitude(valeur: int) -> None:
    pass


def DroneMovementSequence(fcn) -> None:


    __Interface.MainLoop()

    pass
