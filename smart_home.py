import datetime 
from abc import ABC,abstractmethod
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class Light(Device):

    def turn_on(self):
        return 'Light on'
    
    def turn_off(self):
        return 'Light off'


class Fan(Device):

    def turn_on(self):
        return "Fan on"
    
    def turn_off(self):
        return 'Fan off'

class Ac(Device):
    def turn_on(self):
        return 'AC on'
    
    def turn_off(self):
        return 'AC off'

class Controller:
    def __init__(self):
        self.devices= []
    
    def add_device(self,device):
        if device in self.devices:
            print(f"{device.__class__.__name__} has already exist..")
        self.devices.append(device)
        print(f"{device.__class__.__name__} has been added successfully..")

if __name__=="__main__":
    ac=Ac()
    fan=Fan()
    light =Light()
    system = Controller()
    system.add_device(light)
    system.add_device(fan)
    system.add_device(ac)
    for sys in system.devices:
        print(sys.turn_on())


    
