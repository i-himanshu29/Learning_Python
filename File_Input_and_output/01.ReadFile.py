# Python can be used to perform file input and output operations. (read and write data)

# Types of all files
# Text files: These files contain plain text and are human-readable. They usually have extensions like .txt, .csv, .html, .docx , .log etc.
# Binary files: These files contain data in a format that is not human-readable. They can include images, audio files, executable files, etc.
# Binary file like - .jpg, .png, .exe, .bin , .mov , .mp4 etc.

# open , read & close file
# We have to open a file before we can read or write to it. After we are done, we should close the file to free up system resources.

f = open("demo.txt", "r")  # Open a file in read mode
data = f.read()          # Read the contents of the file
print(data)              # Print the contents
print(type(data))        # Print the type of data
f.close()                # Close the file


# Mode    Description

# 'r'      Open a file for reading (default mode)
# 'w'      Open a file for writing (creates a new file or truncates an existing file)
# 'a'      Open a file for appending (adds data to the end of the file)
# 'b'      Open a file in binary mode (used with other modes, e.g., 'rb' or 'wb')
# 't'      Open a file in text mode (default mode, used with other modes, e.g., 'rt' or 'wt')
# '+'      Open a file for updating (reading and writing)
# 'x'      Open a file for exclusive creation (fails if the file already exists)
# 'U'      Universal newline mode (deprecated in Python 3, use 'r' instead)

# 'r+'     Open a file for both reading and writing
# 'w+'     Open a file for both writing and reading (creates a new file or truncates an existing file)
# 'a+'     Open a file for both appending and reading

# 'rb'     Open a file for reading in binary mode
# 'wb'     Open a file for writing in binary mode
# 'ab'     Open a file for appending in binary mode

# 'rt'     Open a file for reading in text mode
# 'wt'     Open a file for writing in text mode
# 'at'     Open a file for appending in text mode

# 'xb'     Open a file for exclusive creation in binary mode
# 'xt'     Open a file for exclusive creation in text mode

# 'r+b'    Open a file for both reading and writing in binary mode
# 'w+b'    Open a file for both writing and reading in binary mode
# 'a+b'    Open a file for both appending and reading in binary mode

# 'r+t'    Open a file for both reading and writing in text mode
# 'w+t'    Open a file for both writing and reading in text mode
# 'a+t'    Open a file for both appending and reading in text mode

# 'x+b'    Open a file for exclusive creation in binary mode
# 'x+t'    Open a file for exclusive creation in text mode


# If i want to read a particular set of character
f = open("demo.txt", "r")
data = f.read(5)          # Read the first 5 characters of the file
print(data)
f.close()                # Close the file

# read line by line
f = open("demo.txt", "r")
line1 = f.readline()      # Read the first line of the file
print(line1)
f.close()                # Close the file

# read line by line - 2nd line
f = open("demo.txt", "r")

line1 = f.readline()      # Read the first line of the file
print(line1)

line2 = f.readline()      # Read the first line of the file
print(line2)

f.close()                # Close the file


# data is already read
f = open("demo.txt", "r")
data = f.read()          # Read the contents of the file
print(data)              # Print the contents

line1 = f.readline()      # Try to read the first line of the file again
print(line1)             # This will print an empty string since the file pointer is at the end of the file

line2 = f.readline()      # Try to read the second line of the file again
print(line2)             # This will also print an empty string

f.close()                # Close the file



