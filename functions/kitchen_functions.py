def add_menu_for_day(kitchen):
    """Prompt the user to add or update the menu for breakfast, lunch, and afternoon tea for a specific day."""
    try:
        # Prompt for week number
        week_input = input("Enter the week number (1-52): ").strip()
        if not week_input:
            raise ValueError("Week number cannot be empty.")
        week = int(week_input)

        # Ensure week is within valid range (1-52)
        if week < 1 or week > 52:
            raise ValueError("Please enter a valid week number between 1 and 52.\n")

        # Day mapping
        day_map = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
        
        # Prompt for day of the week
        day_input = input("Enter the day of the week (1 = Monday,..,5 = Friday): ").strip()
        if not day_input:
            raise ValueError("Day cannot be empty.\n")
        day = int(day_input)
        
        if day not in day_map:
            raise ValueError("Please enter a number between 1 and 5 (weekdays only).\n")
        day = day_map[day]

        print(f"Adding menu for Week {week}, Day: {day}")

    except ValueError as error:
        print(f"{error}")
        return  
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return
    except Exception as e:
        print("\nAn unexpected error occurred")
        return

    # Ask the user to input dishes for each meal
    try:
        breakfast = input("Enter the breakfast dish: ").strip().title()
        lunch = input("Enter the lunch dish: ").strip().title()
        afternoon_tea = input("Enter the afternoon tea dish: ").strip().title()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return
    except Exception as e:
        print("\nAn unexpected error occurred")
        return

    week_str = str(week)
    if week_str not in kitchen.menu:
        kitchen.menu[week_str] = {
            "Monday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
            "Tuesday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
            "Wednesday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
            "Thursday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None},
            "Friday": {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
        }

    kitchen.menu[week_str][day]["Breakfast"] = breakfast
    kitchen.menu[week_str][day]["Lunch"] = lunch
    kitchen.menu[week_str][day]["Afternoon Tea"] = afternoon_tea

    print(f"Menu for {day} in Week {week} has been updated.\n")

def list_menu_for_week(kitchen):
    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print("Invalid input. Please enter a valid week number (integer).")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return
    except Exception as e:
        print("\nAn unexpected error occurred")
        return

    week_str = str(week)

    if week_str not in kitchen.menu:
        print(f"No menu found for Week {week}.\n")
        return

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print(f"\n--- Menu for Week {week} ---")

    for day in days_of_week:
        if day in kitchen.menu[week_str]:
            menu_for_day = kitchen.menu[week_str][day]
            print(f"\nMenu for {day}:")
            print(f"  Breakfast: {menu_for_day['Breakfast'] or 'No dishes set.'}")
            print(f"  Lunch: {menu_for_day['Lunch'] or 'No dishes set.'}")
            print(f"  Afternoon Tea: {menu_for_day['Afternoon Tea'] or 'No dishes set.'}")
        else:
            print(f"No menu found for {day}.")

def list_students_with_allergies(students):
    students_with_allergies = [student for student in students if student.allergies]
    
    if not students_with_allergies:
        print("No students with allergies.\n")
    else:
        print("\nStudents with allergies:")
        for student in students_with_allergies:
            allergies = ', '.join(student.allergies)
            print(f"{student.full_name} (Student ID: {student.get_formatted_id()}) has the following allergies: {allergies}\n")

def delete_menu_for_day(kitchen):
    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print("Invalid input. Please enter a valid week number (integer).")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return
    except Exception as e:
        print("\nAn unexpected error occurred")
        return

    day_map = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday"
    }
    
    try:
        day_input = int(input("Enter the day of the week (1 = Monday, ..., 5 = Friday): "))
        if day_input not in day_map:
            raise ValueError
        day = day_map[day_input]
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5 for weekdays.")
        return
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted.")
        return
    except Exception as e:
        print("\nAn unexpected error occurred")
        return

    week_str = str(week)
    
    if week_str in kitchen.menu and day in kitchen.menu[week_str]:
        kitchen.menu[week_str][day] = {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
        print(f"Menu for {day} (Week {week}) has been deleted.\n")
    else:
        print(f"No menu found for {day} (Week {week}).\n")
