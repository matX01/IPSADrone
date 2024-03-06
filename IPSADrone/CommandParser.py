from IPSADrone.DroneHandling.IPSATelloEngine import IPSADrone




class Command():
    __CommandName = ""

    def __init__(self, CommandName: str) -> None:
        self.__CommandName = CommandName

    def ConvertIntoText(self) -> str:
        return self.__CommandName

    def ExecuteCommand(self, Drone: IPSADrone):
        pass


class TakeOff_Command(Command):

    def __init__(self):
        super().__init__("Décoller()")

    def ExecuteCommand(self, Drone: IPSADrone):
        Drone.TakeOff()

class Land_Command(Command):

    def __init__(self):
        super().__init__("Atterir()")


    def ExecuteCommand(self, Drone: IPSADrone):

        Drone.Land()

class Translation_Command(Command):

    __Direction = ""
    __Distance = 0

    def __init__(self,Direction: str,Distance: int):

        super().__init__("Translation")

        self.__Direction = Direction

        if(self.__Direction != "GAUCHE" and self.__Direction != "DROITE" and self.__Direction != "ARRIERE" and self.__Direction != "AVANT"):
            print("INVALID COMMAND <<Direction>>")
            return
        self.__Distance = Distance

    def ConvertIntoText(self) -> str:

        return "Translation(\"{}\",{})".format(self.__Direction,self.__Distance)

    def ExecuteCommand(self, Drone: IPSADrone):

        match self.__Direction:
            case "GAUCHE":
                Drone.MoveLeft(self.__Distance)
            case "DROITE":
                Drone.MoveRight(self.__Distance)
            case "AVANT":
                Drone.MoveForward(self.__Distance)
            case "ARRIERE":
                Drone.MoveBackward(self.__Distance)

class Rotation_Command(Command):

    __Rotation = 1
    def __init__(self,Rotation):

        super().__init__("Rotation")
        if (Rotation < -360 or Rotation > 360 or Rotation == 0):
            print("INVALID COMMAND <<Rotation>>")
            return
        self.__Rotation = Rotation



    def ConvertIntoText(self) -> str:

        return "Rotation({})".format(self.__Rotation)

    def ExecuteCommand(self, Drone: IPSADrone):

        if(self.__Rotation < 0):
            Drone.RotateCW(self.__Rotation)
            return

        Drone.RotateCCW(self.__Rotation)

class DroneCommandSequencer():

    __CommandList = []
    def __init__(self):
        pass

    def AppendCommand(self,Comm: Command):

        self.__CommandList.append(Comm)
    def IsNextCommandAvailable(self) -> bool:

        return len(self.__CommandList) != 0

    def GetNextCommandName(self) -> str:

        return self.__CommandList[0].ConvertIntoText()


    def ExecuteNextCommand(self,Drone: IPSADrone):

        return self.__CommandList.pop(0).ExecuteCommand(Drone)

    def __str__(self) -> str:
        ReturnStr = ""
        for el in self.__CommandList:

            ReturnStr += el.ConvertIntoText() + "\n"

        return ReturnStr