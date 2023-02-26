student = {}
course = {}
marks = {}

def input_student_info():
    num = int(input("Number of student you want to enter: " ))
    for i in range(0,num):
        student_ID = input("Student ID: ")
        student_name = input("Student name: ")
        student_DOB = input("DOB : ")
        student[student_ID] = {"name": student_name, "DOB": student_DOB}

def input_course_info():
    num = int(input("Number of course you want to enter: "))
    for i in range(0,num):
        course_ID = input("Course ID: ")
        course_name = input("Course name: ")
        course[course_ID] = {"name": course_name}

def input_student_mark():
    course_ID = input("Enter the course ID: ")
    if course_ID not in course:
        print("Invalid course ID")
    for student_ID in student:
        mark = int(input(f"Enter the mark for {student[student_ID]['name']}: "))
        if student_ID not in marks:
            marks[student_ID] = {}
        marks[student_ID][course_ID] = mark

def input_marks():
    course_id = input("Enter the course ID: ")
    if course_id not in courses:
        print("Invalid course ID")
        return
    for student_id in students:
        mark = int(input(f"Enter the mark for {students[student_id]['name']}: "))
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark

def show_student_info():
    for student_ID in student:
        print(f"{student_ID}: {student[student_ID]['name']}")

def show_course_info():
    for course_ID in course:
        print(f"{course_ID}: {course[course_ID]['name']}")

def show_student_mark():
    course_ID = input("Enter the course ID: ")
    for student_ID in student:
        if student_ID in marks and course_ID in marks[student_ID]:
            print(f"{student[student_ID]['name']}: {marks[student_ID][course_ID]}")

while True:
    print("Select an option")
    print("1. Enter student info")
    print("2. Enter course info")
    print("3. Next functions")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_student_info()
    elif choice == "2":
        input_course_info()
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
        input_student_mark()
    elif choice == "2":
        show_course_info()
    elif choice == "3":
        show_student_info()
    elif choice == "4":
        show_student_mark()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")












    

  
