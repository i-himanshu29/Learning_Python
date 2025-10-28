# Python..................
# Python is the simple & easy 
# Free and open source
# High-level programming language
# Developed by Guido van Rossum
# Python is Interpreted language
# Python is Dynamically typed language
# Python is Object-Oriented language
# Python is Portable language
# Python is case-sensitive language




# Used for..............
# Web Development (Django, Flask)
# Data Science (Pandas, NumPy, Matplotlib)
# Machine Learning (Scikit-learn, TensorFlow)
# Artificial Intelligence
# Scripting
# Automation
# Game Development
# Desktop Application Development (Tkinter, PyQt)
# Network Programming
# Cybersecurity
# Internet of Things (IoT)
# Scientific Computing



# Python Character Set...............
# Letters (A-Z, a-z), 
# Digits (0-9), 
# Special Characters (like !, @, #, etc.), and 
# Whitespace characters (space, tab, newline).


# Variable Names in Python..............
# Varable is a name given to memory location to store data in program.
# varaible are changeable i.e we can change the value stored in variable.

# name = "Himanshu"
# age = 23
# price1 = 100


# Rules for naming variables in Python..............
# Identifiers can be a combination of letters, digits, and underscores
# Cannot start with a digit (0-9)
# cannot use special characters like !, @, #, $, %, etc.
# Identifiers are case-sensitive (e.g., myVar and myvar are different)
# Identifiers can be of any length


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

# Keywords in Python.................
# Keywords are reserved words in Python that have special meanings and cannot be used as identifiers (variable names, function names, etc.).
# Examples of keywords: False, None, True, and, as, assert, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield


# Comments in Python.................
# Comments are used to explain the code and make it more readable.
# Single-line comments start with the # symbol.
# Multi-line comments can be created using triple quotes (''' or """).


# Operators in Python.................
# An operator is a special symbol that performs specific operations on one or more operands (values or variables).
# Types of operators:
# Arithmetic Operators: +, -, *, /, %, **, //
# Comparison Operators: ==, !=, >, <, >=, <=
# Logical Operators: and, or, not
# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
# Bitwise Operators: &, |, ^, ~, <<, >>
# Membership Operators: in, not in
# Identity Operators: is, is not


# Type Conversion in Python.................
# Type conversion is the process of converting one data type to another.
# Implicit Type Conversion: Automatically done by Python.
# Explicit Type Conversion: Manually done by the programmer using functions like int(), float(), str(), etc.
# Example of Explicit Type Conversion:
'''
num_str = "123"
num_int = int(num_str)
print("The string value:", num_str)
print("The integer value:", num_int)
print("Data type of num_str:", type(num_str))
print("Data type of num_int:", type(num_int))
'''

# Example of Implicit Type Conversion:

'''
num_int2 = 10
num_float = 5.5
result = num_int2 + num_float
print("The result of addition:", result)
print("Data type of result:", type(result))
'''


# Input in Python.................
# input() function is used to take input from the user.
# Example:
'''
name = input("Enter your name: ")
print("Hello, " + name + "!") 
'''


# Output in Python.................
# print() function is used to display output to the user.
# Example:
'''
age = 23
print("I am", age, "years old.") 
'''

# String in Python.................
# A string is a sequence of characters enclosed in single quotes (' ') or double quotes (" ").
# strings are immutable i.e we cannot change the value of string after creation.
# Example:
'''
greeting = "Hello, World!"
print(greeting)
print("Length of the string:", len(greeting)) 
'''

# String Methods in Python.................
# Concatenation: Joining two or more strings using the + operator.
# Length: Using len() function to get the length of a string.
# Uppercase: Using upper() method to convert a string to uppercase.
# Lowercase: Using lower() method to convert a string to lowercase.
 
# Indexing: Accessing individual characters in a string using their index.
# Slicing: Extracting a substring from a string using slicing notation.

# Conditional Statements in Python.................
# Conditional statements are used to perform different actions based on different conditions.
# if statement: Executes a block of code if a specified condition is true.
# if-else statement: Executes one block of code if a condition is true and another block if it is false.
# elif statement: Checks multiple conditions and executes the corresponding block of code for the first true condition.
# Example:
'''
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
'''

# Note: In Python, indentation is crucial for defining the scope of conditional statements.
# Make sure to use consistent indentation (usually 4 spaces) for blocks of code within conditional statements.


# Lists in Python.................
# A list is an ordered collection of items that can be of different data types.
# Lists are mutable, meaning their elements can be changed after creation.

# strings are immutable i.e we cannot change the value of string after creation.

# lists allows assignment i.e we can change the value stored in list.

# Example:
'''
fruits = ["apple", "banana", "cherry"]
print(fruits)
print("First fruit:", fruits[0])
print("Length of the list:", len(fruits))
'''

