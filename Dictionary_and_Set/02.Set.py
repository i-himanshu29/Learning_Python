# Set : Set is a collection which is unordered, unchangeable*, and unindexed. In Python sets are written with curly brackets.
# Each item in a set is unique and cannot be duplicated.

# set can store multiple data types i.e int, float, string , boolean ,tuple etc.
# set can't store mutable data types like list, dictionary , set etc.

# set -> mutable
# set ke elements -> immutable hote hai



# Create a Set
# collection = {1,2,3,4,5}
# collection = {1,2,"banana",4,"orange"}
collection = {1,2,2,4,"orange","orange"} # duplicate values will be ignored

print(collection)
print(type(collection))
print(len(collection)) # length of set


# Empty Set

empty_set = set() # we have to use set() function to create an empty set
print(empty_set)
print(type(empty_set))


# Methods in Set

methodCollection = set()

# add() method : This method is used to add an element to the set.
methodCollection.add(1)
methodCollection.add(2)
methodCollection.add(2)
methodCollection.add("Himanshu")
methodCollection.add((1,2,3)) # tuple can be added
# methodCollection.add([4,5,6]) # list can't be added , will raise TypeError because list is mutable and unhashable

print(methodCollection) # {1,2} duplicate value will be ignored



# remove() method : This method is used to remove an element from the set. If the element is not found, it raises a KeyError.
methodCollection.remove(2)
# methodCollection.remove(3) # KeyError: 3 not found in set
print(methodCollection) # {1}


# discard() method : This method is used to remove an element from the set. If the element is not found, it does nothing.
methodCollection.discard(3) # no error will be raised
print(methodCollection) # {1}

# unhashable - mutable data types like list, dictionary , set etc. are unhashable
# hashable - immutable data types like int, float, string , boolean ,tuple etc. are hashable



# clear() method : This method is used to remove all elements from the set.
methodCollection.clear()
print(methodCollection) # set() , empty set
print(len(methodCollection)) # 0



# pop() method : This method is used to remove and return an arbitrary element from the set. Raises KeyError if the set is empty.

newCollection = {"apple", "banana", "cherry" , "coding" , "python"}
print(newCollection)
print("Popped item:", newCollection.pop())
print("Popped item:", newCollection.pop())



# union() method : This method returns a new set that is the union of two sets or say combine both set values.
setA = {1, 2, 3}
setB = {3, 4, 5}
setC = setA.union(setB)
print(setC) # {1, 2, 3, 4, 5} , duplicate value 3 will be ignored
print(setA) # {1, 2, 3} , original setA remains unchanged
print(setB) # {3, 4, 5} , original setB remains unchanged


# intersection() method : This method returns a new set that is the intersection of two sets or say common values in both set.

setX = {1, 2, 3, 4}
setY = {3, 4, 5, 6}
setZ = setX.intersection(setY)
print(setZ) # {3, 4} , common values in both set
print(setX) # {1, 2, 3, 4} , original setX remains unchanged
print(setY) # {3, 4, 5, 6} , original setY remains unchanged