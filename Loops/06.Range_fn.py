# Range fn : The range() function is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a specific range of values. The range() function can take one, two, or three arguments:
# 1. range(stop): Generates numbers from 0 to stop-1.
# 2. range(start, stop): Generates numbers from start to stop-1.
# 3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.
# start by default is 0 and step by default is 1.

# print(range(5)) 

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])

# apply loop on it

sequence = range(10)
for i in sequence:
    print(i)
    
# range types
for i in range(10): #range(stop)
    print("\n range stop",i)
    
for i in range(1,11): #range(start,stop)
    print(i)
    
for i in range(1,21,2): #range(start,stop,step)
    print(i)