# Used to check if two variables refer to the exact same object in memory. 

a = [1, 2]
b = [1, 2]
c = a

print(a is b)      # False (different objects in memory)
print(a is c)      # True  (same object reference)
print(a is not b)  # True