# lists slicing in Python.................
# Slicing allows you to extract a portion of a list by specifying a start and end index.
# Example:
'''
numbers = [10, 20, 30, 40, 50, 60]
subset = numbers[1:4]  # Extracts elements from index 1 to 3
print("Subset of numbers:", subset)
'''

# Lists Methods in Python.................
# append(): Adds an element to the end of the list.
# remove(): Removes the first occurrence of a specified element from the list.
# pop(): Removes and returns the element at a specified index (default is the last element).
# insert(): Inserts an element at a specified index.
# sort(): Sorts the elements of the list in ascending order.
# reverse(): Reverses the order of elements in the list.
# Example:
'''
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Updated fruits list:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits list after pop:", fruits)
fruits.insert(1, "kiwi")
print("After inserting kiwi:", fruits)
fruits.sort()
print("Sorted fruits list:", fruits)
fruits.reverse()
print("Reversed fruits list:", fruits)
'''


# Tuples in Python.................
# A tuple is an ordered collection of items that can be of different data types.
# Tuples are immutable, meaning their elements cannot be changed after creation.
# Example:
'''
coordinates = (10, 20)
print(coordinates)
print("First coordinate:", coordinates[0])
print("Length of the tuple:", len(coordinates))
'''


# Tuple Slicing in Python.................
# Slicing allows you to extract a portion of a tuple by specifying a start and end index.
# Example:
'''
numbers = (10, 20, 30, 40, 50, 60)
subset = numbers[2:5]  # Extracts elements from index 2 to 4
print("Subset of numbers:", subset)
'''


# Tuple Methods in Python.................
# count(): Returns the number of occurrences of a specified element in the tuple.
# index(): Returns the index of the first occurrence of a specified element in the tuple.




# Dictionaries in Python.................
# It is used to store data values in key:value pairs.
# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are mutable, meaning their elements can be changed after creation.
#  Don't allows duplicate keys
# Example:
'''
person = {"name": "Himanshu", "age": 23, "city": "New York"}
print(person)
print("Name:", person["name"])
print("Length of the dictionary:", len(person))
'''

# Nested Dictionary in Python.................
# A nested dictionary is a dictionary that contains another dictionary as a value for one of its keys.
# Example:
'''
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "Math": 95,
        "Science": 88,
        "English": 92
    }
}

print(student)
print("Courses:", student["courses"])
print("Math score:", student["courses"]["Math"])
'''

# Dictionary Methods in Python.................
# keys(): Returns a view object containing the keys of the dictionary.
# values(): Returns a view object containing the values of the dictionary.
# items(): Returns a view object containing the key-value pairs of the dictionary as tuples.
# get(): Returns the value for a specified key, or a default value if the key is not found.
# pop(): Removes and returns the value for a specified key.
# update(): Updates the dictionary with key-value pairs from another dictionary or iterable.


# Sets in Python.................
# A set is an unordered collection of unique items.
# Sets are mutable, meaning their elements can be changed after creation.
# set can store multiple data types i.e int, float, string , boolean ,tuple etc.
# set can't store mutable data types like list, dictionary , set etc.

# set -> mutable
# set ke elements -> immutable hote hai

# Example:
'''
fruits = {"apple", "banana", "cherry"}
print(fruits)
print("Length of the set:", len(fruits))
'''

# Methods in Set.................
# add(): Adds an element to the set.
# remove(): Removes a specified element from the set. Raises an error if the element is not found.
# discard(): Removes a specified element from the set. Does not raise an error if the element is not found.
# pop(): Removes and returns an arbitrary element from the set.
# union(): Returns a new set that is the union of two sets.
# intersection(): Returns a new set that is the intersection of two sets.
# difference(): Returns a new set that is the difference of two sets.
# symmetric_difference(): Returns a new set that is the symmetric difference of two sets.
# clear(): Removes all elements from the set.


# Loops in Python.................
# Loops are used to execute a block of code repeatedly until a certain condition is met.
# Types of loops in Python:
# for loop: Used to iterate over a sequence (like a list, tuple, or string) or other iterable objects.
# while loop: Repeats a block of code as long as a specified condition is true.

# Break and Continue Statements in Loops.................
# break statement: Used to exit the loop prematurely when a certain condition is met.
# continue statement: Skips the current iteration of the loop and moves to the next iteration.


# Range Function in Python.................
# Range fn : The range() function is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a specific range of values. The range() function can take one, two, or three arguments:
# 1. range(stop): Generates numbers from 0 to stop-1.
# 2. range(start, stop): Generates numbers from start to stop-1.
# 3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

# Pass Statement in Python.................
# The pass statement is a null operation; it does nothing when executed.
# It is used as a placeholder in situations where a statement is syntactically required but no action is needed.
