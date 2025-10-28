marks = [90, 85, 78, 92, 88]
print("Marks List:", marks)
print("First Mark:", marks[0])
print("Length of Marks List:", len(marks))
print("type of marks:", type(marks))

# store elements of different data types in a list
student = ["Alice", 23, 3.8, True]
print("Student List:", student)
print("Student Name:", student[0])
print("Length of Student List:", len(student))
print("type of student:", type(student))


# lists are mutable and allows assignment
student = ["Alice", 23, 3.8, True]
student[1] = 24  
student[0] = "Bob"
print("Updated Student List:", student)


# lists slicing in Python.................
# similar to string slicing

numbers = [10, 20, 30, 40, 50, 60]
subset = numbers[1:4]  # Extracts elements from index 1 to 3
print("Subset of numbers:", subset) #[20, 30, 40]

# Negative indexing in lists
last_element = numbers[-1]  # Access the last element
print("Last element using negative indexing:", last_element) #60
first_three = numbers[:-3]  # Access all elements except the last three
print("First three elements using negative slicing:", first_three) #[10, 20, 30]
range = numbers[-3:-1]
print("Range using negative slicing:", range) #[40, 50]
