from classes.person import Person  # Import the Person class to use the static method
from constants import color3, color4
from colored import Style

def assign_student(classrooms, student, silent=False):
    """Try to assign a student to a valid classroom based on age."""
    age = student.calculate_age()
    
    # Initialize to track if the student is assigned
    assigned = False

    # Try to assign the student to a valid classroom
    for classroom in classrooms:
        if classroom.is_valid_for_age(age):
            classroom.students.append(student)  # Add the student to the classroom's student list
            student.assign_classroom(classroom)  # Assign the classroom to the student
            assigned = True
            
            # Remove this line, as student_id should not be generated again
            # student.student_id = student.generate_unique_id()  

            if not silent:
                formatted_age = Person.age_in_years_and_months(age)
                print(f"\n{student.full_name} (Student ID: {student.get_formatted_id()}) is {formatted_age} and is assigned to {classroom.name}.")
            
            break  # Exit the loop once the student is assigned

    if not assigned:
        # Clear individual attributes
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
    for classroom in classrooms:  # Loop through each classroom
        if classroom.students:  # Check if the classroom has any students
            print(f"\n{color4}Students in {classroom.get_name()}{Style.reset}:")
            for student in classroom.students:  # Loop through each student in the classroom
                age = student.calculate_age()
                formatted_age = Person.age_in_years_and_months(age)  # Use the static method from Person class
                print(f"{student.full_name}, {formatted_age} with student ID {student.get_formatted_id()}")
        else:
            print(f"\n{color4}No students in {classroom.get_name()}.{Style.reset}")

def count_total_students(classrooms):
    """Count the total number of students and print it."""
    total_students = sum(len(classroom.students) for classroom in classrooms)
    print(f"\n{color3}Total number of students: {total_students}{Style.reset}")  


def delete_student(students, classrooms):
    """Delete a student by their student_id, handling input and exceptions internally."""

    try:
        # Ask for student ID to delete and ensure it's an integer
        student_id = int(input("Enter the student ID to delete: "))  # Convert input to int
    except ValueError:
        print("Invalid input. Please enter a valid student ID (integer).")
        return
    except EOFError:
        print("\nInput interrupted. Returning to the previous menu.")
        return
    except Exception as e:  
        print(f"An unexpected error occurred: {e}")
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
        print(f"{student_to_delete.full_name} removed from {classroom_to_delete_from.get_name()}.")

    # Remove the student from the global students list
    students.remove(student_to_delete)
    print(f"Student {student_to_delete.full_name} (ID: {student_to_delete.student_id}) has been deleted.")
