from classes.person import Person

class ParentGuardian(Person):
    def __init__(self, fname, lname, contact_number, contact_email):
        super().__init__(fname, lname)
        self.contact_number = contact_number
        self.contact_email = contact_email
