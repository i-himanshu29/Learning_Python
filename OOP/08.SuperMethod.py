# Super method :
# super() method is used to access methods of the parent class.

class Car:
    
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name) 
print(car1.type) # give error



# Note - Now solve by super 


class Car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)
        
car1 = ToyotaCar("fortuner","electric")
print(car1.type) 