from .DroneHandling.IPSATelloHandler import IPSADrone
from .UI.IPSATelloInterface import IPSATelloInterface
from .CommandParser import DroneCommandSequencer
from .CommandParser import Command
from .CommandParser import TakeOff_Command
from .CommandParser import Land_Command
from .CommandParser import Translation_Command
from .CommandParser import Rotation_Command
from .DroneHandling.DronePathSim import IPSADronePathSimulator

__Interface = IPSATelloInterface()
__Drone = IPSADrone(True)
__CommParser = DroneCommandSequencer()

def Decoller() -> None:

    Command = TakeOff_Command()

    __CommParser.AppendCommand(Command)


def Atterir() -> None:

    Command = Land_Command()

    __CommParser.AppendCommand(Command)


def Translation(direction, distance: int) -> None:

    Command = Translation_Command(direction,distance)

    __CommParser.AppendCommand(Command)


def Rotation(angle: int) -> None:
    Command = Rotation_Command(angle)

    __CommParser.AppendCommand(Command)


def Change_Altitude(valeur: int) -> None:
    print("NOT IMPLEMENTED")


def DroneMovementSequence(fcn) -> None:
    fcn()

    __PathSim = __Drone.GetPathSim()

    while(__CommParser.IsNextCommandAvailable()):

        print(__CommParser.GetNextCommandName())

        __CommParser.ExecuteNextCommand(__Drone)


    __PathSim.ShowImage()
    __Interface.MainLoop()



def PromptParsedCommands() -> None:

    print(__CommParser)