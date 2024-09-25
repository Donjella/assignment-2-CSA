from functions.student_functions import add_student
from functions.classroom_functions import list_students_by_classroom, delete_student
from classes.classrooms import students, Classroom
from classes.kitchen import Kitchen
from functions.kitchen_functions import list_menu_for_day, add_menu_for_day, list_students_with_allergies, delete_menu_for_day
from functions.file_functions import save_students, load_students, save_menu 

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


def create_main_menu():
    print("Welcome to the Childcare Management App\n")
    print("What would you like to manage?")
    print("1. Students")
    print("2. Kitchen")
    print("3. Exit\n")

    choice = input("Enter your choice: ")
    return choice

def create_student_menu():
    print("\nStudent Management Menu:")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. List Students")
    print("4. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

def create_kitchen_menu():
    print("\nKitchen Management Menu:")
    print("1. Add/Update Menu for the Day")
    print("2. Delete Menu for the Day")
    print("3. List Menu for the Day")
    print("4. List Students with Allergies")
    print("5. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

# Main logic
choice = ""

while choice != "3":  # Main menu loop, "3" is exit
    choice = create_main_menu()

    if choice == "1":  # Student menu
        student_choice = ""
        while student_choice != "4":  # Loop for the student sub-menu
            student_choice = create_student_menu()
            if student_choice == "1":
                print("Add Student")
                add_student(students, classrooms)
            elif student_choice == "2":
                print("Delete Student")
                delete_student(students, classrooms)
            elif student_choice == "3":
                list_students_by_classroom(classrooms)  # List students by classroom
            elif student_choice == "4":
                print("Returning to Main Menu")
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":  # Kitchen menu
        kitchen_choice = ""
        while kitchen_choice != "5":  # Loop for the kitchen sub-menu, option 5 goes back to the main menu
            kitchen_choice = create_kitchen_menu()
            if kitchen_choice == "1":
                add_menu_for_day(kitchen)  # Add/Update Menu for the day
            elif kitchen_choice == "2":
                delete_menu_for_day(kitchen)  # Delete menu for the day
            elif kitchen_choice == "3":
                list_menu_for_day(kitchen)  # List the menu for the day
            elif kitchen_choice == "4":
                list_students_with_allergies(students)  # List students with allergies
            elif kitchen_choice == "5":
                print("Returning to Main Menu")
                break  # Break the kitchen menu loop to return to the main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":  # Exit option
        print("\nSaving students and kitchen data, then exiting the application. Goodbye!\n")
        save_students(students)  # Call save_students before exiting
        save_menu(kitchen)  # Call save_menu to save the kitchen data before exiting
        break  # Exits the main loop

    else:
        print("Invalid choice. Please try again.")
