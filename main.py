from functions.student_functions import add_student
from functions.classroom_functions import list_students_by_classroom, delete_student
from classes.classrooms import students, Classroom
from classes.kitchen import Kitchen
from functions.kitchen_functions import list_menu_for_day, add_menu_for_day, list_students_with_allergies
students = [] 

classrooms = [
    Classroom("Babies Room (0-2 years)", 0, 2),
    Classroom("Toddlers Room (2-3 years)", 2, 3),
    Classroom("Kindergarten Room (3-5 years)", 3, 5)
]

# Initialize the kitchen
kitchen = Kitchen()

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
    print("1. Add Menu for the Day")
    print("2. List Menu for the Day")
    print("3. Update Menu for the Day")
    print("4. List Students with Allergies")
    print("5. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

# Main logic
choice = ""

while choice != "4":  # Main menu loop, "4" is exit
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
            while kitchen_choice != "4":  # Loop for the kitchen sub-menu, option 4 goes back to the main menu
                kitchen_choice = create_kitchen_menu()
                if kitchen_choice == "1":
                    add_menu_for_day(kitchen)
                elif kitchen_choice == "2":
                    list_menu_for_day(kitchen)
                elif kitchen_choice == "3":
                    add_menu_for_day(kitchen)  # You can update the menu the same way as adding it
                elif kitchen_choice == "4":
                     list_students_with_allergies(students)
                elif kitchen_choice == "5":
                    print("Returning to Main Menu")
                    break  # Break the kitchen menu loop to return to the main menu
                else:
                    print("Invalid choice. Please try again.")

    elif choice == "3":  # Exit option
        print("\nExiting the application. Goodbye!\n")
        break  # Exits the main loop

    else:
        print("Invalid choice. Please try again.")

