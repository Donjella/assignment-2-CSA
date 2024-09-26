import random
from classes.person import Person

# Global set to track used student IDs
used_student_ids = set()

class Student(Person):
    def __init__(self, fname, lname, birthday, allergies=None):
        super().__init__(fname, lname, birthday, allergies=allergies)
        self.student_id = self.generate_unique_id()
        self.classroom = None
        self.guardian = None  # Will hold an instance of ParentGuardian

    def generate_unique_id(self):
        """Generate a unique student ID."""
        # Check if all IDs in the specified range are used
        if len(used_student_ids) >= 2:  # Adjust this number to match your max capacity
            return None

        while True:
            new_id = random.randint(1, 2)  # Adjusted range for 1-2
            if new_id not in used_student_ids:  # Check if the ID is unique
                used_student_ids.add(new_id)    # Add the ID to the set of used IDs
                return new_id
    
     # Getter methods
    def get_student_id(self):
        return self.student_id
    
    def get_fname(self):
        return self.fname
    
    def get_lname(self):
        return self.lname
    
    def get_birthday(self):
        return self.birthday
    
    def get_allergies(self):
        return self.allergies
    
    def get_formatted_id(self):
        """Return the student ID formatted as a two-digit string."""
        return f"{self.student_id:02}"

    def assign_classroom(self, classroom):
        self.classroom = classroom