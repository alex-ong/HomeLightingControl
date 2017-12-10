import HomeLightingControl

try:
    import tkinter as tk    
    from tkinter import colorchooser
except ImportError:
    import Tkinter as tk
    
HLC = HomeLightingControl.HomeLightingControl(HomeLightingControl.HOST)

class MainGUI(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupBrightness()
        self.setupColour()
        
    def setupBrightness(self):        
        #simple label
        tk.Label(self, text="brightness").pack()        
        #need to convert slider output to int
        command = lambda x: HLC.setBrightness(int(x)) 
        slider = tk.Scale(self, from_=100, to=0,command=command)
        slider.set(100)
        slider.pack()
    
    def setupColour(self):
        setColour = lambda x: HLC.setColourRGB(x[0][0],x[0][1],x[0][2])
        openColourChooser = lambda : setColour(colorchooser.askcolor(title="Pick a color"))
        tk.Button(self, text="choose color",command=openColourChooser).pack()
        
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Lighting Control")
    root.attributes("-toolwindow",1)
    gui = MainGUI(root)
    gui.pack()
    root.mainloop()