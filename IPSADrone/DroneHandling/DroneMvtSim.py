import numpy as np

class DroneMovement():
    __Position = np.array([0.0, 0.0, 0.0])
    __ForwardVect = np.array([1.0, 0.0, 0.0])
    __Variance = np.array([0, 0, 0])    #TODO Implement Variance

    def __int__(self):
        pass

    def SetHeight(self,x: int) -> None:

        self.__Position[2] = x
    def MoveForward(self, x: int) -> None:
        self.__Position += self.__ForwardVect * x

    def MoveBackward(self, x: int) -> None:
        self.__Position += self.__ForwardVect * -x

    def MoveLeft(self, x: int) -> None:
        UpVect = np.array([0, 0, 1])

        LeftVect = -np.cross(self.__ForwardVect, UpVect)
        self.__Position += LeftVect * x

    def MoveRight(self, x: int) -> None:
        UpVect = np.array([0, 0, 1])

        RightVect = np.cross(self.__ForwardVect, UpVect)
        self.__Position += RightVect * x

    def Rotate(self, angle: int) -> None:
        x_rad = angle * np.pi / 180

        RotateMat = np.array([[np.cos(x_rad), -np.sin(x_rad)], [np.sin(x_rad), np.cos(x_rad)]])

        self.__ForwardVect[0:2] = (RotateMat @ self.__ForwardVect[0:2].T)

    def RotateCW(self, angle: int) -> None:
        self.Rotate(-angle)

    def RotateCCW(self, angle: int) -> None:
        self.Rotate(angle)

    def PrintPos(self):
        print(str(self.__Position) + " : " + str(self.__ForwardVect))
