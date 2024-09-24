from functions.student_functions import add_student
from functions.classroom_functions import list_students_by_classroom

def create_main_menu():
    print("Welcome to the Childcare Management App\n")
    print("What would you like to manage?")
    print("1. Students")
    print("2. Staff")
    print("3. Kitchen")
    print("4. Exit\n")

    choice = input("Enter your choice: ")
    return choice

def create_student_menu():
    print("\nStudent Management Menu:")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. List Students")
    print("5. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

def create_staff_menu():
    print("\nStaff Management Menu:")
    print("1. Add Staff")
    print("2. Delete Staff")
    print("3. Update Staff")
    print("4. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

def create_kitchen_menu():
    print("\nKitchen Management Menu:")
    print("1. Add Menu for the Day")
    print("2. Delete Menu for the Day")
    print("3. Update Menu for the Day")
    print("4. Go Back to Main Menu\n")

    choice = input("Enter your choice: ")
    return choice

# Main logic
choice = ""

while choice != "4":  # Main menu loop, "4" is exit
    choice = create_main_menu()

    if choice == "1":  # Student menu
        student_choice = ""
        while student_choice != "5":  # Loop for the student sub-menu
            student_choice = create_student_menu()
            if student_choice == "1":
                print("Add Student")
                add_student()
            elif student_choice == "2":
                print("Delete Student")
                # Add logic to delete a student
            elif student_choice == "3":
                print("Update Student")
                # Add logic to update a student
            elif student_choice == "4":
                list_students_by_classroom()  # List students by classroom
            elif student_choice == "5":
                print("Returning to Main Menu")
            else:
                print("Invalid choice. Please try again.")

    elif choice == "2":  # Staff menu
        staff_choice = ""
        while staff_choice != "4":  # Loop for the staff sub-menu
            staff_choice = create_staff_menu()
            if staff_choice == "1":
                print("Add Staff")
                # Add logic to add staff
            elif staff_choice == "2":
                print("Delete Staff")
                # Add logic to delete staff
            elif staff_choice == "3":
                print("Update Staff")
                # Add logic to update staff
            elif staff_choice == "4":
                print("Returning to Main Menu")
            else:
                print("Invalid choice. Please try again.")

    elif choice == "3":  # Kitchen menu
        kitchen_choice = ""
        while kitchen_choice != "4":  # Loop for the kitchen sub-menu
            kitchen_choice = create_kitchen_menu()
            if kitchen_choice == "1":
                print("Add Menu for the Day")
                # Add logic to add menu
            elif kitchen_choice == "2":
                print("Delete Menu for the Day")
                # Add logic to delete menu
            elif kitchen_choice == "3":
                print("Update Menu for the Day")
                # Add logic to update menu
            elif kitchen_choice == "4":
                print("Returning to Main Menu")
            else:
                print("Invalid choice. Please try again.")

    elif choice == "4":  # Exit option
        print("Exiting the application. Goodbye!")
        break  # Exits the main loop

    else:
        print("Invalid choice. Please try again.")

