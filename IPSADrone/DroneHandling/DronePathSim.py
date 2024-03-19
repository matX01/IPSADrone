import numpy as np
from .DroneMvtSim import DroneMovement
from .BoundingBox.RoomMap import RoomMap
import cv2
class IPSADronePathSimulator(DroneMovement):
    __MovementSequence = []

    __FlightEnvelope = RoomMap()

    __ImageAvailable = False

    __MovementAllowed = True

    def __init__(self):

        super().__init__()

    def LoadFlightEnveloppe(self,Path: str):

        self.__FlightEnvelope.LoadTestMap()
        LaunchPadCenter = self.__FlightEnvelope.GetLaunchPadCenter()


        self.SetPos(np.array([LaunchPadCenter[0],LaunchPadCenter[1],0.0]))
        self.__MovementSequence.append(self.Position.copy())

        self.SetForwardVect(np.array([0.0,1.0,0.0])) #FIXME Test only


    def IsMovementAllowed(self, CurrentPosition: np.ndarray, PositionToTry: np.ndarray):

        return (self.__FlightEnvelope.IsMovementAllowed(CurrentPosition,PositionToTry))


    def HandleMovement(self):

        self.__MovementSequence.append(self.Position.copy())

        self.__ActualiseImage()

    def __str__(self) -> str:

        return str(self.__MovementSequence)


    def __ActualiseImage(self):

        self.__Image = self.__FlightEnvelope.GetImageCopy()

        for i in range(len(self.__MovementSequence)-1,0,-1):

            cv2.line(self.__Image,
                     np.array([int(self.__MovementSequence[i][0]),
                               int(np.shape(self.__Image)[1] - self.__MovementSequence[i][1])]),
                     np.array([int(self.__MovementSequence[i-1][0]),
                               int(np.shape(self.__Image)[1] - self.__MovementSequence[i-1][1])]),
                     (0,0,0),
                     2)

        self.__ImageAvailable = True

    def GetImage(self):

        self.__ImageAvailable = False
        return self.__Image

    def ShowImage(self):
        if(not self.__ImageAvailable):
            return
        cv2.imshow("YAAA",self.__Image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

