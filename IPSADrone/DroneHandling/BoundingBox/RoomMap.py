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
    def IsPointInBox(self,Point: np.ndarray) -> bool:

        return (Point[0] > self.BottomLeft[0] and
                Point[1] > self.BottomLeft[1] and
                Point[0] < self.TopRight[0] and
                Point[1] < self.TopRight[1])

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
        self.__Size = np.array([500,500])

        self.__LaunchPad = LaunchPadZone(np.array([245,245]),np.array([255,255]))
        self.__LandPad = LandPadZone(np.array([100, 100]), np.array([200, 200]))

        self.__ExclusionZones.append(ExclusionZone(np.array([0,0]),np.array([50,500])))
        self.__ExclusionZones.append(ExclusionZone(np.array([0, 0]), np.array([500, 50])))
        self.__ExclusionZones.append(ExclusionZone(np.array([450,0]), np.array([500,500])))
        self.__ExclusionZones.append(ExclusionZone(np.array([0,450]), np.array([500,500])))

        self.__GenerateImage()

    def LoadMapWithXML(self,XMLPath: str) -> None:
        #FIXME Not implemented
        pass

    def __GenerateImage(self):
        self.__Image = 255 * np.ones((self.__Size[0],self.__Size[1], 3))

        self.__LaunchPad.DrawBox(self.__Image)
        self.__LandPad.DrawBox(self.__Image)
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