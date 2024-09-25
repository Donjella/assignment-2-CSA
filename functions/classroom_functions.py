# classroom_functions.py
from classes.classrooms import classrooms, students

def assign_student(classrooms, student):
    """Try to assign a student to a valid classroom based on age."""
    age = student.calculate_age()
    assigned = False  # Track if the student is assigned to a classroom

    # Try to assign the student to a valid classroom
    for classroom in classrooms:
        if classroom.is_valid_for_age(age):
            classroom.students.append(student)  # Add the student to the classroom's student list
            student.assign_classroom(classroom)  # Assign the classroom to the student
            print(f"{student.full_name} (Student ID: {student.student_id}) is {age:.2f} years old and is assigned to {classroom.name}.")
            assigned = True
            break  # Exit the loop once the student is assigned

    # If the student couldn't be assigned to any classroom
    if not assigned:
        print(f"{student.full_name}, {age:.2f} years old cannot be added to any classroom due to age restriction.")


def list_students_by_classroom(classrooms):
    for classroom in classrooms:  # Loop through each classroom
        if classroom.students:  # Check if the classroom has any students
            print(f"\nStudents in {classroom.get_name()}:")
            for student in classroom.students:  # Loop through each student in the classroom
                age = student.calculate_age()
                print(f"{student.full_name}, {age:.2f} years old with student ID {student.student_id}")
        else:
            print(f"\nNo students in {classroom.get_name()}.")



def delete_student(students, classrooms):
    """Delete a student by their student_id, handling input and exceptions internally."""

    try:
        # Ask for student ID to delete and ensure it's an integer
        student_id = int(input("Enter the student ID to delete: "))  # Convert input to int
    except ValueError:
        print("Invalid input. Please enter a valid student ID (integer).")
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
