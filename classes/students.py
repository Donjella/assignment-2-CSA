import random
from classes.person import Person

# Global set to track used student IDs
used_student_ids = set()

class Student(Person):
    def __init__(self, fname, lname, birthday, allergies=None, student_id=None):
        super().__init__(fname, lname, birthday, allergies=allergies)
        if student_id is None:
            self.student_id = self.generate_unique_id()
        else:
            self.student_id = student_id  # Use the provided student ID
        self.classroom = None
        self.guardian = None  # Will hold an instance of ParentGuardian


    def generate_unique_id(self):
        """Generate a unique student ID."""
        # Check if all IDs in the specified range are used
        if len(used_student_ids) >= 100:  # Adjust this number to match student's max capacity
            return None

        while True:
            new_id = random.randint(1, 100)  # Adjusted range for 1-100 to fit 100 unique student ids
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
    
    def get_classroom_name(self):
        return self.classroom.name

    def assign_classroom(self, classroom):
        self.classroom = classroom