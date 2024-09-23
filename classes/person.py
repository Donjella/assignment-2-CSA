class Person:
    def __init__(self, name, birthday, contact):
        self.name = name
        self.birthday = birthday  # Store as a string "YYYY-MM-DD"
        self.contact = contact

    def calculate_age(self):
        from datetime import datetime
        birth_date = datetime.strptime(self.birthday, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age