class Kitchen:
    def __init__(self):
        # Initialize a dictionary to hold the menu for each day of the week
        self.menu = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": []
        }

    def add_menu(self, day, dishes):
            """Add a list of dishes to the menu for the given day."""
            if day in self.menu:
                self.menu[day] = dishes
                print(f"Menu for {day} has been updated.")
            else:
                print(f"Invalid day: {day}. Please enter a valid day of the week.")

    def list_menu(self, day):
        """List the menu for the given day."""
        if day in self.menu:
            if not self.menu[day]:
                print(f"No menu set for {day}.")
            else:
                print(f"Menu for {day}: {', '.join(self.menu[day])}")
        else:
            print(f"Invalid day: {day}. Please enter a valid day of the week.")