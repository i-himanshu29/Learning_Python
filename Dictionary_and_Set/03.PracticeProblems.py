# Problem-1 : Store following word meanings in a python dictionary and print them
# table :"a piece of furniture","list of facts & figures"
# cat : "a small animal"

dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","list of facts & figures"]
}
print(dictionary)

# Problem-2 : You are given a list of subjects for students.Assume one classroom is required
# for 1 subject.How many classrooms are needed by all students?

"python","java","c","python","java","c++","html","css","html" , "JavaScript","python"

subjects = {
    "python","java","c","python","java","c++","html","css","html" , "JavaScript","python"
}

print(subjects)
print("Number of classrooms needed:", len(subjects))


# Problem-3 : WAP to enter marks of 3 subjects from the user and the store them in a dictionary.
# Start with empty dictionary and add one by one.Use subject name as key and marks as value.

marks = {}
x = input("Enter marks for subject 1: ")
marks.update({"subject 1": x})

x = input("Enter marks for subject 2: ")
marks.update({"subject 2": x})

x = input("Enter marks for subject 3: ")
marks.update({"subject 3": x})

print(marks)



# Problem-4 : Figureout a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

# values = {9, 9.0} # by default 9 and 9.0 are considered same in set as both represent same numeric value
values = {9, "9.0"} # storing 9 as integer and 9.0 as string to make them separate values
print(values)

# second way - built-in data types

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)