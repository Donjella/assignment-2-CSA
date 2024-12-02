from colored import Style, stylize, attr, fg # Library for terminal text styling and colors.
from prettytable import PrettyTable # Library for creating formatted tables in the terminal, for example, displaying students with allergies in a neat table.

from constants import color3, color4, color5  # Predefined color constants for consistent styling.

def add_menu_for_day(kitchen):
    #  Prompt the user to add or update the menu for a specific day in a given week.
    # Purpose: It allows the user to set or update dishes for breakfast, lunch, and afternoon tea for a specific day by 
    # updating the `menu` dictionary in the Kitchen instance.
    
    # Arguments: kitchen (Kitchen): The Kitchen instance where the menu will be updated.

    # Example of how it works/is used: 
    #     1. Prompts the user for the week number and day of the week.
    #     2. Validates the input for week and day ranges.
    #     3. Collects dishes input for breakfast, lunch, and afternoon tea.
    #     4. Updates or creates the menu for the specified week and day.
    #     5. It also handles invalid inputs for week, day, and dishes and safely exits if input is interrupted (e.g., Ctrl+C or EOFError).

    try:
        # Prompt for week number
        week_input = input("Enter the week number (1-52): ").strip()
        if not week_input:
            raise ValueError(f"{color5}Week number cannot be empty.{Style.reset}")
        week = int(week_input)

        # Ensure week is within valid range (1-52)
        if week < 1 or week > 52:
            raise ValueError(f"{color5}Please enter a valid week number between 1 and 52.{Style.reset}\n")

        # Day mapping
        day_map = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
        
        # Prompt for day of the week
        day_input = input("Enter the day of the week (1 = Monday,..,5 = Friday): ").strip()
        if not day_input:
            raise ValueError(f"{color5}Day cannot be empty.{Style.reset}\n")
        day = int(day_input)
        
        if day not in day_map:
            raise ValueError(f"{color5}Please enter a number between 1 and 5 (weekdays only).{Style.reset}\n")
        day = day_map[day]

        print(f"\n{color4}Adding/updating menu for Week {week}, Day: {day}{Style.reset}\n")

    except ValueError as error:
        print(f"{color5}{error}{Style.reset}")
        return  
    except (EOFError, KeyboardInterrupt):
        print(f"\n{color5}Input interrupted.{Style.reset}")
        return
    except Exception as e:
        print(f"\n{color5}An unexpected error occurred{Style.reset}")
        return

    # Ask the user to input dishes for each meal
    try:
        breakfast = input("Enter the breakfast dish: ").strip().title()
        lunch = input("Enter the lunch dish: ").strip().title()
        afternoon_tea = input("Enter the afternoon tea dish: ").strip().title()
    except (EOFError, KeyboardInterrupt):
        print(f"\n{color5}Input interrupted.{Style.reset}")
        return
    except Exception as e:
        print(f"\n{color5}An unexpected error occurred{Style.reset}")
        return

    week_str = str(week)
    if week_str not in kitchen.menu:
        # Check if the specified week exists in the kitchen's menu.
        # If the week is not present, initialize a new entry in the `menu` dictionary.
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

    print(f"\n{color3}Menu for {day} in Week {week} has been updated.{Style.reset}")

def list_menu_for_week(kitchen):
    # Display the menu for all weekdays in a given week.

    # Purpose: Retrieves and displays the menu for a specified week in a formatted layout.

    # Arguments: kitchen (Kitchen): The Kitchen instance containing the menu to display.

    # Example of how it works/is used: 
    #     1. Prompts the user for the week number.
    #     2. Checks if a menu exists for the week.
    #     3. Displays the menu for each weekday with breakfast, lunch, and afternoon tea.
    #     4. Exception Handling: Handles invalid week inputs and missing menu data and safely exits if input is interrupted.
    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print(f"{color5}Invalid input. Please enter a valid week number (integer).{Style.reset}")
        return
    except (EOFError, KeyboardInterrupt):
        print(f"\n{color5}Input interrupted.{Style.reset}")
        return
    except Exception as e:
        print(f"\n{color5}An unexpected error occurred{Style.reset}")
        return

    week_str = str(week)

    if week_str not in kitchen.menu:
        print(f"{color3}No menu found for Week {week}.{Style.reset}\n")
        return

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print(f"\n{color3}--- Menu for Week {week} ---{Style.reset}")

    for day in days_of_week:
        if day in kitchen.menu[week_str]:
            menu_for_day = kitchen.menu[week_str][day]
            print(f"{color4}\nMenu for {day}:{Style.reset}")
            print(f"  Breakfast: {menu_for_day['Breakfast'] or 'No dishes set.'}")
            print(f"  Lunch: {menu_for_day['Lunch'] or 'No dishes set.'}")
            print(f"  Afternoon Tea: {menu_for_day['Afternoon Tea'] or 'No dishes set.'}")
        else:
            print(f"No menu found for {day}.")

