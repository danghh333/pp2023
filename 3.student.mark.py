import math
#import numpy as np

class Student:
    def __init__(self):
        self.students = {}

    def input_student_info(self):
        num = int(input("Number of student you want to enter: " ))
        for i in range(0,num):
            student_ID = input("Student ID: ")
            student_name = input("Student name: ")
            student_DOB = input("DOB: ")
            self.students[student_ID] = {"name": student_name, "DOB": student_DOB}

    
    def show_student_info(self):
        for student_ID in self.students:
            print(f"{student_ID}: {self.students[student_ID]['name']}")

class Course:
    def __init__(self):
        self.courses = {}

    def input_course_info(self):
        num = int(input("Number of course you want to enter: "))
        for i in range(0,num):
            course_ID = input("Course ID: ")
            course_name = input("Course name: ")
            self.courses[course_ID] = {"name": course_name}

    def show_course_info(self):
        for course_ID in self.courses:
            print(f"{course_ID}: {self.courses[course_ID]['name']}")

class Mark:
    def __init__(self):
        self.marks = {}

    def input_student_mark(self, student, course):
        course_ID = input("Enter the course ID: ")
        if course_ID not in course.courses:
            print("Invalid course ID")
        for student_ID in student.students:
            mark = math.floor((float(input(f"Enter the mark for {student.students[student_ID]['name']}: ")))*10)/10
            if student_ID not in self.marks:
                self.marks[student_ID] = {}
            self.marks[student_ID][course_ID] = mark

    def show_student_mark(self, student, course):
        course_ID = input("Enter the course ID: ")
        for student_ID in student.students:
            if student_ID in self.marks and course_ID in self.marks[student_ID]:
                print(f"{student.students[student_ID]['name']}: {self.marks[student_ID][course_ID]}")

student_obj = Student()
course_obj = Course()
mark_obj = Mark()

while True:
    print("Select an option")
    print("1. Enter student info")
    print("2. Enter course info")
    print("3. Next functions")
    choice = input("Enter your choice: ")
    if choice == "1":
        student_obj.input_student_info()
    elif choice == "2":
        course_obj.input_course_info()
    elif choice == "3":
        break

while True:
    print("Select an option")
    print("1. Input marks for a course")
    print("2. Show course info")
    print("3. Show student info")
    print("4. Show student marks for a given choice")
    print("5. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        mark_obj.input_student_mark(student_obj, course_obj)
    elif choice == "2":
        course_obj.show_course_info()
    elif choice == "3":
        student_obj.show_student_info()
    elif choice == "4":
        mark_obj.show_student_mark(student_obj, course_obj)
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
