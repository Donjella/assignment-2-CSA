from classes.person import Person # Internal importing of the Person class to extend its functionality.

class ParentGuardian(Person):
    # Represents a parent or guardian associated with a student. Like the Student class, it inherits from the Person class.
    # This class extends the Person class to include additional attributes and methods specific to guardians, such as contact number and email address.
    # Methods include __init__, get_guardian_fname, get_guardian_lname, get_guardian_contact_number, and get_guardian_contact_email.
    def __init__(self, fname, lname, contact_number, contact_email):
        # Initializes a ParentGuardian instance by extending the attributes of the Person class.
        # Purpose: Sets up a parent or guardian with their name, contact number, and email address.
        # Arguments:
        #   fname (str): The first name of the guardian.
        #   lname (str): The last name of the guardian.
        #   contact_number (str): The contact phone number of the guardian.
        #   contact_email (str): The email address of the guardian.
        # Attributes:
        #   fname, lname (inherited from Person), contact_number, contact_email.
        
        # Example Usage:
        #   guardian = ParentGuardian("Jude", "Bellingham", "1234567890", "judebellingham@coderacademy.edu.au")
        #   print(guardian.contact_number) -> "1234567890"
        super().__init__(fname, lname) # Call the parent class constructor to initialize shared attributes.
        self.contact_number = contact_number
        self.contact_email = contact_email

# Getter methods for guardian details
    def get_guardian_fname(self):
        # Retrieves the first name of the guardian.
        # Purpose: Provides access to the guardian's first name.
        # Returns: str: The first name of the guardian.

        #Example - guardian = ParentGuardian("Jude", "Bellingham", "1234567890", "judebellingham@coderacademy.edu.au")
        # print(guardian.get_guardian_fname()) -> output will be "Jude"
        return self.fname
    
    def get_guardian_lname(self):
        # Retrieves the last name of the guardian.
        # Purpose: Provides access to the guardian's last name.
        # Returns: str: The last name of the guardian.

        #Example - guardian = ParentGuardian("Jude", "Bellingham", "1234567890", "judebellingham@coderacademy.edu.au")
        # print(guardian.get_guardian_lname()) -> output will be "Bellingham"
        return self.lname
    
    def get_guardian_contact_number(self):
        # Retrieves the contact number of the guardian.
        # Purpose: Provides access to the guardian's phone number.
        # Returns: The contact number of the guardian.
        # Example:
        #   guardian = ParentGuardian("Jude", "Bellingham", "1234567890", "judebellingham@coderacademy.edu.au")
        #   print(guardian.get_guardian_contact_number()) -> "1234567890"
        return self.contact_number
    
    def get_guardian_contact_email(self):
           # Retrieves the email address of the guardian.
        # Purpose: Provides access to the guardian's email address.
        # Returns: The email address of the guardian.
        # Example:
        #   guardian = ParentGuardian("Jude", "Bellingham", "1234567890", "judebellingham@coderacademy.edu.au")
        #   print(guardian.get_guardian_contact_email()) -> "judebellingham@coderacademy.edu.au"
        return self.contact_email