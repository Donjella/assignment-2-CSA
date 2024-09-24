from datetime import datetime

class Person:
    def __init__(self, fname, lname, birthday, contact):
        self.fname = fname
        self.lname = lname
        self.birthday = birthday
        self.contact = contact
        
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
        return f"Name: {self.fname}{self.lname}, Birthday: {self.birthday}, Contact: {self.contact}"