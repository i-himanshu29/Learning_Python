# Class Method :
# A class method is bound to the class & receives the class as an implicit first argument.
# Note:- Static method can't access or modify class & generally for utility.

# class Person:
#     name = "anonymous"
    
#     def changeName(self,name):
#         self.name = name
        
# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)

# #.........
# class Person:
#     name = "anonymous"
    
#     def changeName(self,name):
#         Person.name = name
        
# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)


# .........
class Person:
    name = "anonymous"
    
    def changeName(self,name):
        self.__class__.name = "Rahul hai ji"
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

# Jo kaam @staticmethod nhi kar sakte wo hum class methods ke through karwaate hai

class Person:
    name = "anonymous"
    
    # def changeName(self,name):
    #     self.__class__.name = "Rahul hai ji"
        
    @classmethod
    def changeName(cls,name):
        cls.name = name
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


# static methods
# class methods (cls)
# instance methods (self)