from abc import ABC,abstractmethod
class Device(ABC):
    def __init__(self,name):
        self.name=name
        self.status=False
    
    def turn_on(self):
        self.status=True
    
    def turn_off(self):
        self.status=False
    
    # @abstractmethod
    def __str__(self):
        return f"Device name {self.name} with status {self.turn_on} or {self.turn_off}"

class Light(Device):
    # def __init__(self,name):
    #     super().__init__(name)
    #     self.status=False
    def __str__(self):
        return f"Device {self.name} - {'ON' if self.status else 'OFF'}"
class Fan(Device):
    def __str__(self):
        return f"Device {self.name} - {'ON' if self.status else 'OFF'}"

class AirConditioner(Device):
    def __str__(self):
        return f"Device {self.name} - {'ON' if self.status else 'OFF'}"

class SmartHome:
    def __init__(self):
        self.devices=[]
    
    def add_device(self,device):
        self.devices.append(device)
    
    def show_status(self):
        if self.devices:
            for device in self.devices:
                print('Device status: ',device.status)
        else:
            print('No device avilable in the device list')

if __name__=="__main__":
    home=SmartHome()
    # ----------------------------------------------------
    light = Device('Light')
    fan = Device('Fan')
    ac = Device('AirConditioner')
    # -----------------------------------------------------
    home.add_device(light)
    home.add_device(fan)
    home.add_device(ac)

    # --------------------------------------
    light.turn_on()
    ac.turn_on()
    home.show_status()



