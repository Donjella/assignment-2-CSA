def add_menu_for_day(kitchen):
    """Prompt the user to add a menu for breakfast, lunch, and afternoon tea for a specific day."""
    day = input("Enter the day of the week: ").capitalize()

    # Ask the user to input dishes for each meal and use title() to capitalize each word
    breakfast = input("Enter the breakfast dish: ").strip().title()
    lunch = input("Enter the lunch dish: ").strip().title()
    afternoon_tea = input("Enter the afternoon tea dish: ").strip().title()

    # Add each dish to the respective meal
    kitchen.add_menu(day, "Breakfast", breakfast)
    kitchen.add_menu(day, "Lunch", lunch)
    kitchen.add_menu(day, "Afternoon Tea", afternoon_tea)

def list_menu_for_day(kitchen):
    """Prompt the user to list the menu for a specific day."""
    kitchen.list_menu()

def list_students_with_allergies(students):
    """List all students with allergies."""
    students_with_allergies = [student for student in students if student.allergies]
    
    if not students_with_allergies:
        print("No students with allergies.\n")
    else:
        print("\nStudents with allergies:")
        for student in students_with_allergies:
            allergies = ', '.join(student.allergies)
            print(f"{student.full_name} (ID: {student.student_id}) has the following allergies: {allergies}\n")