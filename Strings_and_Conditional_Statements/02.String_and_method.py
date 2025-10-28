# Creating a string
my_string = "  MCA students  "

# Display the original string
print("Original String:", my_string)   

# 1. strip() - removes spaces from beginning and ending in string
print("After strip():", my_string.strip()) 

# 2. lower() - converts to lowercase
print("Lowercase:", my_string.lower())  

# 3. upper() - converts to uppercase
print("Uppercase:", my_string.upper())  

# 4. title() - converts first letter of each word to uppercase
print("Title Case:", my_string.title()) 

# 5. replace() - replaces part of the string
print("Replace 'MCA' with 'BCA':", my_string.replace("MCA", "BCA"))   

# 6. split() - splits string into list
print("Split by spaces:", my_string.split())  

# 7. join() - joins elements of a list with a separator
words = ["Python", "is", "fun"]
print("Join with '+':", "+".join(words))  
 
# string concatination 
words1 = "Python"
words2 = "Hai ji"
print("Join with '+':", (words1 + " " + words2))   

# 8. find() - returns the index of first occurrence
print("Index of 'MCA':", my_string.find("MCA"))

# 9. count() - counts occurrences of a substring
print("Count of 's':", my_string.count("s"))

# 10. isalpha() - checks if all characters are alphabets
print("'MCA'.isalpha():", "MCA".isalpha())
print("'MCA1'.isalpha():", "MCA1".isalpha())

# 11. isnumeric() - checks if all characters are digits
print("'1234'.isnumeric():", "1234".isnumeric())
print("'1234H'.isnumeric():", "1234H".isnumeric())

# 12. startswith() and endswith()
print("Starts with 'MCA':", my_string.strip().startswith("MCA"))
print("Ends with 'nts!':", my_string.strip().endswith("nts"))

# 13. format() - formats a string
age = 21
formatted_string = "I am {} years old.".format(age)
print("Formatted String:", formatted_string)

# 14 . capitalize() - capitalizes the first character of the string
hello_str = "hello world"
print("Capitalized String:", hello_str.capitalize())

# 15. center() - centers the string within a specified width
centered_str = "MCA".center(20, '*')
print("Centered String:", centered_str)
