import tkinter as tk


class _IPSATelloFrame(tk.LabelFrame):
    
    framePos = []
    frameSide = ""

    def __init__(self,MainWindow: tk.Tk,FrameName: str, framePos: list, frameSide = tk.LEFT):
    
        self.framePos = framePos
        self.frameSide = frameSide

        super().__init__(MainWindow,text=FrameName,borderwidth=2,relief=tk.GROOVE)

    def Pack(self):
        
        self.pack(padx= self.framePos[0], pady = self.framePos[1], side= self.frameSide)

class _PosFrame(_IPSATelloFrame):

    def __init__(self,MainWindow: tk.Tk):
        

        super().__init__(MainWindow,"Position",[10,10])



class _Menu():
    FrameList = []

    def __init__(self):
        pass

    def PushFrame(self,Fr: _IPSATelloFrame) -> None:

        self.FrameList.append(Fr)

    def DisplayMenu(self) -> None:

        for el in self.FrameList:
            
            el.Pack()



class IPSATelloInterface():

    window = None

    Menu = []

    def __init__(self) -> None:
        
        self.window = tk.Tk()
        self.window.title("IPSA Tello controller")
        self.window.geometry("400x400")

        Men = _Menu()

        PosFrm = _PosFrame(self.window)

        Men.PushFrame(PosFrm)

        Men.DisplayMenu()

    
    def UpdateLoop(self) -> None:
        pass



    def MainLoop(self) -> None:

        self.window.mainloop()


