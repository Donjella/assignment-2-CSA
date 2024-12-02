class Kitchen:
    # Represents a kitchen responsible for managing menus for different days and weeks.
    # This class provides methods to add, update, list, and delete menus for specific days and weeks.
    # It uses a nested dictionary structure to organize menu items for breakfast, lunch, and afternoon tea.
    # It includes the following methods __init__, add_menu, list_menu, and delete_menu

    def __init__(self):
        # Initialise a dictionary to hold the menu for each week and each day of the week
        # Purpose: Sets up a structure to store menus for each week and day.
        # Attributes: menu (dict): A nested dictionary to store menus, organized by week and day.
        # Example structure:
        # {
        #     week_number: {
        #         day_name: {
        #             "Breakfast": str, 
        #             "Lunch": str, 
        #             "Afternoon Tea": str
        #         }
        #     }
        # }
        self.menu = {}

    def add_menu(self, week, day, breakfast, lunch, afternoon_tea): 
        # Adds or updates the menu for a specific day and week.
        # Purpose: Allows setting the menu for breakfast, lunch, and afternoon tea for a given day.
        # Arguments:
        #   week (int): The week number (e.g., 1 for Week 1).
        #   day (str): The day of the week (e.g., "Monday").
        #   breakfast (str): The breakfast dish for the day.
        #   lunch (str): The lunch dish for the day.
        #   afternoon_tea (str): The afternoon tea dish for the day.

        # Example:
        #   kitchen.add_menu(1, "Monday", "Pancakes", "Spaghetti", "Fruit Salad")
        #   Adds a menu for Week 1, Monday with the given meals.

        # This if statement below ensures the week exists in the menu dictionary.
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

        # Set/update the dish for each meal (breakfast, lunch, and afternoon tea)
        self.menu[week][day]["Breakfast"] = breakfast
        self.menu[week][day]["Lunch"] = lunch
        self.menu[week][day]["Afternoon Tea"] = afternoon_tea

        print(f"Menu for {day} in Week {week} has been updated.\n")

    def list_menu(self):
        # Lists all menus for each week and day.
        # Purpose: Displays the menu for all weeks and days in a readable format.
        
        # Example:
        #   kitchen.list_menu()
        #   Output:
        #   --- Menu for Week 1 ---
        #   Menu for Monday:
        #     Breakfast: Pancakes
        #     Lunch: Spaghetti
        #     Afternoon Tea: Fruit Salad
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
        # Deletes the menu for a specific day in a specific week.
        # Purpose: Removes all menu items for a specified day, resetting them to None.
        # Arguments:
        #   week (int): The week number.
        #   day (str): The day of the week (e.g., "Monday").

        # Example:
        #   kitchen.delete_menu(1, "Monday")
        #   Removes the menu for Monday in Week 1, resetting all meals to None
        if week in self.menu and day in self.menu[week]:
            self.menu[week][day] = {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
            print(f"Menu for {day} in Week {week} has been deleted.")
        else:
            print(f"Invalid day or week: {day} in Week {week}. Please enter a valid day and week.")
