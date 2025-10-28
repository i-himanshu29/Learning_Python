# For loop : used to iterate over a sequence (like list, tuple, string) or other iterable objects.

# Example:
print("For loop example:")

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)
    
# Example-2

vegies = ["carrot", "broccoli", "spinach", "potato"]
for veg in vegies:
    print(veg)
    
# Example-3 : for loop on tuple

tup = (10, 20, 30, 40, 50)
for item in tup:
    print(item)
    

# Example-4 : optional - else in for loop 
str = "hello"
for char in str:
    if(char == 'e'):
        print("e found")
        break
    print(char)
else:
    print("Loop completed")