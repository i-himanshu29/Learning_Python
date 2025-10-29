# Recursion is a programming technique where a function calls itself to solve a smaller instance of the same problem.
# Base Case: A condition that stops the recursion to prevent infinite loops.
# Recursive Case: The part of the function where it calls itself with modified arguments.

# call stack : Defined as the mechanism that keeps track of function calls in a program.

def show(n):
    if(n==0): # base case
        return
    print(n)
    show(n-1) # recursive case
    print("END")
    
show(5)


# Example-2 : Factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(4))
print(fact(5))


# Problem-1 : Write a recursive function to calculate the sum of first n natural number.

def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)
    
sum = calc_sum(5)
print(sum)


# Problem-2 : Write a recursive function to print all the elements in a list (Hint:use list & index as parameters).

def print_list(list,idx=0):
    if(idx == len(list)):
        return 
    print(list[idx])
    print_list(list,idx+1)
    
fruits = ["Mango","litchi","apple","banana"]
print_list(fruits)