import json
from classes.students import Student  # Import the Student class
from functions.classroom_functions import assign_student  
from classes.parent_guardian import ParentGuardian


def save_students(students):
    with open('data/students.json', 'w') as file:
        students_to_save = [
            {
                'student_id': student.get_student_id(),
                'fname': student.get_fname(),
                'lname': student.get_lname(),
                'birthday': student.get_birthday(),
                'allergies': student.get_allergies(),
                # Access guardian details through the guardian attribute
                'guardian': {
                    'fname': student.guardian.get_guardian_fname(),
                    'lname': student.guardian.get_guardian_lname(),
                    'contact_number': student.guardian.get_guardian_contact_number(),
                    'contact_email': student.guardian.get_guardian_contact_email()
                }
            }
            for student in students
        ]
        json.dump(students_to_save, file, indent=4)


def load_students(students, classrooms):
    """Load student data from a JSON file and populate the students list."""
    try:
        with open('data/students.json', 'r') as file:
            students_data = json.load(file)
            for student_dict in students_data:
                # Recreate ParentGuardian object from the loaded data
                guardian_dict = student_dict.get('guardian', {})
                guardian = ParentGuardian(
                    fname=guardian_dict.get('fname'),
                    lname=guardian_dict.get('lname'),
                    contact_number=guardian_dict.get('contact_number'),
                    contact_email=guardian_dict.get('contact_email')
                )
                # Recreate Student object from the loaded data
                student = Student(
                    fname=student_dict['fname'],
                    lname=student_dict['lname'],
                    birthday=student_dict['birthday'],
                    allergies=student_dict.get('allergies', [])
                )
            
                student.student_id = student_dict['student_id']  # Restore the student ID
                student.guardian = guardian  # Associate the guardian with the student
                
                students.append(student)
                
                # Assign the student to the correct classroom based on age
                # using silent=True to not print assigned list of students on startup
                assign_student(classrooms, student, silent=True)

    except FileNotFoundError:
        print("No previous student data found. Starting fresh.")
    except Exception as e:
        print(f"An error occurred while loading students: {e}")



# Start of kitchen file functions

def save_menu(kitchen):
    """Save the kitchen menu to a JSON file."""
    with open('data/kitchen.json', 'w') as file:
        json.dump(kitchen.menu, file, indent=4)
    print("Menu saved successfully.")


def load_menu(kitchen):
    """Load the kitchen menu from a JSON file."""
    try:
        with open('data/kitchen.json', 'r') as file:
            loaded_menu = json.load(file)

        # Use integer keys for mapping back to day names
        day_map = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
        kitchen.menu = {}
        
        for week, days in loaded_menu.items():
            kitchen.menu[week] = {}
            for day, meals in days.items():
                # Use the correct day mapping
                kitchen.menu[week][day] = meals

        print("Menu loaded successfully.")
        
    except FileNotFoundError:
        print("No saved menu found. Starting with an empty menu.")
