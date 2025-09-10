# Question 1: Smart Home Automation System
# Requirements:
# Create an abstract base class Device (with turn_on(), turn_off() as abstract methods).
# Create subclasses:
# Light (extra: brightness control)
# Fan (extra: speed control)
# AC (extra: temperature control)
# Use encapsulation for private attributes (like _status).
# Create a nested class Schedule inside Device, which stores on/off timings.
# Demonstrate by creating multiple devices, setting schedules, and turning them on/off dynamically.
import datetime
from abc import ABC, abstractmethod
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    class Schedule:
        def on_timing(self):
            return f"On Timing for device - {datetime.datetime.now()}"
    
        def off_timing(self):
            return f"Off Timing for debice- {datetime.datetime.now()}"

class Light(Device):
    def __init__(self):
        self.__status=False
    
    def turn_on(self):
        print (f"{self.__class__.__name__} has been turn on successfully..")
        self.__status=True

    def turn_off(self):
        print(f"{self.__class__.__name__} has been turn off successfully..")
        self.__status = False
    
    def birghtness_controll(self):
        return 'Brigtness controlled successfully..'

class Fan(Device):
    def __init__(self):
        self.__status=False
    
    def turn_on(self):
        print(f"{self.__class__.__name__} has been turn on successfully..")
        self.__status =True
    
    def turn_off(self):
        print(f"{self.__class__.__name__} has been turn off successfully..")
        self.__status=False
    
    def speed_control(self):
        return f"speed controlled successfully.."

class Ac(Device):
    def __init__(self):
        self.__status=False
    
    def turn_on(self):
        print(f"{self.__class__.__name__} has been turn on successfully..")
        self.__staus=True
    
    def turn_off(self):
        print(f"{self.__class__.__name__} has been turn off successfully..")
        self.__status=False
    
    def temp_controll(self):
        return f"Temprature controlled successfully.."

if __name__=="__main__":
    device = [Light(),Fan(),Ac()]
    for i in device:
        i.turn_on()
        subclass = i.Schedule()
        print(subclass.on_timing())


    