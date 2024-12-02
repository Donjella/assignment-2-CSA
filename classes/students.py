import random  # An external library used to generate random numbers for unique student IDs.

from classes.person import Person  # Internally importing the Person class for inheritance.

# Global set to track used student IDs - this ensures that all generated student IDs are unique across the application.
used_student_ids = set()

class Student(Person):
    # Represents a student with attributes such as name, birthday, allergies, student ID, and classroom. Like the ParentGuardian class, it inherits from the Person class.
    # This class extends the Person class to include additional attributes and methods specific to students, 
    # such as student ID generation, classroom assignment, and retrieving guardian information.
    # Methods include __init__, generate_unique_id, and various getter methods.

    def __init__(self, fname, lname, birthday, allergies=None, student_id=None):
        # Initializes a Student instance by extending the attributes of the Person class.
        # Purpose: Sets up a student with attributes for name, birthday, allergies, student ID, classroom, and guardian.
        # Arguments:
        #   fname (str): The first name of the student.
        #   lname (str): The last name of the student.
        #   birthday (str): The student's date of birth in "YYYY-MM-DD" format.
        #   allergies (list, optional): A list of the student's allergies. Defaults to None.
        #   student_id (int, optional): A unique student ID. If None, a new ID is generated. Defaults to None.
        # Attributes:
        #   fname, lname, birthday, allergies (inherited from Person), student_id, classroom, guardian.

        # Example:
        #   student = Student("John", "Doe", "2010-05-15", allergies=["Peanuts"])
        #   print(student.student_id) -> A unique ID (e.g., 42).

        super().__init__(fname, lname, birthday, allergies=allergies)
        if student_id is None:
            self.student_id = self.generate_unique_id() # Generate a unique ID if none is provided.
        else:
            self.student_id = student_id  # Use the provided student ID
        self.classroom = None # Will store the assigned classroom (if any).
        self.guardian = None  # Will hold an instance of ParentGuardian


    def generate_unique_id(self):
        # Generates a unique student ID within a specified range.
        # Purpose: Ensures that each student has a unique identifier.
        # Returns: int or None: A unique ID or None if the maximum capacity is reached. i.e. when IDs between 1 and 100 are all in use.

        # Example Usage:
        #   student_id = student.generate_unique_id()
        #   print(student_id) -> A unique ID (e.g., 15).

        # Implementation Details:
        #   - IDs are integers between 1 and 100 (adjustable as needed).
        #   - Tracks used IDs with the global set `used_student_ids`.
        #   - Check if all IDs in the specified range are used

        if len(used_student_ids) >= 100:  # Adjust this number to match student's max capacity
            return None

        while True:
            new_id = random.randint(1, 100)  # Adjusted range for 1-100 to fit 100 unique student ids
            if new_id not in used_student_ids:  # Check if the ID is unique
                used_student_ids.add(new_id)    # Add the ID to the set of used IDs
                return new_id
    
    # Getter methods

    def get_student_id(self):
        # Retrieves the student's unique ID.
        # Returns: int: The student's unique ID.
        return self.student_id

    def get_fname(self):
        # Retrieves the first name of the student.
        # Returns: str: The student's first name.
        return self.fname

    def get_lname(self):
        # Retrieves the last name of the student.
        # Returns: str: The student's last name.
        return self.lname

    def get_birthday(self):
        # Retrieves the student's date of birth.
        # Returns: str: The student's birthday in "YYYY-MM-DD" format.
        return self.birthday

    def get_allergies(self):
        # Retrieves the list of the student's allergies.
        # Returns: list: The student's allergies.
        return self.allergies

    def get_formatted_id(self):
    
        # Purpose: Provides a consistent format for displaying student IDs.
        # Returns: str: The student ID formatted as "XX". i.e returns the student ID formatted as a two-digit string.

        # Example:
        #   student_id = student.get_formatted_id()
        #   print(student_id) -> "05" (if the ID is 5).
        return f"{self.student_id:02}"

    def get_classroom_name(self):
        # Retrieves the name of the classroom assigned to the student.
        # Returns: str: The name of the assigned classroom.

        # Example:
        #   student.assign_classroom(classroom)
        #   print(student.get_classroom_name()) -> "Babies Room".
        return self.classroom.name

    def assign_classroom(self, classroom):
        # Assigns the student to a specific classroom.
        # Purpose: Links the student with a classroom instance.
        # Arguments:
        #   classroom (Classroom): The classroom to assign the student to.

        # Example:
        #   student.assign_classroom(babies_classroom)
        #   print(student.classroom.name) -> "Babies Room".
        self.classroom = classroom