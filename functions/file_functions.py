import json

def save_students(students):
    with open('data/students.json', 'w') as file:
        students_to_save = [
            {
                'student_id': student.student_id,
                'fname': student.fname,
                'lname': student.lname,
                'birthday': student.birthday,
                'contact': student.contact,
                'allergies': student.allergies,
            }
            for student in students
        ]
        json.dump(students_to_save, file, indent=4)
