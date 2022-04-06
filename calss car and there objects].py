# A python program to create a car abstarct class that contains an instance variable, a concrete method and two abstact methods.
# Class Car have registration number , fuel tank, steering and brakes,where fuel tank is a concrete method  and steering and brakes are abstract method.
from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,RegNo):
        self.RegNo = RegNo
    def Fuel_tank(self):
        print("Fill the fuel into the tank .")
        print("For car with the registration number ", self.RegNo)

    @abstractmethod
    def steering(self):
        pass
    def braking(self):
        pass

# Now creating class maruti with base class Car
class Maruti(Car): 
    def steering(self):
        print("Maruti uses manual steering")
        print("Drive the car.")
    def braking(self):
        print("Maruti uses huydraulic breaks,")
        print("Apply and stop it.")

m = Maruti(100)
m.Fuel_tank()
m.steering()
m.braking()