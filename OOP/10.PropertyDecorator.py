# Property
# We use @property decorator on any method in the class to use the method as a property.

class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        
stu1 = Student(98,97,99)
print(stu1.percentage)

stud1.phy = 86 # suppose teacher change the no.
print(stud1.phy)
print(stud1.percentage) # It will same percentage means it goes not change after updated the marks

# That's why we do like this.............
# Jab hum kise bhi atttribute ko fix value nhi de sakte toh kise na kise dosre parameter ke uper depend karegi



class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        
    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        
        
stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86 # suppose teacher change the no.
print(stu1.phy)

stu1.calcPercentage()
print(stu1.percentage) # It will same percentage means it goes not change after updated the marks


# But we have another way to do that
# that is Property decorator - @property


class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.math)/3)+"%"
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3)+"%"
        
stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86 # suppose teacher change the no.
print(stu1.phy)
print(stu1.percentage) # It will same percentage means it goes not change after updated the marks

