class Kitchen:
    def __init__(self):
        # Initialize a dictionary to hold the menu for each week and each day of the week
        self.menu = {}

    def add_menu(self, week, day, breakfast, lunch, afternoon_tea):
        """Add or update the menu for breakfast, lunch, and afternoon tea for a given day and week."""
        # Ensure the week number is in the menu dictionary
        if week not in self.menu:
            self.menu[week] = {
                "Monday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Tuesday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Wednesday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Thursday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Friday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Saturday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
                "Sunday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
            }

        # Set the dish for each meal (breakfast, lunch, and afternoon tea)
        self.menu[week][day]["Breakfast"] = breakfast
        self.menu[week][day]["Lunch"] = lunch
        self.menu[week][day]["Afternoon Tea"] = afternoon_tea

        print(f"Menu for {day} in Week {week} has been updated.\n")

    def list_menu(self):
        """List the menu for every week and day."""
        for week, days in self.menu.items():
            print(f"\n--- Menu for Week {week} ---")
            for day, meals in days.items():
                print(f"\nMenu for {day}:")
                for meal_type, dish in meals.items():
                    if dish:
                        print(f"  {meal_type}: {dish}")
                    else:
                        print(f"  {meal_type}: No dishes set.")

    def delete_menu(self, week, day):
        """Delete the menu for a specific day in a week."""
        if week in self.menu and day in self.menu[week]:
            self.menu[week][day] = {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
            print(f"Menu for {day} in Week {week} has been deleted.")
        else:
            print(f"Invalid day or week: {day} in Week {week}. Please enter a valid day and week.")
