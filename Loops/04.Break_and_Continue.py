# Break : used to exit the loop completely
# continue : used to skip the current iteration and move to the next iteration

i = 1
while i<=5:
    print(i)
    if i==3:
        break
    i += 1
print("Loop ended")
    
    
# continue example

i = 0
while i<=5:
    if(i==3):
        i += 1
        continue # skip the current iteration when i is 3
    print(i)
    i += 1
    
# print only odd and skip even numbers from 1 to 10

i=1
while i<=10:
    if i%2==0:
        i += 1
        continue
    print(i)
    i += 1
    
# print only even and skip odd numbers from 1 to 10
i=1
while i<=10:
    if i%2!=0:
        i += 1
        continue
    print(i)
    i += 1