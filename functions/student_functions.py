from datetime import datetime  # Import to handle date and age calculations.
from colored import Style  # Import for styled terminal output.

from constants import color3, color4, color5  # Import predefined color codes for consistent styling.
from functions.classroom_functions import assign_student  # Import to assign students to classrooms.
from classes.students import Student  # Import the Student class for creating student instances.
from classes.parent_guardian import ParentGuardian  # Import the ParentGuardian class for guardian details.

def add_student(students, classrooms):
    # Add a new student to the system.
    # Purpose: This function collects validated input from the user to create a new student instance.
    # It ensures the student is assigned to a classroom based on their age and associates them with a guardian.

    # Example of how it is used:
    #     1. It Prompts the user for validated input: first name, last name, birthday, allergies, and guardian details.
    #     2. Validates user input to ensure correctness and consistency together with exception handling.
    #        Exception handling captures and handles invalid inputs such as valid names (no numbers) and safely exit function if input in interrupted.
    #     3. Checks the student's age and assigns them to an appropriate classroom.
    #     4. Adds the student to the global list of students.

    # Arguments:
    #     students (list): The global list of Student instances to update.
    #     classrooms (list): The list of Classroom instances used for student assignment.

    # Validate first name (fname)
    while True:
        try:
            fname = input("Enter student's first name: ").strip().capitalize()
            # Check for consecutive hyphens first
            if '--' in fname:
                raise ValueError(f"{color5}First name cannot contain consecutive hyphens ('--').{Style.reset}")
            # Allow alphabets and hyphens only
            elif fname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError(f"{color5}First name should only contain alphabets. Hyphens ('-') are allowed.{Style.reset}")
        except ValueError as e:
            print(f"{color5}{e}{Style.reset}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
            return  

    # Validate last name (lname)
    while True:
        try:
            lname = input("Enter student's last name: ").strip().capitalize()
            # Check for consecutive hyphens first
            if '--' in lname:
                raise ValueError(f"{color5}Last name cannot contain consecutive hyphens ('--').{Style.reset}")
            # Allow alphabets and hyphens only
            elif lname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError(f"{color5}Last name should only contain alphabets. Hyphens ('-') are allowed.{Style.reset}")
        except ValueError as e:
            print(f"{color5}{e}{Style.reset}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
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
            print(f"{color5}Invalid date format or date out of range. Please enter valid date in the format YYYY-MM-DD.{Style.reset}")
        

     # Initialize an empty list for allergies
    allergies = []

    # Validate if the student has allergies
    while True:
        try:
            has_allergy = input("Does the student have any allergies? (yes/no): ").strip().lower()
            if has_allergy in ['yes', 'y', 'no', 'n']:
                break  # Valid input, exit loop
            else:
                print(f"{color5}Please enter a valid answer - 'yes' or 'y' and 'no' or 'n'.{Style.reset}")
        except EOFError:
            print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
            return
            

    # If the student has allergies, ask for each allergy
    if has_allergy in ['yes', 'y']:
        while True:
            try:
                # Get the first allergy
                allergy = input("Enter name of allergy: ").strip().capitalize()
                
                # Check that allergy is not empty and contains only alphabetic characters, spaces, or hyphens
                if allergy and all(char.isalpha() or char in [' ', '-'] for char in allergy):
                    allergies.append(allergy)
                else:
                    raise ValueError(f"{color5}Allergy should only contain alphabetic characters, spaces, or hyphens. Please try again.{Style.reset}")

                # Ask if there are more allergies
                while True:
                    more_allergies = input("Does the student have any more allergies? (yes/no): ").strip().lower()
                    if more_allergies in ['yes', 'y', 'no', 'n']:
                        break  # Valid input, exit loop
                    else:
                        print(f"{color5}Please enter a valid answer - 'yes' or 'y' and 'no' or 'n'.{Style.reset}")

                # Exit the loop if there are no more allergies
                if more_allergies in ['no', 'n']:
                    break
            except ValueError as e:
                print(f"{color5}{e}{Style.reset}")
            except EOFError:
                print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
                return
        

    # Collect guardian details
    print("\nEnter parent/guardian information:")

    # Validate guardian first name and last name
    while True:
        try:
            guardian_fname = input("Enter parent/guardian's first name: ").strip().capitalize()
            # Check for consecutive hyphens
            if '--' in guardian_fname:
                raise ValueError("Parent/guardian's first name cannot contain consecutive hyphens ('--').")
            # Allow alphabets and hyphens only
            elif guardian_fname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError("Parent/guardian's first name should only contain alphabets. Hyphens ('-') are allowed.")
        except ValueError as e:
            print(f"{color5}{e}{Style.reset}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
            return  

# Validate guardian last name
    while True:
        try:
            guardian_lname = input("Enter parent/guardian's last name: ").strip().capitalize()
            # Check for consecutive hyphens
            if '--' in guardian_lname:
                raise ValueError(f"{color5}Parent/guardian's last name cannot contain consecutive hyphens ('--').{Style.reset}")
            # Allow alphabets and hyphens only
            elif guardian_lname.replace('-', '').isalpha():
                break  # Valid input, exit loop
            else:
                raise ValueError(f"{color5}Parent/guardian's last name should only contain alphabets. Hyphens ('-') are allowed.{Style.reset}")
        except ValueError as e:
            print(f"{color5}{e}{Style.reset}")
        except (KeyboardInterrupt, EOFError):
            print(f"{color5}\nInput interrupted. Returning to previous menu.{Style.reset}")
            return  

    # Validate emergency contact number (should contain only digits and check length)
    while True:
        try:
            contact_number = input("Enter parent/guardian's contact number (numbers only): ").strip()
            # Check if it's a valid 10-digit Australian number
            if contact_number.isdigit() and len(contact_number) == 10 and (contact_number.startswith('04') or contact_number.startswith('0')):
                break  # Valid input, exit loop
            else:
                print(f"{color5}Contact number should start with '04' for mobiles or '0' for landlines, and contain exactly 10 digits.{Style.reset}")
                print(f"{color5}International contacts with '+' area codes are not accepted{Style.reset}\n")
        except (KeyboardInterrupt, EOFError):
            print(f"{color5}\nInput interrupted. Returning to previous menu.{Style.reset}")
            return 

    # Validate emergency contact email
    while True:
        try:
            contact_email = input("Enter parent/guardian's contact email: ").strip()
            
            # Check for spaces
            if " " in contact_email:
                raise ValueError(f"{color5}Email address should not contain spaces.{Style.reset}")
            
            # Check for a single '@'
            if contact_email.count("@") != 1:
                raise ValueError(f"{color5}Email address should contain exactly one '@' symbol.{Style.reset}")
            
            # If all checks pass, break the loop
            break
            
        except ValueError as e:
            print(f"{color5}{e}{Style.reset}")
        except EOFError:
            print(f"\n{color5}Input interrupted. Returning to previous menu.{Style.reset}")
            return
        except Exception:
            print(f"{color5}Please enter a valid email.{Style.reset}")

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
    #  List parent/guardian details for a specific student by their ID.
    # Purpose: This function retrieves and displays the guardian's details for a given student ID.

    # Arguments: students (list): The global list of Student instances.

    # Example of how it is used:
    #     1. It prompts the user to enter a student ID.
    #     2. It then finds the corresponding student using the ID.
    #     3. Displays the guardian's full name, contact number, and email by retrieving guardian details for a specific student by ID.
    #     4. It also includes exception Handling that handles invalid inputs, such as non-numeric student IDs and it
    #        Provides feedback if no students are enrolled or if no student is found with the entered ID.

    # if no students are enrolled
    if not students:
        print("\nNo parent/guardian details to display as no students enrolled.\n")
        return
    try:
        # Prompt for a student ID
        student_id = int(input("\nEnter the student ID to view guardian details: "))
    except ValueError:
        print(f"{color5}Invalid input. Please enter a valid numeric student ID.{Style.reset}")
        return

    # Find the student by ID
    # use next() to retrieve first item that matach student id
    student = next((student for student in students if student.student_id == student_id), None)
    
    if student:
        guardian = student.guardian # Retrieve the ParentGuardian instance associated with the student.
        if guardian:
            print(f"\n{color4}Student: {student.full_name} (ID: {student.get_formatted_id()}){Style.reset}")
            print(f"  Guardian Name: {guardian.full_name}")
            print(f"  Contact Number: {guardian.contact_number}")
            print(f"  Contact Email: {guardian.contact_email}\n")
        else:
            print(f"Student: {student.full_name} (ID: {student.get_formatted_id()}) has no associated guardian.\n")
    else:
        print(f"\n{color3}No student found with ID {student_id}.{Style.reset}")
