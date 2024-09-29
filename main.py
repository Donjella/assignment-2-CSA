from functions.student_functions import add_student, list_guardian_details
from functions.classroom_functions import list_students_by_classroom, delete_student, count_total_students
from classes.classrooms import students, Classroom
from classes.kitchen import Kitchen
from functions.kitchen_functions import list_menu_for_week, add_menu_for_day, list_students_with_allergies, delete_menu_for_day
from functions.file_functions import save_students, load_students, save_menu, load_menu
from constants import color1, color2, color3, color4, color5
from colored import Style

# Global list for students
students = []

# Initialize classrooms
classrooms = [
    Classroom("Babies Room (0-2 years)", 0, 2),
    Classroom("Toddlers Room (2-3 years)", 2, 3),
    Classroom("Kindergarten Room (3-5 years)", 3, 5)
]

# Load students from the saved students.json file
load_students(students, classrooms)

# Initialize the kitchen
kitchen = Kitchen()

# Load the kitchen menu from the saved kitchen.json file
load_menu(kitchen)

def create_menu(menu_title, options, valid_choices):
    """Generic function to display a menu and get a validated user choice."""
    while True:
        try:
            print(f"\n{menu_title}")
            for option in options:
                print(option)

            choice = input("Please enter your choice: ")
            if choice in valid_choices:
                return choice  # Valid input, return choice
            else:
                print(f"{color5}Invalid choice. Please enter a number between {valid_choices[0]} and {valid_choices[-1]}.{Style.reset}")
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Returning to Main Menu.")
            return valid_choices[-1]  # Return the last valid choice to exit gracefully

def create_main_menu():
    welcome_message = f"{color1}Welcome to the Childcare Management Application{Style.reset}\nWhat would you like to manage?\n"
    return create_menu(
        welcome_message,
        ["1. Students", "2. Kitchen", "3. Exit\n"],
        ["1", "2", "3"]
    )

def create_student_menu():
    student_header = f"{color2}Student Management Menu{Style.reset}\nWhat would you like to do?\n"
    return create_menu(
        student_header,
        [
            "1. Add Student",
            "2. Delete Student",
            "3. List Students",
            "4. Display Parent/Guardian Details",
            "5. Save changes and return to Main Menu\n"
        ],
        ["1", "2", "3", "4", "5"]
    )

def create_kitchen_menu():
    kitchen_header = f"{color2}Kitchen Management Menu{Style.reset}\nWhat would you like to do?\n"
    return create_menu(
        kitchen_header,
        [
            "1. Add/Update Menu for the Day",
            "2. Delete Menu for the Day",
            "3. List Menu for the Week",
            "4. List Students with Allergies",
            "5. Save changes and return to Main Menu\n"
        ],
        ["1", "2", "3", "4", "5"]
    )

# Main logic
choice = ""

while choice != "3":  # Main menu loop, "3" is exit
    choice = create_main_menu()

    if choice == "1":  # Student menu
        student_choice = ""
        while student_choice != "5":  # Loop for the student sub-menu
            student_choice = create_student_menu()
            if student_choice == "1":
                print(f"{color4}Adding Student{Style.reset}\n")
                add_student(students, classrooms)
            elif student_choice == "2":
                print(f"{color4}Deleting Student{Style.reset}\n")
                delete_student(students, classrooms)
            elif student_choice == "3":
                print(f"\n{color3}Students list{Style.reset}") 
                list_students_by_classroom(classrooms)  # List students by classroom
                count_total_students(classrooms)
            elif student_choice == "4":
                list_guardian_details(students)  # Display parent/guardian details
            elif student_choice == "5":
                save_students(students)# Call save_students while exiting
                print(f"\n{color3}Student menu changes successfully saved{Style.reset}")  

    elif choice == "2":  # Kitchen menu
        kitchen_choice = ""
        while kitchen_choice != "5":  # Loop for the kitchen sub-menu, option 5 goes back to the main menu
            kitchen_choice = create_kitchen_menu()
            if kitchen_choice == "1":
                add_menu_for_day(kitchen)  # Add/Update Menu for the day
            elif kitchen_choice == "2":
                print(f"{color4}Deleting Menu for the day{Style.reset}\n")
                delete_menu_for_day(kitchen)  # Delete menu for the day
            elif kitchen_choice == "3":
                list_menu_for_week(kitchen)  # List the menu for the week
            elif kitchen_choice == "4":
                list_students_with_allergies(classrooms)  # List students with allergies
            elif kitchen_choice == "5":
                print("Save changes and return to Main Menu")
                save_menu(kitchen)  # Call save_menu to save the kitchen data before exiting
                print(f"\n{color3}Kitchen changes successfully saved{Style.reset}") 
                break  # Break the kitchen menu loop to return to the main menu

    elif choice == "3":  # Exit option
        print(f"\n{color1}Thanks for using the Childcare Management Application.{Style.reset}")
        print(f"{color1}See you again soon!{Style.reset}\n")
    

