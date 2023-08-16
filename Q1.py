"""
Task: Build a basic management system of your own choice such as student, online shop etc,
that uses the idea of inheritance. Also, mention the type of inheritance being used.
"""
class Parent:
    def __init__(self, p_name):
        self.p_name = p_name
class Student(Parent): #types of inheritance: single inheritance
    def __init__(self, name, roll, branch):
        self.name = name
        self.roll = roll
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Parent Name:", p_name)
        print("Roll Number:", self.roll)
        print("Branch:", self.branch)

class Marks(Student): #types of inheritance: multiple inheritance
    def __init__(self, name, roll, branch, marks):
        self.marks = marks

    def display(self):
        print("Marks:", self.marks)

class Attendance(Student): #types of inheritance: multiple inheritance
    def __init__(self, name, roll, branch, attendance):
        self.attendance = attendance

    def display(self):
        print("Attendance:", self.attendance)

class Result(Marks, Attendance): #types of inheritance: multiple inheritance
    def __init__(self, name, roll, branch, marks, attendance):
        self.marks = marks
        self.attendance = attendance
    def display(self):
        print("Result:", self.marks + self.attendance)


print("Welcome to the Student Management System")
print("Enter the details of the student")
print()
name = input("Enter the name of the student: ")
p_name = input("Enter the name of the parent: ")
roll = input("Enter the roll number of the student: ")
branch = input("Enter the branch of the student: ")
marks = int(input("Enter the marks of the student: "))
attendance = int(input("Enter the attendance of the student: "))
print()
print("The details of the student are:")
p = Parent(p_name)
s = Student(name, roll, branch)
s.display()
m = Marks(name, roll, branch, marks)
m.display()
a = Attendance(name, roll, branch, attendance)
a.display()
r = Result(name, roll, branch, marks, attendance)
r.display()
