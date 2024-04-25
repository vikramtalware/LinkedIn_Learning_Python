#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class vehicle():
    def __init__(self, bodystyle): # this gets called when a class is constructed and initialized
        self.bodystyle = bodystyle
    def drive(self, speed):
        self.speed = speed
        self.mode = "Driving"

class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print(self.mode, "my", self.enginetype, "car at", self.speed)

class motorcycle(vehicle):
    def __init__(self, enginetype, hasasidecar):
        super().__init__("Motorcycle")
        if hasasidecar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print(self.mode, "my", self.enginetype, "motorcycle at", self.speed)    

car1 = car("Gas")
car2 = car("Electric")
mc1 = motorcycle("Gas", True)
mc2 = motorcycle("Electric", False)

print(mc1.wheels)
print(mc2.doors)
print(car1.doors)
print(car2.enginetype)

car1.drive(30)
car2.drive(40)
mc2.drive(50)