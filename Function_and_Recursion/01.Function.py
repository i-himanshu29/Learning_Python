# A function is a block of reusable code that performs a specific task.
# Functions help in breaking down a program into smaller, manageable parts.
# Defining a Function: Functions are defined using the def keyword followed by the function name and parentheses ().
# Calling a Function: A function is called by using its name followed by parentheses ().
# Parameters and Arguments: Functions can take parameters (inputs) that are passed as arguments when calling the function.
# Return Statement: Functions can return a value using the return statement.


def calc_sum(a, b): # parameters a and b
    """This function takes two numbers as input and returns their sum."""
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)  # Calling the function with arguments 5 and 10

# print hello

def print_hello():
    print("Hello, World!")
    
print_hello()  
print_hello()
print_hello()

# average of three numbers

def average_of_three(x, y, z):
    sum = x + y + z
    average = sum / 3
    return average

avg = average_of_three(10, 20, 30)
print("Average:", avg)


# Built-in Functions:
# Python provides several built-in functions that can be used without importing any additional modules.
# Examples of built-in functions: print(), len(), type(), int(), float(), str(), input(), range(), sum(), max(), min(), sorted(), etc.

# print() function
print("Python Built-in Functions Examples:")
print("Python",end=" ") # end parameter to avoid new line

# len() function
my_list = [1, 2, 3, 4, 5]
print("Length of my_list:", len(my_list))

# type() function
my_var = 42
print("Type of my_var:", type(my_var))

# max() function
numbers = [10, 20, 5, 30, 15]
print("Maximum number:", max(numbers))
# min() function
print("Minimum number:", min(numbers))

# sorted() function
unsorted_list = [5, 2, 9, 1, 5, 6]
sorted_list = sorted(unsorted_list)
print("Sorted list:", sorted_list)

# sum() function
total = sum(numbers)
print("Sum of numbers:", total)


# Default Parameters : A function can have default parameter values that are used if no argument is provided during the function call.

def cal_prod(a=1 , b=3):
    product = a * b
    print(product)
    return product

cal_prod()  

def cal_prod2(a, b=4): # default values taken from last parameter
    product = a * b
    print(product)
    return product

cal_prod2(5) #20
cal_prod2() #erreoer because a is required parameter without default value

def cal_prod3(a=2, b):
    product = a * b
    print(product)
    return product

# cal_prod3(5) #error because non-default parameter b follows default parameter a
