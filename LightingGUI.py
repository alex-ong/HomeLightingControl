import HomeLightingControl
import tkinter as tk
HLC = HomeLightingControl.HomeLightingControl(HomeLightingControl.HOST)

class MainGUI(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupBrightness()
    
    def setupBrightness(self):        
        #simple label
        tk.Label(self, text="brightness").pack()        
        #need to convert slider output to int
        command = lambda x: HLC.setBrightness(int(x)) 
        slider = tk.Scale(self, from_=100, to=0,command=command)
        slider.set(100)
        slider.pack()
        
    
if __name__ == '__main__':
    root = tk.Tk()
    gui = MainGUI(root)
    gui.pack()
    root.mainloop()