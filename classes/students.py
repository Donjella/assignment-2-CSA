import random
from classes.person import Person

# Global set to track used student IDs
used_student_ids = set()

class Student(Person):
    def __init__(self, fname, lname, birthday, contact, allergies = None):
        super().__init__(fname, lname, birthday, contact, allergies)
        self.student_id = self.generate_unique_id()
        self.classroom = None

    def generate_unique_id(self):
        while True:
            new_id = random.randint(1, 10)  # Adjusted range for 1-100
            if new_id not in used_student_ids:  # Check if the ID is unique
                used_student_ids.add(new_id)    # Add the ID to the set of used IDs
                return new_id

    def get_formatted_id(self):
        """Return the student ID formatted as a two-digit string."""
        return f"{self.student_id:02}"

    def assign_classroom(self, classroom):
        self.classroom = classroom