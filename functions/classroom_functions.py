# classroom_functions.py
from classes.classrooms import classrooms

def assign_student(classroom, student):
    """Assign a student to the classroom if they meet the age criteria."""
    age = student.calculate_age()
    if classroom.is_valid_for_age(age):
        classroom.students.append(student)
        student.assign_classroom(classroom)  # Call student's method to assign the classroom
        print(f"{student.name} (student id: {student.student_id}) is {age:.2f} years old and is assigned to {classroom.name}.")
        return True
    else:
        print(f"{student.name}, {age:.2f} years old cannot be added to {classroom.name} due to age restriction.")
        return False