# In parent_guardian.py
from classes.person import Person

class ParentGuardian(Person):
    def __init__(self, fname, lname, contact_number, contact_email):
        # Initialize fname and lname using Person's constructor
        super().__init__(fname, lname, birthday=None, contact_number=contact_number, contact_email=contact_email)
