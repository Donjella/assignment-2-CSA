def add_menu_for_day(kitchen):
    """Prompt the user to add or update the menu for breakfast, lunch, and afternoon tea for a specific day."""
    week = input("Enter the week number: ")
    day = input("Enter the day of the week: ").capitalize()

    # Ask the user to input dishes for each meal
    breakfast = input("Enter the breakfast dish: ").strip().title()
    lunch = input("Enter the lunch dish: ").strip().title()
    afternoon_tea = input("Enter the afternoon tea dish: ").strip().title()

    # Add each dish to the respective meal
    kitchen.add_menu(week, day, breakfast, lunch, afternoon_tea)


def list_menu_for_day(kitchen):
    """Prompt the user to list the menu for a specific week and day."""
    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print("Invalid input. Please enter a valid week number (integer).")
        return

    day = input("Enter the day of the week: ").capitalize()

    if week in kitchen.menu and day in kitchen.menu[week]:
        menu_for_day = kitchen.menu[week][day]
        print(f"\nMenu for {day} (Week {week}):")
        print(f"  Breakfast: {menu_for_day['Breakfast'] or 'No dishes set.'}")
        print(f"  Lunch: {menu_for_day['Lunch'] or 'No dishes set.'}")
        print(f"  Afternoon Tea: {menu_for_day['Afternoon Tea'] or 'No dishes set.'}")
    else:
        print(f"No menu found for {day} (Week {week}).\n")

def list_students_with_allergies(students):
    """List all students with allergies."""
    students_with_allergies = [student for student in students if student.allergies]
    
    if not students_with_allergies:
        print("No students with allergies.\n")
    else:
        print("\nStudents with allergies:")
        for student in students_with_allergies:
            allergies = ', '.join(student.allergies)
            print(f"{student.full_name} (Student ID: {student.student_id}) has the following allergies: {allergies}\n")

def delete_menu_for_day(kitchen):
    """Prompt the user to delete the menu for a specific week and day."""
    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print("Invalid input. Please enter a valid week number (integer).")
        return

    day = input("Enter the day of the week: ").capitalize()

    if week in kitchen.menu and day in kitchen.menu[week]:
        kitchen.menu[week][day] = {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
        print(f"Menu for {day} (Week {week}) has been deleted.\n")
    else:
        print(f"No menu found for {day} (Week {week}).\n")