# functions/student_functions.py
from functions.classroom_functions import assign_student
from classes.students import Student
from classes.parent_guardian import ParentGuardian  # Import the ParentGuardian class
from datetime import datetime

def add_student(students, classrooms):
    # Validate first name (fname)
    while True:
        try:
            fname = input("Enter student's first name: ")
            # Check for consecutive hyphens first
            if '--' in fname:
                raise ValueError("First name cannot contain consecutive hyphens ('--').")
            # Allow alphabets and hyphens only
            elif fname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("First name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(e)

    # Validate last name (lname)
    while True:
        try:
            lname = input("Enter student's last name: ")
            # Allow alphabets and hyphen only
            if lname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("Last name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(e)


    # Validate birthday input with try-except block
    while True:
        birthday = input("Enter student's birthday (YYYY-MM-DD): ")
        try:
            # Try to parse the date; if it fails, an exception is raised
            datetime.strptime(birthday, "%Y-%m-%d")
            break  # Valid date, exit loop
        except ValueError:
            print("Invalid date format or date out of range. Please enter valid date in the format YYYY-MM-DD.")

    # Initialize an empty list for allergies
    allergies = []

    while True:
        has_allergy = input("Does the student have any allergies? (yes/no): ").strip().lower()
        if has_allergy in ['yes', 'no']:
            break  # Valid input, exit loop
        else:
            print("Please enter 'yes' or 'no'.")

    if has_allergy == 'yes':
        while True:
            # Get the first allergy
            allergy = input("Enter the allergy: ").strip().capitalize()
            allergies.append(allergy)

            # Ask if there are more allergies
            more_allergies = input("Does the student have any more allergies? (yes/no): ").strip().lower()

            if more_allergies != 'yes':
                break  # Exit the loop if there are no more allergies

    # Collect guardian details
    print("\nEnter parent/guardian information:")

    # Validate guardian first name and last name
    while True:
        guardian_fname = input("Enter guardian's first name: ")
        guardian_lname = input("Enter guardian's last name: ")

        if guardian_fname.isalpha() and guardian_lname.isalpha():
            break  # Valid input, exit loop
        else:
            print("First name and last name should only contain alphabets. Please try again.")

    # Validate emergency contact number (should contain only digits)
    while True:
        contact_number = input("Enter guardian's contact number (numbers only): ")
        if contact_number.isdigit():
            break  # Valid input, exit loop
        else:
            print("Contact number should only contain numbers. Please try again.")

    # Validate emergency contact email
    while True:
        contact_email = input("Enter guardian's contact email: ")
        if "@" in contact_email and "." in contact_email:  # Simple validation check for an email structure
            break  # Valid input, exit loop
        else:
            print("Please enter a valid email address.")

    # Create the parent/guardian object
    guardian = ParentGuardian(guardian_fname, guardian_lname, contact_number, contact_email)

    # Create a new student with guardian details
    student = Student(fname, lname, birthday, allergies)

    # Attach the guardian to the student
    student.guardian = guardian

    # Check if the student_id is None, indicating the ID couldn't be generated
    if student.student_id is None:
        print("\nChildcare is full. No more unique student IDs available.")
        return  # Exit the function without adding the student

    # Assign student to the correct classroom based on age
    assign_student(classrooms, student)

    # Add student to the global students list
    students.append(student)

def list_guardian_details(students):
    """List parent/guardian details for a specific student by student ID."""
    if not students:
        print("\nNo students to display.\n")
        return
    try:
        # Prompt for a student ID
        student_id = int(input("\nEnter the student ID to view guardian details: "))
    except ValueError:
        print("Invalid input. Please enter a valid numeric student ID.")
        return

    # Find the student by ID
    # use next() to retrieve first item that matach student id
    student = next((student for student in students if student.student_id == student_id), None)
    
    if student:
        guardian = student.guardian
        if guardian:
            print(f"\nStudent: {student.full_name} (ID: {student.get_formatted_id()})")
            print(f"  Guardian Name: {guardian.full_name}")
            print(f"  Contact Number: {guardian.contact_number}")
            print(f"  Contact Email: {guardian.contact_email}\n")
        else:
            print(f"Student: {student.full_name} (ID: {student.get_formatted_id()}) has no associated guardian.\n")
    else:
        print(f"No student found with ID {student_id}.")
