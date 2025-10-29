# Problem-1 : WAF to print the length of a list(list is passed as a parameter)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
heros = ["thor","ironman","captain america","hulk","black panther"]

def print_length_of_list(lst):
    length = len(lst)
    print("Length of the list:", length)
    
print_length_of_list(cities)
print_length_of_list(heros)


# Problem-2 : WAF to print the elements of a list in a single line.(list is the parameter)
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
heros = ["thor","ironman","captain america","hulk","black panther"]

def print_len(list):
    print(len(list))
    
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heros)
print()
print_list(cities)
print()


# Problem-3 : WAF to find the factorial of n.(n is the parameter)

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(fact)
    
factorial(6)



# Problem-4 : WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 82.74
    print(f"{usd_val} USD is equal to {inr_val} INR")
    
converter(100)