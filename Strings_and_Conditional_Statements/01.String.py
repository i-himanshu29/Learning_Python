str1 = "This is a sample string."
str2 = 'Python'
print("String 1:", str1)
print("String 2:", str2)

str3 = "this is a python's world"
print("String 3:", str3)

str4 = "This is a multi-line string.\nIt spans multiple lines."
print("String 4:", str4)

# concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + name
print("Full Greeting:",full_greeting)

full_greetings = greeting + " " + name
print("Full Greeting with space:",full_greetings)

#Length of string
# count spaces as well
print("Length of String 1:", len(str1))

# indexing
subject = "Mathematics"
print("First character:", subject[0])

# python don't allow str object item assignment
# subject[0] = 'm'  # This will raise an error

# Slicing
# str[starting_index : ending_index : step] # ending_index is exclusive
print("Substring (0-4):", subject[0:5])  # 'Mathe'
print("Substring (5-):", subject[5:])    # 'matics'
print("Substring (:5):", subject[:5])    # 'Mathe'
print("Substring with step (0-10-2):", subject[0:10:2])  # 'Mteai'

# Negative indexing
print("Substring (-4:):", subject[-4:])  # 'tics'
print("Substring (:-4):", subject[:-4])  # 'Mathema'
print("Substring (-7:-2):", subject[-7:-2])  # 'emati'
print("Substring with step (::-1):", subject[::-1])  # 'scitamhtaM'
