# Problem-1 : Define a Circle class to create a circle with the radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return 22/7*self.radius ** 2
    
    def perimeter(self):
        return 2 * 22/7 * self.radius
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


# Problem-2 : Create a class called Order which stores item & its price.
# Use Dunder function __gt__() to convey that:
# order1 > order2 if the price of order1 > price of order2
        
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self,odr):
        return self.price > odr2.price
        
    
odr1 = Order("chips",20)
odr2 = Order("tea",15)
 
print(odr1 > odr2) #True