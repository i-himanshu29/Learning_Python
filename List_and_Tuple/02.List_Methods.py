# append() - Adds an element at the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("Updated fruits list:", fruits)

# remove() - Removes the first occurrence of a specified element from the list
fruits.remove("banana")
print("After removing banana:", fruits)

# pop() - Removes and returns the element at a specified index (default is the last element)
popped_fruit = fruits.pop()
print("Popped fruit:", popped_fruit)
print("Fruits list after pop:", fruits)

# insert() - Inserts an element at a specified index
fruits.insert(1, "kiwi") # inserting kiwi at index 1
print("\nAfter inserting kiwi:", fruits)

# sort() - Sorts the elements of the list in ascending order
fruits.sort()
print("Sorted fruits list:", fruits)

# reverse() - Reverses the order of elements in the list
fruits.reverse()
print("Reversed fruits list:", fruits)


# sorting in decreasing order
students = ["John", "Alice", "Bob", "Diana"]
print("...", students.sort(reverse=True)) 
print("Sorts the list in descending order",students)

list = [2,1,3]
print(list.append(4))  # Appends 4 to the list
print("\n", list.sort(reverse=True))  # Sorts the list in descending order
print(list)
# also apply on characters

