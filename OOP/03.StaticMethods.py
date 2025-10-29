# Method that do not use self parameter(work at class level) are called static methods.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def hello():
        print("Hello Student!")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of", self.name, "is", sum / len(self.marks))
    
student1 = Student("Alice", [85, 90, 95])
student1.get_avg()
# student1.hello() #Error
# Note :  This will raise an error because hello() does not take self parameter hence we can make it a static method.


# Solution - Decorator
# Decorators : allows us to modify the behavior of a function or method without changing its actual code.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello Student!")
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of", self.name, "is", sum / len(self.marks))
    
student1 = Student("Alice", [85, 90, 95])
student1.get_avg()
student1.hello()  # Now this will work fine.