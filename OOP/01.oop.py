# OOP : object-oriented programming is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.
# It is used to structure code in a way that is modular, reusable, and easier to maintain.
# Real Word Scenario : In a real-world scenario, OOP can be used to model complex systems by breaking them down into smaller, more manageable objects. 

# Procedural programming : 
# Procedural programming is a programming paradigm that uses procedures or routines to perform tasks. 
# It is based on the concept of procedure calls, where a program is divided into smaller, reusable functions that can be called as needed.
# It is used to structure code in a linear, step-by-step manner.

# Functional programming :
# Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions.
# It emphasizes the use of pure functions, immutability, and higher-order functions.
# reuseablity increases and redundency decreases.

# Object Oriented Programming (OOP) is a programming paradigm that uses "objects" to represent data and methods to manipulate that data.
# reusability increases and redundency decreases.
# It is used to structure code in a way that is modular, reusable, and easier to maintain.

# Class : 
# A class is a blueprint for creating objects. 
# It defines the properties and behaviors of the objects that will be created from it.

class Student:
    name = "Himanshu"  # Attribute/Property
    
# Object : 
# An object is an instance of a class.

student1 = Student()  # Creating an object of the Student class
print(student1)  # Printing the object
print(student1.name)  # Accessing the attribute of the object

class Car:
    color = "Red"  # Attribute/Property
    model = "Toyota"
    
car1 = Car()  # Creating an object of the Car class
print(car1.color) 
print(car1.model) 


# Constructor :
# A constructor is a special method that is called when an object is created.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# self Parameter : It is a reference to the current instance of the class. 
# It is used to access variables and methods that belong to that specific object.


class Person:
    def __init__(self, name, age):  # Constructor with parameters
        print("Constructor called")  # Message to indicate constructor is called
        print(self)
        self.name = name  # Initializing attributes
        self.age = age
        
person1 = Person("Alice", 30)  
print(person1)
print(person1.name) #Alice

person2 = Person("Bob", 25)
print(person2.name) #Bob
print(person2.name , person2.age) 


# Additional Constructor


class Person:
    # Default Constructor
    def __init__(self):
        print("Default Constructor called")
        
    # Parameterized Constructor
    def __init__(self, name, age):  # Constructor with parameters
        print("Constructor called")  # Message to indicate constructor is called
        print(self)
        self.name = name  # Initializing attributes
        self.age = age
        
# wahi contructor chalega jo last me jiske parameters match karenge object banate waqt 
person1 = Person("Alice", 30)  
print(person1)
print(person1.name) #Alice

person2 = Person("Bob", 25)
print(person2.name) #Bob
print(person2.name , person2.age) 



# Class & Instance Attributes :

# class.attr : 
# obj.attr : 

class Student:
    school = "ABC School"  # Class Attribute , It stored in memory only once and shared among all instances.
    
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute
        
student1 = Student("Himanshu", 20)
print(student1.name)  # Accessing Instance Attribute
print(student1.school)


# What is 2 Class Attributes & Instance Attributes ?

class Student:
    school = "ABC School"  # Class Attribute , It stored in memory only once and shared among all instances.
    name = "Anonymous"  # Class Attribute
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute
        
student1 = Student("Himanshu", 20)
print(student1.name)  # Accessing Instance Attribute

# Note : If we have same name of class and obj attribute then obj attribute will be given priority.


# Methods 
# Method : A method is a function that is defined inside a class and is used to perform operations on the data contained in the class.

class Student:
    school = "ABC School"  # Class Attribute , It stored in memory only once and shared among all instances.
    
    def __init__(self, name, age):
        self.name = name  # Instance Attribute
        self.age = age    # Instance Attribute
        
    def welcome(self):
        print("Welcome Student : ", self.name)
        
    def get_marks(self):
        return self.marks
        
student1 = Student("Himanshu", 20)
student1.welcome()  # Calling the method
print(student1.get_marks())  # Calling the method that returns marks (will give error as marks is not defined)