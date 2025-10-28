# Loops are used to repeat instructions.

# Demonstrating for and while loop.................
print("\nWhile loop example:")
count = 1
while count <= 5:
    print("Hello ji")
    count += 1
print(count)

# print numbers from 1 to 5
i = 5
while i>=1:
    print(i)
    i -= 1
    
print("Loop ended")

# for loop
print("\nFor loop example:")
for i in range(1, 6):
    print(i, end=" ")


# Multiplication Table using while loop
print("\nTable of", num, "using while loop:")
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

