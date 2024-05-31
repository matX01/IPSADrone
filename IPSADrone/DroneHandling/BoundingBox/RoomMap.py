import numpy as np
import cv2
import xmltodict
import xmltodict as xml


class BoundingBox:

    def __init__(self,BottomLeft: np.ndarray,TopRight: np.ndarray,Color: tuple) -> None:
        self.BottomLeft = BottomLeft
        self.TopRight = TopRight
        self.__color = Color
    """def __init__(self,XmlToParse: dict,Color: np.ndarray) -> None:

        self.BottomLeft = None
        self.TopRight = None
        self.__color = Color"""

    def __Parse(self,XMLToParse: dict) -> None:

        #XMLToParse.get()

        pass

    def __str__(self) -> str:

        return str(self.BottomLeft) + " : " + str(self.TopRight)
    def TestLine(self,Point1: np.ndarray,Point2: np.ndarray,Point3: np.ndarray,Point4: np.ndarray) -> bool:

        if(np.linalg.norm(np.cross((Point2 - Point1),(Point4 - Point3))) == 0):
            return False


        uA = (((Point4[0] - Point3[0]) *
              (Point1[1] - Point3[1]) -
               (Point4[1] - Point3[1]) *
               (Point1[0] - Point3[0])) /
              ((Point4[1] - Point3[1]) *
               (Point2[0] - Point1[0]) -
               (Point4[0] - Point3[0]) *
               (Point2[1] - Point1[1])))

        uB = (((Point2[0] - Point1[0]) *
               (Point1[1] - Point3[1]) -
               (Point2[1] - Point1[1]) *
               (Point1[0] - Point3[0]))/
              ((Point4[1] - Point3[1]) *
               (Point2[0] - Point1[0]) -
               (Point4[0] - Point3[0]) *
               (Point2[1] - Point1[1])))

        return uA >= 0.0 and uA <= 1.0 and uB >= 0.0 and uB <= 1.0

    def IsLineIntersectBox(self,Point1: np.ndarray, Point2: np.ndarray) -> bool:

        Line1A = np.array([self.BottomLeft[0],self.BottomLeft[1]])
        Line1B = np.array([self.TopRight[0],self.BottomLeft[1]])

        Line2A = Line1A
        Line2B = np.array([self.BottomLeft[0],self.TopRight[1]])

        Line3A = self.TopRight
        Line3B = Line2B

        Line4A = Line1B
        Line4B = Line3A


        if(self.TestLine(Line1A,Line1B,Point1,Point2)):
            return True
        if(self.TestLine(Line2A,Line2B,Point1,Point2)):
            return True
        if(self.TestLine(Line3A,Line3B,Point1,Point2)):
            return True
        if(self.TestLine(Line4A,Line4B,Point1,Point2)):
            return True
        return False




    def GetCenter(self) -> np.ndarray:

        return np.array([(self.BottomLeft[0] + self.TopRight[0])/2,(self.BottomLeft[1] + self.TopRight[1])/2])

    def DrawBox(self,Image: np.ndarray) -> None:

        cv2.rectangle(Image,
                      np.array([self.BottomLeft[0],np.shape(Image)[1] - self.BottomLeft[1]]),
                      np.array([self.TopRight[0],np.shape(Image)[1] - self.TopRight[1]]),
                      self.__color,-1)


class ExclusionZone(BoundingBox):
    def __init__(self,BottomLeft: np.ndarray,TopRight: np.ndarray):

        super().__init__(BottomLeft,TopRight,(0,0,255))
    """def __init__(self,XMLToParse: dict):

        super().__init__(XMLToParse,np.array([255,0,0]))"""

class LaunchPadZone(BoundingBox):
    def __init__(self,BottomLeft: np.ndarray,TopRight: np.ndarray):

        super().__init__(BottomLeft, TopRight,(255, 255, 0))


class LandPadZone(BoundingBox):
    def __init__(self, BottomLeft: np.ndarray, TopRight: np.ndarray):

        super().__init__(BottomLeft, TopRight,(0, 255, 255))


class RoomMap():
    def __init__(self):

        self.__ExclusionZones = []
        self.__LaunchPad = None
        self.__LandPad = None
        self.__Size = np.array([0,0])
        self.__Image = None

    def LoadTestMap(self) -> None:
        pass

        #FIXME FOR TEST ONLY
        self.__Size = np.array([270,270])

        self.__LaunchPad = LaunchPadZone(np.array([30,30]),np.array([40,40]))
        self.__LandPad = LandPadZone(np.array([100, 100]), np.array([200, 200]))


        self.__ExclusionZones.append(ExclusionZone(np.array([0,0]),np.array([20,270])))
        self.__ExclusionZones.append(ExclusionZone(np.array([0, 0]), np.array([270, 20])))
        self.__ExclusionZones.append(ExclusionZone(np.array([250,0]), np.array([270,270])))
        self.__ExclusionZones.append(ExclusionZone(np.array([0,250]), np.array([270,270])))
        #self.__ExclusionZones.append(ExclusionZone(np.array([300, 300]), np.array([320, 320])))
        self.__GenerateImage()

    def LoadMapWithXML(self,XMLPath: str) -> None:
        #FIXME Not implemented
        pass

    def __GenerateImage(self):
        self.__Image = 255 * np.ones((self.__Size[0],self.__Size[1], 3))

        self.__LaunchPad.DrawBox(self.__Image)
        #self.__LandPad.DrawBox(self.__Image)
        for el in self.__ExclusionZones:

            el.DrawBox(self.__Image)

    def GetImageCopy(self):

        return self.__Image.copy()

    def DisplayImage(self):

        cv2.imshow("Map", self.__Image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def GetLaunchPadCenter(self) -> np.ndarray:

        return self.__LaunchPad.GetCenter()

    def IsMovementAllowed(self,CurrentPosition: np.ndarray,PositionToTry: np.ndarray) -> bool:

        if(PositionToTry[0] < 0 or PositionToTry[1] < 0 or PositionToTry[0] > self.__Size[0] or PositionToTry[1] > self.__Size[1]):
            return False

        for el in self.__ExclusionZones:

            if(el.IsLineIntersectBox(CurrentPosition[0:2],PositionToTry[0:2])):
                print(el)
                return False

        return True
