class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
        
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

# Now How to add two complex number
# That's why use Dunder functions - function ke aage double underscore lagate hai __

# a+b   -------->  a.__add__(b)
# a-b   -------->  a.__sub__(b)
# a*b   -------->  a.__mul____(b)
# a/b   -------->  a.__truediv____(b)
# a%b   -------->  a.__mod____(b)
# __mod__
# __and__
# __xor__
# __or__
# __pow__
# __abs__



class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1.add(num2)
num3.showNumber()

# Note : That's how complex number added
# But I don't want to add function here
# that's why we use Dunder function


class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
    
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()

num3 = num1 - num2
num3.showNumber()

# Note : Dunder function is the application of the Dunder Function