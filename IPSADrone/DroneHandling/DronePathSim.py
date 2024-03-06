import numpy as np
from .DroneMvtSim import DroneMovement
from .BoundingBox.RoomMap import RoomMap
import cv2
class IPSADronePathSimulator(DroneMovement):
    __MovementSequence = []

    __FlightEnvelope = RoomMap()

    __ImageAvailable = False

    def __init__(self):

        super().__init__()

    def LoadFlightEnveloppe(self,Path: str):

        self.__FlightEnvelope.LoadTestMap()
        LaunchPadCenter = self.__FlightEnvelope.GetLaunchPadCenter()


        self.SetPos(np.array([LaunchPadCenter[0],LaunchPadCenter[1],0.0]))
        self.__MovementSequence.append(self.Position.copy())

        self.SetForwardVect(np.array([0.0,1.0,0.0])) #FIXME Test only



    def HandleMovement(self):

        self.__MovementSequence.append(self.Position.copy())


    def __str__(self) -> str:

        return str(self.__MovementSequence)


    def __ActualiseImage(self):

        self.__Image = self.__FlightEnvelope.GetImageCopy()

        for i in range(len(self.__MovementSequence)-1,0,-1):

            cv2.line(self.__Image,self.__MovementSequence[i][0:2].astype(np.int32),self.__MovementSequence[i-1][0:2].astype(np.int32),(0,0,0),2)

        self.__ImageAvailable = True

    def GetImage(self):

        self.__ImageAvailable = False
        return self.__Image

    def ShowImage(self):

        cv2.imshow("YAAA",self.__Image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

