# Vehicle Control System (Protocol for Interfaces)
# Requirement:
# Define a Vehicle protocol with methods start() and stop().
# Implement Car, Bike, and Truck classes.
# Create a TransportSystem class that works with any vehicle.


from typing import Protocol,List
class Vehicle(Protocol):
    def start(self):
        pass
    def stop(self):
        pass

class Car:
    def start(self):
        print('Car Started..')
    def stop(self):
        print('Car stopped..')

class Bike:
    def start(self):
        print('Bike start..')
    
    def stop(self):
        print('Bike stop')

class Truck:
    def start(self):
        print('Truck Started..')
    
    def stop(self):
        print('Truck stopped')

class Transportsystem:
    def __init__(self,vehicle:List[Vehicle]):
        self.vehile=vehicle
    
    def process(self):
        for transport in self.vehile:
            transport.start()
            transport.stop()


if __name__=='__main__':

    transport = Transportsystem([Car(),Bike(),Truck()])
    transport.process()
