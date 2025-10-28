# Key can be of type: String, Number, Tuple
# Don't allow duplicate keys

info = {
    "name": "Dictionary",
    "subjects":["Math", "Science", "English"],
    "topic":("Data Types", "Variables", "Loops"),
    "age":30,
    "isActive":True,
    "marks":96.8,
}

print(info)
print(info["name"])
print(info["subjects"])

# print(info["surname"])  # This will raise a KeyError because 'surname' key does not exist

info["name"] = "Himanshu"
print(info)

# Empty dictionary
null_dict = {}
print(null_dict)
# OR
null_dict2 = dict()
null_dict2["new_key"] = "new_value"
print(null_dict2)

# Nested Dictionary...........
student = {
    "name": "Alice",
    "age": 22,
    "courses": {
        "Math": 95,
        "Science": 88,
        "English": 92
    }
}

print(student)
print(student["courses"])
print(student["courses"]["Math"])


# Methods in Dictionary...................

studentDetails = {
    "name": "Alice",
    "age": 22,
    "subjects": {
        "Math": 95,
        "Science": 88,
        "English": 92
    }
}

# Keys()
# keys(): Returns a view object containing the keys of the dictionary.

print(studentDetails.keys())
print(list(studentDetails.keys()))
print(len(studentDetails.keys()))

# values()
# values(): Returns a view object containing the values of the dictionary.

print(studentDetails.values())
print(list(studentDetails.values()))
print(len(studentDetails.values()))

# items()
# items(): Returns a view object containing the key-value pairs of the dictionary as tuples.

print(studentDetails.items())
print(list(studentDetails.items()))
print(len(studentDetails.items()))

pairs = list(studentDetails.items())
print(pairs[0])          # First key-value pair as a tuple


# get()
# get(key, default=None): Returns the value for the specified key if it exists; otherwise, returns the default value.

print(studentDetails["name"])          # Output: Alice
print(studentDetails.get("name"))          # Output: Alice


# let's say somehow you misspelled the key like name2
# print(studentDetails[name2]) # This will raise a NameError because name2 is not defined
print(studentDetails.get("name2"))  # Output: None , not a NameError # use method because it won't raise error and all the program will run smoothly


# update()
# update(other_dict): Updates the dictionary with key-value pairs from another dictionary.

studentDetails.update({"age": 23, "city": "New York"})
print(studentDetails)

# or 

new_dict = {"city": "Los Angeles", "age": 24}
studentDetails.update(new_dict)
print(studentDetails)