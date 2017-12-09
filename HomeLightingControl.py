import milight
HOST = '192.168.1.104'
controller = milight.MiLight({'host': HOST, 'port': 8899}, wait_duration=0) #Create a controller with 0 wait between commands
light = milight.LightBulb(['rgbw', 'white', 'rgb']) #Can specify which types of bulbs to use
controller.send(light.on(1)) # Turn on group 1 lights
controller.send(light.all_on()) # Turn on all lights, equivalent to light.on(0)

class HomeLightingControl(object):
    def __init__(self, host):        
        self.controller = milight.MiLight({'host':host, 'port':8899}, wait_duration=0)
        self.group = milight.LightBulb(['rgbw'])
    def turnOn(self):
        self.controller.send(self.group.all_on())
    def turnOff(self):
        self.controller.send(self.group.all_off())
    
    #used when you want a HSL light
    #if our lightness is > 0.95, it'll use the white LED
    def setColour(self, hue, sat, light):
        message = self.group.color(milight.color_from_hls(hue, light, sat))
        self.controller.send(message)
    
    #takes an int from 0->100
    def setBrightness(self, brightness):
        message = self.group.brightness(brightness)
        self.controller.send(message)
    
if __name__ == '__main__':
    hlc = HomeLightingControl(HOST)
    hlc.turnOn()
    hlc.setColour(0.0,0.0,1.0)
    hlc.setBrightness(100)