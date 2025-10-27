# Data Types in Python..............
# Data types are used to classify the type of data that a variable can hold.
# Common data types in Python include:
# int: Integer data type (e.g., 10, -5, 0)
# float: Floating-point data type (e.g., 10.5, -3.14)
# str: String data type (e.g., "Hello", 'Python')
# bool: Boolean data type (True or False)
# list: Ordered collection of items (e.g., [1, 2, 3], ['a', 'b', 'c'])
# tuple: Immutable ordered collection of items (e.g., (1, 2, 3), ('x', 'y', 'z'))
# dict: Key-value pairs (e.g., {'name': 'Himanshu', 'age': 23})
# set: Unordered collection of unique items (e.g., {1, 2, 3}, {'a', 'b', 'c'})
# type() function is used to know the data type of variable.
# none : Represents the absence of a value (NoneType)

name1 = "Himanshu"
name2 = 'Himanshu'
name3 = """Himanshu"""

print(type(name1))
print(type(name2))
print(type(name3))

age = 23
old = False
gf = None

print(type(age))
print(type(old))
print(type(gf))