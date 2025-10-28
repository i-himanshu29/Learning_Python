tup = (2,1,3,1)
print(tup[0])

tup[0]=5 # This will raise an error because tuples are immutable

tup = () # empty tuple
print(tup)
print(len(tup))
print(type(tup))

tup = (1,) # single element tuple and , means it's a tuple
print(tup)
print(len(tup))
print(type(tup))


# slicing in tuple
numbers = (10, 20, 30, 40, 50, 60)
subset = numbers[2:5]  # Extracts elements from index 2 to 4
print("Subset of numbers:", subset)

# Tuple Methods in Python.................
# count(): Returns the number of occurrences of a specified element in the tuple.
tup = (1,2,3,1,4,1)
count_1 = tup.count(1)
print("Count of 1 in tuple:", count_1)

# index(): Returns the index of the first occurrence of a specified element in the tuple.
index_3 = tup.index(3)
print("Index of 3 in tuple:", index_3)



