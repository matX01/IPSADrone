from .IPSATelloEngine import IPSADrone
from .IPSATelloInterface import IPSATelloInterface
from .CommandParser import DroneCommandParser
from .CommandParser import Command
from .CommandParser import TakeOff_Command
from .CommandParser import Land_Command
from .CommandParser import Translation_Command

__Interface = IPSATelloInterface()
__Drone = IPSADrone(True)
__CommParser = DroneCommandParser()

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
    pass


def Change_Altitude(valeur: int) -> None:
    print("NOT IMPLEMENTED")


def DroneMovementSequence(fcn) -> None:
    fcn()
    PromptParsedCommands()

    __Interface.MainLoop()

    pass

def PromptParsedCommands() -> None:

    print(__CommParser)