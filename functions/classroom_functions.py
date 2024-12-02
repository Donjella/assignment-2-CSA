from prettytable import PrettyTable  # External library used to display tabular data. E.g. list students by classrooms in individual tables
from colored import Style, stylize, attr, fg  # External library for colored text styling.

from classes.person import Person  # Import the Person class for shared methods like age formatting.
from constants import color3, color4, color5  # Imported constants for consistent colored output.

def assign_student(classrooms, student, silent=False):
    # Assign a student to a valid classroom based on their age.

    # Purpose:
    #   Loops through available classrooms to find a match for the student's age range.
    #   If a match is found, the student is assigned to the classroom.
    #   If no match is found, the student's details are cleared.

    # Arguments:
    #   classrooms (list): A list of Classroom instances.
    #   student (Student): The student instance to be assigned.
    #   silent (bool, optional): silent argument in the assign_student function suppresses the output messages 
    #   and help not to assign student id again when it loads from load_students function in file_functions.py
    #   that inform about the success or failure of assigning a student to a classroom. Default is False.

    # Example Usage:
    #   assign_student(classrooms, student)
    #   Assigns the student to a classroom based on their age.

    age = student.calculate_age() # Calculate the student's age in years, including fractional months, using the `calculate_age` method from the Person class.

    
    # Initialize to track if the student is assigned
    assigned = False

    # Try to assign the student to a valid classroom
    for classroom in classrooms:
        if classroom.is_valid_for_age(age):
            classroom.students.append(student)  # Add the student to the classroom's student list
            student.assign_classroom(classroom)  # Assign the classroom to the student
            assigned = True
            # If silent mode is not enabled, provide user feedback with output below
            if not silent:
                # Format the student's age as a user-friendly string (e.g., "3 years and 2 months old")
                formatted_age = Person.age_in_years_and_months(age)
                print(f"\n{color3}{student.full_name} (Student ID: {student.get_formatted_id()}) is {formatted_age} and is assigned to {classroom.name}.{Style.reset}")
            
            break  # Exit the loop once the student is assigned

    if not assigned:
        # Clear student details if no classroom is suitable
        student.fname = None
        student.lname = None
        student.birthday = None
        student.allergies = []
        student.guardian = None

        if not silent:
            formatted_age = Person.age_in_years_and_months(age)
            if student.fname and student.lname:
                print(f"{student.full_name}, {formatted_age} cannot be added to any classroom due to age restriction. Therefore, they are not enrolled.")
            else:
                print(f"Student of age: {formatted_age} cannot be added to any classroom due to age restriction. Therefore, they are not enrolled.")


def list_students_by_classroom(classrooms):
    # Display a list of students for each classroom in a tabular format.
    # Purpose: Iterates through classrooms and lists enrolled students, including their full names, IDs, and formatted ages.
    # Arguments: classrooms (list): A list of Classroom instances.

    # Example: list_students_by_classroom(classrooms) results in the output of tables of students grouped by classroom.
    for classroom in classrooms:
        if classroom.students:  # Check if the classroom has any students
            # Initialize the table for the specific classroom
            table = PrettyTable()

            # Bold and style headers for table
            header_color = fg("blue") + attr("bold")
            header_student_name_id = stylize("Student Name (Student ID)", header_color)
            header_age = stylize("Age", header_color)

            # Apply green color for table lines
            table.horizontal_char = stylize("-", fg("spring_green_4"))
            table.junction_char = stylize("+", fg("spring_green_4"))
            table.vertical_char = stylize("|", fg("spring_green_4"))

            table.field_names = [header_student_name_id, header_age]

            for student in classroom.students:  # Loop through each student in the classroom
                age = student.calculate_age()
                formatted_age = Person.age_in_years_and_months(age)  # Use the static method from Person class
                name_id = f"{student.full_name} (ID: {student.get_formatted_id()})"

                # Add row to the table
                table.add_row([name_id, formatted_age])

            # Print the table for the current classroom
            print(f"\n{color3}Students in {classroom.get_name()}:{Style.reset}")
            print(table)
        else:
            # If no students in the classroom, print a message
            print(f"\n{color4}No students in {classroom.get_name()}.{Style.reset}")


def count_total_students(classrooms):
    # Count and print the total number of students across all classrooms.
    # Purpose: Calculates and displays the total number of enrolled students.
    # Arguments: classrooms (list): A list of Classroom instances.

    # Output will print the total number of students in the childcare across all classrooms.
    total_students = sum(len(classroom.students) for classroom in classrooms)
    print(f"\n{color3}Total number of students: {total_students}{Style.reset}")  


def delete_student(students, classrooms):
    # Delete a student by their student ID.
    # Purpose: Prompts the user for a student ID and removes the corresponding student from their assigned classroom and the global student list.

    # Arguments:
    #    1. students (list): A list of all Student instances.
    #    2. classrooms (list): A list of all Classroom instances.

    try:
        # Ask for student ID to delete and ensure it's an integer
        student_id = int(input("Enter the student ID to delete: "))  # Convert input to int
    except ValueError:
        print(f"{color5}Invalid input. Please enter a valid student ID (integer).{Style.reset}")
        return
    except EOFError:
        print(f"\n{color5}Input interrupted. Returning to the previous menu.{Style.reset}")
        return
    except Exception as e:  
        print(f"{color5}An unexpected error occurred: {e}{Style.reset}")
        return
    
    # Find the student in the classrooms' students list
    student_to_delete = None
    classroom_to_delete_from = None

    # Loop through each classroom to find the student
    for classroom in classrooms:
        for student in classroom.students:
            if student.student_id == student_id:  # Ensure comparison is between integers
                student_to_delete = student
                classroom_to_delete_from = classroom
                break  # Exit inner loop once the student is found
        if student_to_delete:
            break  # Exit outer loop once the student is found
    
    if not student_to_delete:
        print(f"Student with ID {student_id} not found.")
        return
    
    # Remove the student from the classroom they are assigned to
    if classroom_to_delete_from:
        classroom_to_delete_from.students.remove(student_to_delete)
        print(f"\n{color3}{student_to_delete.full_name} removed from {classroom_to_delete_from.get_name()}.{Style.reset}")

    # Remove the student from the global students list
    students.remove(student_to_delete)
    print(f"{color3}{student_to_delete.full_name} (student ID: {student_to_delete.student_id}) has been deleted from the system.{Style.reset}")
