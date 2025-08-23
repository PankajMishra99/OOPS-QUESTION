from typing import Protocol,List
class SmartDevice(Protocol):
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class Light:
    def turn_on(self):
        print('Light on')
    
    def turn_off(self):
        print('Light off')

class Fan:
    def turn_on(self):
        print('Fan on')
    def turn_off(self):
        print('Fan of')


class AC:
    def turn_on(self):
        print('AC on')
    
    def turn_off(self):
        print('AC of')

class Homeautomation:
    def __init__(self,device:List[SmartDevice]):
        self.device=device


    def process(self):
        for dev in self.device:
            dev.turn_on()
            dev.turn_off()
if __name__=="__main__":
    system=Homeautomation([Light(),Fan(),AC()])
    system.process()