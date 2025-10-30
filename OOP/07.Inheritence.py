#Inhertance : When one class(child/derived) derives the properties & methods of another class(parent/base).
class Car:
    color = "black"
    
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

print(car1.name) # no error
print(car1.color)
print(car1.start())


# Single Inheritance............................................
# A child class inherits from only one parent class.
print("\nSingle Inheritance................")
class Parent:
    def show(self): # Self - Current instances of class .It is used to access variables and methods that belong to that specific object.
        print("Parent class method in Single Inheritance")

class Child(Parent):
    def display(self): # self - this particular object I’m working with right now."
        print("Child class method in Single Inheritance")

# Object of Child class
c = Child()
c.show()      # Inherited from Parent
c.display()   # Defined in Child


# Multiple Inheritance...............................................
# A child class inherits from more than one parent class.
print("\nMultiple Inheritance................")
class Mother:
    def mother_method(self):
        print("Mother class method in Multiple Inheritance")

class Father:
    def father_method(self):
        print("Father class method in Multiple Inheritance")

class Son(Mother, Father):  # Inherits from both
    pass # Pass is the keyword used to indicate an empty block of code in Python. It is often used as a placeholder when a statement is syntactically required but no action is needed.It means 'do nothing'

s = Son()
s.mother_method()
s.father_method()


# Multilevel inheritance.....................................
# A class inherits from another derived class, forming a chain.
print("\nMultilevel Inheritance................")
class Grandfather:
    def grand_father(self):
        print("Grandfather class method in Multilevel Inheritance")

class Father(Grandfather):
    def father_method(self):
        print("Father class method in Multilevel Inheritance")

class Son(Father):
    def son_method(self):
        print("Son class method in Multilevel Inheritance")

s = Son()
s.grand_father()
s.father_method()
s.son_method()


# Hierarchical Inheritance............................................
# Multiple child classes inherit from the same parent class.
print("\nHierarchical Inheritance................")
class Parent:
    def show(self):
        print("Parent class method in Hierarchical Inheritance")

class Child1(Parent):
    def child1_method(self):
        print("Child1 class method in Hierarchical Inheritance")

class Child2(Parent):
    def child2_method(self):
        print("Child2 class method in Hierarchical Inheritance")

c1 = Child1()
c2 = Child2()

c1.show()
c1.child1_method()

c2.show()
c2.child2_method()


# Hybrid Inheritance........................................................
# A combination of two or more types of inheritance.
# (like single + multiple + multilevel)
print("\nHybrid Inheritance................")
class School:
    def school_method(self):
        print("School class method in Hybrid Inheritance")

class Teacher(School):
    def teacher_method(self):
        print("Teacher class method in Hybrid Inheritance")

class Student(School):
    def student_method(self):
        print("Student class method in Hybrid Inheritance")

class Monitor(Teacher, Student):  # Multiple inheritance
    def monitor_method(self):
        print("Monitor class method")

m = Monitor()
m.school_method()
m.teacher_method()
m.student_method()
m.monitor_method()
