import pytest
from functions.student_functions import add_student
from classes.classrooms import Classroom


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
    # Mock 'inputs' for the student details and follows all validation from actual add student_function
    mocker.patch('builtins.input', side_effect=[
        'Kylian',      # First name
        'Mbappe',     # Last name
        '2023-01-01', # Birthday
        'yes',        # Yes for question asking for any allergies
        'Peanut',     # Input allergy
        'yes',         # yes when asking for any more allergies
        'Dairy',       # Input allergy
        'no',          # no when asking for any more allergies
        'Mary',       # Guardian's first name
        'Lamb',       # Guardian's last name
        '0406346693',  # Guardian's contact number - needs to be 
        'mary@example.com'  # Guardian's contact email
    ])
    
    # Call `add_student`
    add_student(students, classrooms)
    
    # Check that the student has been added (matching the input above to pass)
    assert len(students) == 1 # test that student is added to students list
    assert students[0].get_fname() == 'Kylian'
    assert students[0].guardian.get_guardian_contact_email() == 'mary@example.com'
    assert students[0].get_allergies() == ['Peanut', 'Dairy']