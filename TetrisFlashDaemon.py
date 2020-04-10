from Networking.TCPServer import CreateServer
import json
import time
from threading import Thread
from HomeLightingControl import HomeLightingControl, HOST

RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
COOL_BLUE = (128,128,255)
MAGENTA = (255, 0, 128)
YELLOW = (255,255,0)
PURPLE = (255,0,255)
WHITE = (255, 255, 255)

LEVEL_DATA = { 
               18: WHITE,
               19: RED,
               20: COOL_BLUE,
               21: GREEN,
               22: PURPLE,
               23: GREEN,
               24: MAGENTA,
               25: BLUE,
               26: RED,
               27: BLUE,
               28: PURPLE,
               29: RED,
               None: WHITE
             }

def setColor(api, level):
    if level is not None:
        level = int(level)
        if (level < 18 or level >= 30):
            level = (level % 10) + 20    
    api.setColourRGB_tuple(LEVEL_DATA[level])
    
def flash(api, callback):
    print('flashthread')
    for i in range(3):
        api.setColourRGB_tuple(RED)
        time.sleep(0.003)
        api.setColourRGB_tuple(GREEN)
        time.sleep(0.003)
        api.setColourRGB_tuple(BLUE)
        time.sleep(0.003)
    callback()
     
FLASH_TIME = 1.0

class FlashDaemon(object):
    def __init__(self, api):
        self.api = api
        self.isFlashing = False
        self.currentLevel = 0
        
    def stopFlash(self):
        self.isFlashing = False
        setColor(self.api,self.currentLevel)
        
    def handleMessage(self, message):
        data = message.decode('utf8')
        data = json.loads(data)
        time_stamp = time.time()
        
        self.checkFlash(data)        
        if not self.isFlashing:
            self.updateLevel(data['level'])
    
    def updateLevel(self, newLevel):
        if self.currentLevel != newLevel:
            self.currentLevel = newLevel
            setColor(self.api, newLevel)
            
    def checkFlash(self, data):
        if not self.isFlashing:            
            if data['flash']:
                self.isFlashing = True
                worker = Thread(target=flash, args=(self.api,self.stopFlash))
                worker.setDaemon(True)                                  
                worker.start()                
        

    
    
if __name__ == '__main__':
    hlc = HomeLightingControl(HOST)
    hlc.turnOn()
    fd = FlashDaemon(hlc)
    server = CreateServer('localhost', 3339, fd.handleMessage)    
    while True:
        pass