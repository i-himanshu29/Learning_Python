# Example-1 : Age Classification
# age = 24
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Note: In Python, indentation is crucial for defining the scope of conditional statements.
# Make sure to use consistent indentation (usually 4 spaces) for blocks of code within conditional statements.

# Example-2 : of traffic light

light = input("Enter the traffic light color (red, yellow, green): ").lower()

if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Get Ready")
elif(light == "green"):
    print("Go")
else:
    print("Invalid color")
    
    
# Example-3 : of grading system

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
elif marks >= 50 and marks < 60:
    print("Grade: E")
else:
    print("Grade: F")
    
    
    
# Nested if-else statements

# Example-4 : Check if a number is positive, negative, or zero and also check if it's even or odd

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
    
    
# Example-5 : Check if a year is a leap year or not

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
        
else:
    print(year, "is not a leap year")
    
    
# Example-6 : Determine the largest of three numbers
# use nesting

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2:
    if num1 >= num3:
        print(num1, "is the largest number")
    else:
        print(num3, "is the largest number")
else:
    if num2 >= num3:
        print(num2, "is the largest number")
    else:
        print(num3, "is the largest number")
        
        
# Example-7 : Determine the largest of 4 numbers
# use nested if-else statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))

if(num1 >= num2):
    if(num1 >= num3):
        if(num1 >= num4):
            print(num1, "is the largest number")
        else:
            print(num4, "is the largest number")
    else:
        if(num3 >= num4):
            print(num3, "is the largest number")
        else:
            print(num4, "is the largest number")
else:
    if(num2 >= num3):
        if(num2 >= num4):
            print(num2, "is the largest number")
        else:
            print(num4, "is the largest number")
    else:
        if(num3 >= num4):
            print(num3, "is the largest number")
        else:
            print(num4, "is the largest number")
            
            
            
