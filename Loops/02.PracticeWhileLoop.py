# Problem-1 : Print numbers from 1 to 100
i = 1
while(i <= 100):
    print(i)
    i += 1


# Problem-2 : Print numbers from 100 to 1
i = 100
while(i >= 1):
    print(i)
    i -= 1


# Problem-3 : Print the multiplication table of a number n.
number = int(input("Enter a number to print its multiplication table: "))
i = 1
while(i <= 10):
    print(number*i)
    i += 1


# Problem-4 : Print the elements of the following list using a loop.
# [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while(idx < len(nums)):
    print(nums[idx])
    idx += 1
    

heros = ["ironman","thor","hulk","captain america","black panther"]
# taverse the list heros using while loop and print each hero in a new line
idx = 0
while(idx < len(heros)):
    print(heros[idx])
    idx += 1
    

# Problem-5 : Search for a number x in this tuple using loop
# [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100,36)
x = int(input("Enter a number to search in the tuple: "))

idx = 0
while(idx < len(nums)):
    if(nums[idx] == x):
        print(f"Number {x} found at index {idx}")
    else:
        print(f"Number {x} not found at index {idx}")
    idx += 1
    
# or use break to stop at first occurrence

idx = 0
while(idx < len(nums)):
    if(nums[idx] == x):
        print("finding",idx)
        break
    idx += 1