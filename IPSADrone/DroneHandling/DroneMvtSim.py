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
        self.Position += self.ForwardVect * x
        self.HandleMovement()

    def MoveBackward(self, x: int) -> None:
        self.Position += self.ForwardVect * -x
        self.HandleMovement()

    def MoveLeft(self, x: int) -> None:
        UpVect = np.array([0, 0, 1])

        LeftVect = -np.cross(self.ForwardVect, UpVect)
        self.Position += LeftVect * x
        self.HandleMovement()

    def MoveRight(self, x: int) -> None:
        UpVect = np.array([0, 0, 1])

        RightVect = np.cross(self.ForwardVect, UpVect)
        self.Position += RightVect * x
        self.HandleMovement()

    def Rotate(self, angle: int) -> None:
        x_rad = angle * np.pi / 180

        RotateMat = np.array([[np.cos(x_rad), -np.sin(x_rad)], [np.sin(x_rad), np.cos(x_rad)]])

        self.ForwardVect[0:2] = (RotateMat @ self.ForwardVect[0:2].T)

    def RotateCW(self, angle: int) -> None:
        self.Rotate(-angle)

    def RotateCCW(self, angle: int) -> None:
        self.Rotate(angle)

    def PrintPos(self):
        print(str(self.Position) + " : " + str(self.ForwardVect))
