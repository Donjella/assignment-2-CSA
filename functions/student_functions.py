# functions/student_functions.py
from functions.classroom_functions import assign_student
from classes.students import Student
from classes.parent_guardian import ParentGuardian  # Import the ParentGuardian class
from datetime import datetime

def add_student(students, classrooms):
    # Validate first name (fname)
    while True:
        try:
            fname = input("Enter student's first name: ").strip().capitalize()
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
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted.")
            return  

    # Validate last name (lname)
    while True:
        try:
            lname = input("Enter student's last name: ").strip().capitalize()
            # Check for consecutive hyphens first
            if '--' in lname:
                raise ValueError("Last name cannot contain consecutive hyphens ('--').")
            # Allow alphabets and hyphens only
            elif lname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("Last name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(e)
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted.")
            return  

    # Validate birthday input with try...except block
    while True:
        birthday = input("Enter student's birthday (YYYY-MM-DD): ")
        try:
            birthday_date = datetime.strptime(birthday, "%Y-%m-%d")
            # Calculate age based on birthday and current date
            age_in_years = (datetime.now() - birthday_date).days // 365
            # Check if the age falls within any classroom range
            if not any(classroom.is_valid_for_age(age_in_years) for classroom in classrooms):
                print(f"Student's age ({age_in_years} years) is out of the range for all available classrooms. No further input is needed")
                return  # Exit the function without collecting more input
            break
        except ValueError:
            print("Invalid date format or date out of range. Please enter valid date in the format YYYY-MM-DD.")

     # Initialize an empty list for allergies
    allergies = []

    # Validate if the student has allergies
    while True:
        has_allergy = input("Does the student have any allergies? (yes/no): ").strip().lower()
        if has_allergy in ['yes', 'y', 'no', 'n']:
            break  # Valid input, exit loop
        else:
            print("Please enter a valid answer - 'yes' or 'y' and 'no' or 'n'.")

    # If the student has allergies, ask for each allergy
    if has_allergy in ['yes', 'y']:
        while True:
            try:
                # Get the first allergy
                allergy = input("Enter the allergy: ").strip().capitalize()
                
                # Check that allergy is not empty and contains only alphabetic characters, spaces, or hyphens
                if allergy and all(char.isalpha() or char in [' ', '-'] for char in allergy):
                    allergies.append(allergy)
                else:
                    raise ValueError("Allergy should only contain alphabetic characters, spaces, or hyphens. Please try again.")

                # Ask if there are more allergies
                while True:
                    more_allergies = input("Does the student have any more allergies? (yes/no): ").strip().lower()
                    if more_allergies in ['yes', 'y', 'no', 'n']:
                        break  # Valid input, exit loop
                    else:
                        print("Please enter a valid answer - 'yes' or 'y' and 'no' or 'n'.")

                # Exit the loop if there are no more allergies
                if more_allergies in ['no', 'n']:
                    break
            except ValueError as e:
                print(e)

    # Collect guardian details
    print("\nEnter parent/guardian information:")

    # Validate guardian first name and last name
    while True:
        try:
            guardian_fname = input("Enter guardian's first name: ").strip().capitalize()
            # Check for consecutive hyphens
            if '--' in guardian_fname:
                raise ValueError("Guardian's first name cannot contain consecutive hyphens ('--').")
            # Allow alphabets and hyphens only
            elif guardian_fname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("Guardian's first name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(e)
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted.")
            return  # You can choose to exit the function or handle as needed

# Validate guardian last name
    while True:
        try:
            guardian_lname = input("Enter guardian's last name: ").strip().capitalize()
            # Check for consecutive hyphens
            if '--' in guardian_lname:
                raise ValueError("Guardian's last name cannot contain consecutive hyphens ('--').")
            # Allow alphabets and hyphens only
            elif guardian_lname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("Guardian's last name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(e)
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted.")
            return  

    # Validate emergency contact number (should contain only digits and check length)
    while True:
        try:
            contact_number = input("Enter guardian's contact number (numbers only): ").strip()
            # Check if it's a valid 10-digit Australian number
            if contact_number.isdigit() and len(contact_number) == 10 and (contact_number.startswith('04') or contact_number.startswith('0')):
                break  # Valid input, exit loop
            else:
                print("Contact number should start with '04' for mobiles or '0' for landlines, and contain exactly 10 digits.")
                print("International contacts with '+' area codes are not accepted\n")
        except (KeyboardInterrupt, EOFError):
            print("\nInput interrupted.")
            return 

    # Validate emergency contact email
    while True:
        try:
            contact_email = input("Enter guardian's contact email: ").strip()
            
            # Check for spaces
            if " " in contact_email:
                raise ValueError("Email address should not contain spaces.")
            
            # Check for a single '@'
            if contact_email.count("@") != 1:
                raise ValueError("Email address should contain exactly one '@' symbol.")
            
            # If all checks pass, break the loop
            break
            
        except ValueError as e:
            print(e)
        except EOFError:
            print("\nInput interrupted.")
            return
        except Exception:
            print("Please enter a valid email.")

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
        print("\nNo parent/guardian details to display as no students enrolled.\n")
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
