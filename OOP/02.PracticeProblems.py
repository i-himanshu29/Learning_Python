# Problem-1 : Create a student class takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Average marks of", self.name, "is", sum / len(self.marks))
    
student1 = Student("Alice", [85, 90, 95])
student1.get_avg()

# If i want to change name of student1

student1.name = "Bob"
student1.get_avg()

