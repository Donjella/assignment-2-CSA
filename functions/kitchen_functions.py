def add_menu_for_day(kitchen):
    """Prompt the user to add a menu for a specific day."""
    day = input("Enter the day of the week: ").capitalize()
    dishes = input("Enter the dish for the day")
    kitchen.add_menu(day, [dish.strip() for dish in dishes])

def list_menu_for_day(kitchen):
    """Prompt the user to list the menu for a specific day."""
    day = input("Enter the day of the week: ").capitalize()
    kitchen.list_menu(day)