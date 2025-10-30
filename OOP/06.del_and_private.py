# del Keyword : Used to delete object properties or object itself

class Student:
    def __init__(self,name):
        self.name = name
    
s1 = Student("Himanshu")
print(s1.name)

del s1.name
print(s1.name)


# Private(like) attributes & methods
# conceptual implementation in python
# Private attributes and methods are meant to be used only within the class and are not accessible from outside the class

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # __ for private
    
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.__acc_pass) # we cannot access outside the class
print(acc1.reset_pass())

class Person:
    __name = "Anonymous"
    
    def __hello(self,name):
        print("hello person!")
    
    def welcome(self):
        self.__hello()
        
p1 = person()
print(p1.__hello)
print(p1.welcome())


