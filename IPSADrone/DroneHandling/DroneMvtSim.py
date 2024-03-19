import numpy as np

class DroneMovement():



    def __init__(self):
        self.Position = np.array([0.0, 0.0, 0.0])
        self.ForwardVect = np.array([1.0, 0.0, 0.0])
        self.Variance = np.array([0.0, 0.0, 0.0])

    def SetPos(self,NewPos: np.ndarray):

        self.Position = NewPos

    def SetForwardVect(self,NewForwardVect: np.ndarray):

        self.ForwardVect = NewForwardVect

    def HandleMovement(self):

        pass

    def SetHeight(self, x: int) -> None:
        self.Position[2] = x
        self.HandleMovement()
    def MoveForward(self, x: int) -> None:
        self.Position = self.CalculateMoveForward(x)
        self.HandleMovement()

    def CalculateMoveForward(self,x: int) -> np.ndarray:
        return self.Position + self.ForwardVect * x


    def MoveBackward(self, x: int) -> None:
        self.Position = self.CalculateMoveBackward(x)
        self.HandleMovement()
    def CalculateMoveBackward(self,x: int) -> np.ndarray:
        return self.Position + self.ForwardVect * -x


    def MoveLeft(self, x: int) -> None:
        self.Position = self.CalculateMoveLeft(x)
        self.HandleMovement()

    def CalculateMoveLeft(self,x: int) -> np.ndarray:
        UpVect = np.array([0, 0, 1])
        LeftVect = -np.cross(self.ForwardVect, UpVect)
        return self.Position + LeftVect * x

    def MoveRight(self, x: int) -> None:
        self.Position = self.CalculateMoveRight(x)
        self.HandleMovement()

    def CalculateMoveRight(self,x: int) -> np.ndarray:
        UpVect = np.array([0, 0, 1])
        RightVect = np.cross(self.ForwardVect, UpVect)
        return self.Position + RightVect * x

    def Rotate(self, angle: int) -> None:
        x_rad = angle * np.pi / 180

        RotateMat = np.array([[np.cos(x_rad), -np.sin(x_rad)], [np.sin(x_rad), np.cos(x_rad)]])

        self.ForwardVect[0:2] = (RotateMat @ self.ForwardVect[0:2].T)

    def RotateCW(self, angle: int) -> None:
        self.Rotate(angle)

    def RotateCCW(self, angle: int) -> None:
        self.Rotate(angle)

    def PrintPos(self):
        print(str(self.Position) + " : " + str(self.ForwardVect))
