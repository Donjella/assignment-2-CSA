import random
from classes.person import Person

class Student(Person):
    def __init__(self, name, birthday, contact, fees=0):
        super().__init__(name, birthday, contact)  # Inherit from Person
        self.student_id = random.randint(10, 99)  # Random 2-digit student ID
        self.fees = fees
        self.classroom = None