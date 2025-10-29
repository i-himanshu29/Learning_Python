# Abstraction : Hiding the complex implementation details and showing only the essential features of the object.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start_engine(self):
        self.acc = True
        self.clutch = True
        print("Engine started")

# Creating an object of the Car class
my_car = Car()
my_car.start_engine()  