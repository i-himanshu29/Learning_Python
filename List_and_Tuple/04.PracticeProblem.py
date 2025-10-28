# Problem-1 : WAP to ask the user to enter the name of thier 3 favorite movies and store them in a list.

# movies = []
# mov1 = input("Enter the name of your 1st favorite movie: ")
# mov2 = input("Enter the name of your 2nd favorite movie: ")
# mov3 = input("Enter the name of your 3rd favorite movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print("Your favorite movies are:", movies)

# or

movies = []
mov = input("Enter the 1st movie:")
movies.append(mov)
mov = input("Enter the 2nd movie:")
movies.append(mov)
mov = input("Enter the 3rd movie:")
movies.append(mov)
print("Your favorite movies are:", movies)


# Problem-2 : WAP to check if a list contains a palindrome of elements 

list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
    
    
# list2 = ["m","a","d","a","m"]
list2 = ["m","a","d","a","m","p"]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("list2 is a palindrome")
else:
    print("list2 is not a palindrome")
    
    
# Problem-3 : Store the below value in a list & sort them from "A" to "D".

grade = ["D","A","B","C","A","B","D","C","B","A"]
grade.sort()
print("Original grade list:", grade)