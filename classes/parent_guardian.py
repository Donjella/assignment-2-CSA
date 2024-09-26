from classes.person import Person

class ParentGuardian(Person):
    def __init__(self, fname, lname, contact_number, contact_email):
        super().__init__(fname, lname)
        self.contact_number = contact_number
        self.contact_email = contact_email

# Getter methods for guardian details
    def get_guardian_fname(self):
        return self.fname
    
    def get_guardian_lname(self):
        return self.lname
    
    def get_guardian_contact_number(self):
        return self.contact_number
    
    def get_guardian_contact_email(self):
        return self.contact_email