def list_students_with_allergies(classrooms):

    #  List all students with allergies, displaying their name, classroom, and allergies in a formatted table.
    # Purpose: It iterates through all classrooms to find students with allergies and displays the student information (name, ID, classroom, and allergies) 
    # in a color-coded and styled table.

    # Arguments:
    #     classrooms (list): A list of Classroom instances, each containing a list of students.

    # Example of how it works/is used: 
    #     1. Initializes a PrettyTable for displaying the information in a tabular format.
    #     2. Iterates through each classroom and its students to find students with allergies using a nested for loop.
    #     3. Populates and output the table with relevant student data.
    #     4. Exception Handling: handles empty tables gracefully by providing a clear message if no students have allergies.

    # Initialize the table
    table = PrettyTable()

    # Bold the headers and apply the spring_green_4 color
    header_color = fg("blue") + attr("bold")
    header_student_name_id = stylize("Student Name (Student ID)", header_color)
    header_classroom = stylize("Classroom", header_color)
    header_allergies = stylize("Allergies", header_color)

    # Apply green color for table lines
    table.horizontal_char = stylize("-", fg("spring_green_4"))
    table.junction_char = stylize("+", fg("spring_green_4"))
    table.vertical_char = stylize("|", fg("spring_green_4"))
    
    table.field_names = [header_student_name_id, header_classroom, header_allergies]

    for classroom in classrooms:
        for student in classroom.students:
            if student.allergies:  # If student has allergies
                allergies = ', '.join(student.allergies)
                name_id = f"{student.full_name} (ID: {student.get_formatted_id()})"
                
                # Add row to the table
                table.add_row([name_id, classroom.get_name(), allergies])


    # Check if the table has any rows
    if len(table.rows) == 0:
        print("No students with allergies.\n")
    else:
        print(f"\n{color3}Students with allergies:{Style.reset}")
        print(table)


def delete_menu_for_day(kitchen):
    # Delete the menu for a specific day in a given week.
    # Purpose: This function allows the user to remove the menu for breakfast, lunch, and afternoon tea for a specific day in the specified week.
    # It is done by updating the `menu` dictionary in the Kitchen instance to clear the menu for the selected day.

    # Arguments:
    #     kitchen (Kitchen): The Kitchen instance where the menu will be modified.

    # Example of how it works/is used:
    #     1. Prompts the user for the week number and day of the week.
    #     2. Validates the inputs to ensure they are within the correct range.
    #     3. Deletes the menu for the specified day if it exists.

    # Exception Handling:
    #     - Handles invalid inputs for week and day (e.g., non-numeric values, out-of-range inputs).
    #     - Provides a clear message if the menu for the specified day and week is not found.
    #     - Safely exits if input is interrupted (e.g., Ctrl+C or EOFError).

    try:
        week = int(input("Enter the week number: "))
    except ValueError:
        print(f"{color5}Invalid input. Please enter a valid week number (integer).{Style.reset}")
        return
    except (EOFError, KeyboardInterrupt):
        print(f"\n{color5}Input interrupted.{Style.reset}")
        return
    except Exception as e:
        print(f"\n{color5}An unexpected error occurred{Style.reset}")
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
        print(f"{color5}Invalid input. Please enter a number between 1 and 5 for weekdays.{Style.reset}")
        return
    except (EOFError, KeyboardInterrupt):
        print(f"\n{color5}Input interrupted.{Style.reset}")
        return
    except Exception as e:
        print(f"\n{color5}An unexpected error occurred{Style.reset}")
        return

    week_str = str(week)
    
    if week_str in kitchen.menu and day in kitchen.menu[week_str]:
        kitchen.menu[week_str][day] = {"Breakfast": None, "Lunch": None, "Afternoon Tea": None}
        print(f"\n{color3}Menu for {day} (Week {week}) has been deleted.{Style.reset}")
    else:
        print(f"{color3}No menu found for {day} (Week {week}).{Style.reset}\n")
