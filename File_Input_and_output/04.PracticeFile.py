# Problem - 1 : Create a new file "practice.txt" using python. Add some data in it:


with open("practice.txt","w") as f:
    f.write("Python is a high-level, interpreted programming language.\n")
    f.write("It was created by Guido van Rossum and first released in 1991.\n")
    f.write("Python's design philosophy emphasizes code readability with its notable use of significant whitespace.\n")
    
    
    
# Problem-2 : WAF that replaces all occurrences of "Python" with "Java" in that practice.txt file.

with open("practice.txt","r") as f:
    data = f.read()
new_data = data.replace("Python","Java")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)
    
    
    
    
# Problem-3 : Search if the "learning" exists in the file or not.

with open("practice.txt","r") as f:
    data = f.read()
    word = "programming"
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")


# you can write it in function also

def check_word_in_file():
    with open("practice.txt","r") as f:
    data = f.read()
    word = "programming"
    if(data.find(word)!=-1):
        print("found")
    else:
        print("not found")
        

# Problem-4 : WAF to find in which line of the file does the word "programming" occur first.
# Print-1 if word not found

def check_for_line():
    word = "programming"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
            
    return -1

print(check_for_line())
            
            
# Problem-5 : From a file containing numbers separated by comma, print the count of even numbers.


# brute-force approach
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    num = ""
    for i in range(len(data)):
        if(data[i]==','):
            # print(num)
            print(int(num))
            num = ""
        else:
            num += data[i]
            
# optimized approach

count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
    
    numbers = data.split(",")
    for val in numbers:
        if(int(val)%2==0):
            count += 1
            
print("Count of even numbers :",count)
   