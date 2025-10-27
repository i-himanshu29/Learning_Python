age = int(input("Enter your age:"))   # takes age input and converts to integer

if age > 18:                          # checks if greater than 18
    print("You are adult")
else:
    print("You are not adult")


# example of taking multiple inputs
name = input("Enter your name:")  
prentAge = int(input("Enter your parent's age:"))
marks = float(input("Enter your marks:"))

print("Hello,", name)
print("Your parent's age is:", prentAge)
print("Your marks are:", marks)