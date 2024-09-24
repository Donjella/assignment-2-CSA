class Classroom:
    def __init__(self, name, min_age, max_age):
        self.name = name
        self.min_age = min_age
        self.max_age = max_age
        self.students = []

    def is_valid_for_age(self, age):
        return self.min_age <= age < self.max_age

    def get_name(self):
        return self.name

# Global list of students
students = []

# Initialize the classrooms
babies_classroom = Classroom("Babies Room (0-2 years)", 0, 2)
toddlers_classroom = Classroom("Toddlers Room(2-3 years)", 2, 3)
kindergarten_classroom = Classroom("Kindergarten Room(3-5 years)", 3, 5)

# List of classrooms
classrooms = [babies_classroom, toddlers_classroom, kindergarten_classroom]