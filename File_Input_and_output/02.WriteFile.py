# Writing to a file...........................................................................................................................................
# Definiton : To write data to a file, you need to open the file in write ('w'), append ('a'), or exclusive creation ('x') mode. 
# If the file does not exist, it will be created. If it already exists and you open it in write mode, the existing content will be truncated (deleted).

f = open("output.txt", "w")  # Open a file in write mode
f.write("Hello, World!\n")   # Write data to the file   
f.write("This is a test file.\n")  # Write more data to the file
f.close()                     # Close the file


# append the data in output file
f = open("output.txt", "a")  # Open a file in append mode
f.write("This line is appended.\n")  # Append data to the file
f.close()                     # Close the file


# With Syntax
# task : open the file , read the data and close the file
# When you are using with syntax, Python automatically takes care of closing the file for you, even if an error occurs while working with the file.
with open("output.txt", "r") as f: # f : file object and it is aliess
    data = f.read()
    print(data)
    
with open("output.txt", "w") as f:
    f.write("Using with syntax to write data.\n")
    
    