from datetime import datetime # Imported to handle date parsing and age calculation.

class Person:
    # Represents a person with attributes such as name, birthday, contact details, and allergies.
    # This class provides methods to calculate the person's age, format their full name, and manage allergies.

    # Methods include __init__, full_name (property), calculate_age, __str__, age_in_years_and_months, and get_allergies.
    def __init__(self, fname, lname, birthday=None, contact_number=None, contact_email=None, allergies=None):
        # Initialises a Person instance with their personal and contact details.
        # Purpose: Sets up a person with attributes for their name, birthday, contact details, and allergies.

        # Arguments:
        #   fname (str): The person's first name.
        #   lname (str): The person's last name.
        #   birthday (str, optional): The person's date of birth in "YYYY-MM-DD" format. Defaults to None.
        #   contact_number (str, optional): The person's contact phone number. Defaults to None.
        #   contact_email (str, optional): The person's email address. Defaults to None.
        #   allergies (list, optional): A list of allergies. Defaults to an empty list if not provided.

        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.contact_number = contact_number
        self.contact_email = contact_email
        self.allergies = allergies if allergies is not None else []

    # With @property, you can access the full name like an attribute (person.full_name) instead of calling it as a method (person.full_name()) with encapsulation.
    # With @property it prevents redundant attributes.

    # Example:
    # person = Person("john", "doe")
    # person.full_name = f"{person.fname} {person.lname}"  # Manual update required on any name change without @property
    # with @property, we can use the following: 
    # person = Person("john", "doe")
    # print(person.full_name) - Automatically updates based on fname and lname without additional logic.
    @property
    def full_name(self):
        
        # Purpose: Combines the first and last name into a properly formatted full name.
        # Returns: (str) the full name of the person with proper capitalization.

        # Example: 
        #   person = Person("Kylian", "Mbappe")
        #   print(person.full_name) -> "Kylian Mbappe"
        return f"{self.fname.capitalize()} {self.lname.capitalize()}"

    def calculate_age(self):
        # Converts a decimal age in years into a string with years and months.
        # Purpose: Provides a more human-readable representation of age.
        # Arguments: age_in_years (float): The age in decimal years (e.g., 2.5 for 2 years and 6 months).
        # Returns: str: The age expressed in years and months.

        # Example:
        #   age_str = Person.age_in_years_and_months(2.5)
        #   print(age_str) -> "2 years and 6 months old"
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age_in_days = (today - birth_date).days
        age_in_years = age_in_days / 365.25  # Convert days to years, including fractions
        return age_in_years

    def __str__(self):
        return f"Name: {self.fname} {self.lname}, Birthday: {self.birthday}, Contact: {self.contact}"

     # The @staticmethod decorator:
        # - Indicates that this method does not operate on an instance of the class or its attributes.
        # - Can be called directly using the class name without instantiating the class.
    @staticmethod
    def age_in_years_and_months(age_in_years):
        # Purpose: Converts a decimal age in years into a string with years and months.
        # Arguments:
        #   age_in_years (float): The age in decimal years (e.g., 2.5 for 2 years and 6 months).
        # Returns: str: The age expressed in years and months.

        # Example:
        #   age_str = Person.age_in_years_and_months(2.5)
        #   print(age_str) -> "2 years and 6 months old"
        """Convert age from decimal years to a string with years and months."""
        years = int(age_in_years)
        months = int((age_in_years - years) * 12)

        if years == 0:
            return f"{months} months old"
        elif months == 0:
            return f"{years} years old"
        else:
            return f"{years} years and {months} months old"

    def get_allergies(self):
        # Retrieves the list of the person's allergies using a gettor method.
        # Purpose: Provides access to the allergies attribute.
        # Returns: list: The person's allergies.

        # Example:
        #   person = Person("John", "Doe", allergies=["Peanuts", "Shellfish"])
        #   print(person.get_allergies()) -> ["Peanuts", "Shellfish"]
        return self.allergies 