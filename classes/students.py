import random
from classes.person import Person

# Global set to track used student IDs
used_student_ids = set()

class Student(Person):
    def __init__(self, name, birthday, contact, fees=0):
        super().__init__(name, birthday, contact)
        self.student_id = self.generate_unique_id()
        self.fees = fees
        self.classroom = None

    def generate_unique_id(self):
        """Generate a unique student ID."""
        while True:
            new_id = random.randint(10, 99)
            if new_id not in used_student_ids:  # Check if the ID is unique
                used_student_ids.add(new_id)    # Add the ID to the set of used IDs
                return new_id

    def assign_classroom(self, classroom):
        self.classroom = classroom