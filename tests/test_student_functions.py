import pytest
from functions.student_functions import add_student
from classes.classrooms import Classroom
from classes.parent_guardian import ParentGuardian


@pytest.fixture
def classrooms():
    return [
        Classroom("Babies Room (0-2 years)", 0, 2),
        Classroom("Toddlers Room (2-3 years)", 2, 3),
        Classroom("Kindergarten Room (3-5 years)", 3, 5)
    ]

@pytest.fixture
def students():
    return []

def test_add_student(mocker, students, classrooms):
    # Mock 'inputs' for the student details 
    mocker.patch('builtins.input', side_effect=[
        'Simon',      # First name
        'Cowell',       # Last name
        '2023-01-01', # Birthday
        'no',        # No allergies
        'Mary',      # Guardian's first name
        'Lamb',       # Guardian's last name
        '123456789', # Guardian's contact number
        'mary@example.com'  # Guardian's contact email
    ])
    
    # Call `add_student`
    add_student(students, classrooms)
    
    # Check that the student has been added (matching the input above to pass)
    assert len(students) == 1 #test that student is added to students list
    assert students[0].get_fname() == 'Simon'
    assert students[0].guardian.get_guardian_contact_email() == 'mary@example.com'
