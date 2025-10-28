# The pass statement is a null operation; it does nothing when executed.
# It is used as a placeholder in situations where a statement is syntactically required but no action is needed.

# Below code give error because the for loop is empty and Python expects an indented block after the colon.

# for i in range(5):
#     # empty

# print(some useful_code_here)



# use of Pass statement
# generally used in try-except blocks, functions, classes, loops etc.

for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for even numbers
    else:
        print("odd",i)
        
        
# Problem-1 WAP to find the sum of first n natural numbers using while loop.

n = int(input("Enter a natural number n: "))
i = 1
sum_n = 0
while(i <= n):
    sum_n += i
    i += 1
print("Sum is : ", sum_n)



# Problem-2 : WAP to find the factorial of a number using while loop.

num = int(input("Enter a number to find its factorial: "))
i = 1
factorial = 1
while(i <= num):
    factorial *= i
    i += 1
print(f"Factorial of {num} is : ", factorial)

# in for loop
num = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is : ", factorial)