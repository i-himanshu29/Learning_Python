# Polymorphysm : 
# When the same operator is allowed to have different meaning according to the context.


# Dunder function - operator Overloading


# Method Overriding (Runtime Polymorphism)
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
a.sound()
d = Dog()
d.sound()

# Duck Typing (Compile-time Polymorphism)
def call_sound(obj):
    obj.sound()

class Cat:
    def sound(self):
        print("Cat meows")

call_sound(Dog())
call_sound(Cat())
