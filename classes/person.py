from datetime import datetime

class Person:
    def __init__(self, fname, lname, birthday, contact, allergies=None):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.contact = contact
        self.allergies = allergies if allergies is not None else []  # Default to an empty list if no allergies provided

    @property
    def full_name(self):
        """Return the full name with proper capitalization."""
        return f"{self.fname.capitalize()} {self.lname.capitalize()}"

    def calculate_age(self):
        """Calculate age in years, including fractions of months."""
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age_in_days = (today - birth_date).days
        age_in_years = age_in_days / 365.25  # Convert days to years, including fractions
        return age_in_years

    def __str__(self):
        return f"Name: {self.fname} {self.lname}, Birthday: {self.birthday}, Contact: {self.contact}"

    @staticmethod
    def age_in_years_and_months(age_in_years):
        """Convert age from decimal years to a string with years and months."""
        years = int(age_in_years)
        months = int((age_in_years - years) * 12)

        if years == 0:
            return f"{months} months old"
        elif months == 0:
            return f"{years} years old"
        else:
            return f"{years} years and {months} months old"
