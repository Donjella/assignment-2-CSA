class Classroom:
    # Represents a classroom with a specific name, age range, and a list of enrolled students.
    # This class is used to define a classroom and manage students within a specified age range.
    # It provides methods to validate if a student's age falls within the classroom's range and to retrieve the classroom's name.

    # method includes __init__, is_valid_for_age and get_name
    
    def __init__(self, name, min_age, max_age):
        # Initialises the classroom with its name, age range, and an empty student list.
        self.name = name # name (str): The name of the classroom.
        self.min_age = min_age # The (int) minimum age (inclusive) for students in this classroom.
        self.max_age = max_age # The (int) maximum age (inclusive) for students in this classroom.
        self.students = [] # students (list): A list to store students assigned to this classroom.

    def is_valid_for_age(self, age):
        # Checks if a given age falls within the classroom's age range.
        # Purpose: Validates whether a student's age falls within the classroom's age range.
        # Arguments: age (int): The student's age.
        # Returns -  bool: True if the age is within the classroom's range, False otherwise.

        # Example: if classroom.is_valid_for_age(student.age) -> classroom.students.append(student) 
        # i.e. If the student's age is valid for the classroom, add them to the classroom's list of students.
        return self.min_age <= age < self.max_age

    def get_name(self):
        # Retrieve the name of the classroom.
        # Purpose: Provides the name of the classroom for display or reference.
        # Returns - str: The name of the classroom.

        # Example: print(classroom.get_name()) -> Output: "Babies Room (0-2 years)
        return self.name

# Global list of students
# Purpose: This list is used to store all student instances in the application. 
# Students can be assigned to a classroom based on their age, and this global list ensures they can be accessed from various parts of the application.
students = []

# Initialize the classrooms
# Purpose: These instances represent predefined classrooms categorized by age range. 
# Students will be assigned to these classrooms automatically based on their age.
babies_classroom = Classroom("Babies Room (0-2 years)", 0, 2)
toddlers_classroom = Classroom("Toddlers Room(2-3 years)", 2, 3)
kindergarten_classroom = Classroom("Kindergarten Room(3-5 years)", 3, 5)

# List of classrooms
# Purpose: This list contains all classroom instances. 
# It is used to iterate through classrooms when assigning students or retrieving information about specific classrooms.

# Example Usage - Assign a student to a classroom based on age:
# for student in students:
#     for classroom in classrooms:
#         if classroom.is_valid_for_age(student.age):
#             classroom.students.append(student)
#             break
classrooms = [babies_classroom, toddlers_classroom, kindergarten_classroom]