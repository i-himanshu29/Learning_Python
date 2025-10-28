# Problem-1: Print the elements of the following list using a for loop.
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

nums = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
for num in nums:
    print(num) 
    

# Problem-2 : Search for a number y in this tuple using a for loop
# (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

nums = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20,12)
x = 12
idx = 0;
for el in nums:
    if el == x:
        print("number found at idx", idx)
    idx += 1
    
# break
nums = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20,12)
x = 12
idx = 0;
for el in nums:
    if el == x:
        print("number found at idx", idx)
        break
    idx += 1