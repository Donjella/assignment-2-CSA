class Kitchen:
    def __init__(self):
        # Initialize a dictionary to hold the menu for each day of the week
        self.menu = {
            "Monday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Tuesday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Wednesday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Thursday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Friday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Saturday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
            "Sunday": {"Breakfast": [], "Lunch": [], "Afternoon Tea": []},
        }

    def add_menu(self, day, meal_type, dish):
        """Add a dish to the specified meal type for the given day."""
        if day in self.menu:
            if meal_type in self.menu[day]:
                self.menu[day][meal_type].append(dish)
                print(f"{dish} has been added to {meal_type} for {day}.")
            else:
                print(f"Invalid meal type: {meal_type}. Please enter 'breakfast', 'lunch', or 'afternoon_tea'.")
        else:
            print(f"Invalid day: {day}. Please enter a valid day of the week.")

    def list_menu(self):
        """List the menu for every day of the week."""
        for day, meals in self.menu.items():
            print(f"\nMenu for {day}:")
            for meal_type, dishes in meals.items():
                if dishes:
                    print(f"{meal_type.title()}: {', '.join(dishes)}")
                else:
                    print(f"{meal_type.title()}: No dishes set.")
