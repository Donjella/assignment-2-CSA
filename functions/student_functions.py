from functions.classroom_functions import classrooms  # Import the classrooms list
from classes.students import Student
from functions.classroom_functions import assign_student

def add_student():
    name = input("Enter student's name: ")
    birthday = input("Enter student's birthday (YYYY-MM-DD): ")
    contact = input("Enter student's contact information: ")

    # Create a new student
    student = Student(name, birthday, contact)

    # Assign student to the correct classroom based on age
    for classroom in classrooms:
        if assign_student(classroom, student):
            break  