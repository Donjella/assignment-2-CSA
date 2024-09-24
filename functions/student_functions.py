from functions.classroom_functions import classrooms  # Import the classrooms list
from classes.students import Student
from functions.classroom_functions import assign_student
from datetime import datetime

def add_student():
    # Validate first name (fname) and last name (lname)
    while True:
        fname = input("Enter student's first name: ")
        lname = input("Enter student's last name: ")

        if fname.isalpha() and lname.isalpha():
            break  # Valid input, exit loop
        else:
            print("First name and last name should only contain alphabets. Please try again.")

    # Validate contact information (should contain only digits)
    while True:
        contact = input("Enter student's contact information (numbers only): ")
        if contact.isdigit():
            break  # Valid input, exit loop
        else:
            print("Contact information should only contain numbers. Please try again.")

    # Validate birthday input with try-except block
    while True:
        birthday = input("Enter student's birthday (YYYY-MM-DD): ")
        try:
            # Try to parse the date; if it fails, an exception is raised
            datetime.strptime(birthday, "%Y-%m-%d")
            break  # Valid date, exit loop
        except ValueError:
            print("Invalid date format or date out of range. Please enter valid date in the format YYYY-MM-DD.")

    # Create a new student
    student = Student(fname, lname, birthday, contact)

    # Assign student to the correct classroom based on age
    for classroom in classrooms:
        if assign_student(classroom, student):
            break