# Childcare Management Application

### Quick Overview
This is a terminal-based command-line interface (CLI) application created to manage both students and kitchen operations at a childcare center with a maximum capacity of 100 students. The application enables users to add, view, and delete student records, access details about their parents or guardians, manage daily kitchen menus, and track students' allergies efficiently.

## Table of Contents

## Application Setup
Users can clone or fork the code of the application from its [GitHub repository](https://github.com/Donjella/assignment-2-CSA).

The application uses both in-built and external libraries:

1. [Colored](https://pypi.org/project/colored/)
2. [PrettyTable](https://pypi.org/project/prettytable/)
3. [JSON](https://pypi.org/project/colored/)  
4. [Pytest](https://docs.pytest.org/en/latest/) 
5. [Pytest Mock](https://pytest-mock.readthedocs.io/en/latest/) 
6. [Python datetime module](https://docs.python.org/3/library/datetime.html) 
7. [Python Random Module](https://docs.python.org/3/library/random.html) 

### Setting Up the Environment
1. Application is written in **Python Version 3.12.5**. Hence, please ensure you have Python 3.12.5 or later installed.
2. Install dependencies using a virtual environment.  

```bash
# to set up virtual environment
python3 -m venv .venv

# activate virtual environment
source .venv/bin/activate
```
3. Create a .gitignore file and add .venv to avoid pushing the virtual environment packages to the GitHub repository.
4. **requirements.txt** file is included in the application's [GitHub repository](https://github.com/Donjella/assignment-2-CSA). Hence, users can quickly install project dependencies once the virtual environment is active.  

```bash
# Install dependencies from requirements.txt.
pip install -r requirements.txt

# ONLY if you wish to install dependencies manually. If you have installed from requirements.txt, you can ignore these:
pip install colored
pip install pytest
pip install pytest-mock
pip install prettytable
```
## Third-party software licensing and security
The application makes use of various third-party software to facilitate its functionality and enhance user experience. 

Below is a comprehensive list of the third-party libraries used, their purposes, licenses, and information on their security impact.

1. ### [Colored](https://pypi.org/project/colored/)  
  
  - **Purpose**: to add color and styles to output in the application.
  - **Licence**: MIT Licence
  - **Ethical, legal and security impacts**: The library handles terminal output only and does not interact with sensitive data or external systems, ensuring minimal security risk.

2. ### [PrettyTable](https://pypi.org/project/prettytable/)
  
  - **Purpose**: PrettyTable is used within the application to create clean, well-formatted tables in this CLI app to display information.
  - **Licence**: BSD Licence
  - **Ethical, legal and security impacts**: PrettyTable is a pure table formatting library that poses no security risk as it doesn't process external inputs or handle sensitive data.

3. ### [JSON](https://pypi.org/project/colored/)  
  
  - **Purpose**: For reading from and writing to JSON files for student and kitchen data persistence.
  - **Licence**: Python Software Foundation Licence
  - **Ethical, legal and security impacts**: JSON is a built-in Python module and is secure for handling data serialization as long as it does not process untrusted input without proper validation.

4. ### [Pytest](https://docs.pytest.org/en/latest/) 
  
  - **Purpose**: Python testing framework for running unit tests to ensure code quality.
  - **Licence**: Python Software Foundation Licence
  - **Ethical, legal and security impacts**: Pytest is a testing framework used during development and testing phases only. It does not run in production and does not introduce any runtime security vulnerabilities.

5. ### [Pytest Mock](https://pytest-mock.readthedocs.io/en/)
  
  - **Purpose**: A plugin for pytest that provides easy mocking functionality to enable isolatation to parts of the application and test components effectively.
  - **Licence**: Python Software Foundation Licence
  - **Ethical, legal and security impacts**: Similar to pytest, it has no security impact on the production environment as it is used solely for development and testing.

6. ### [Python datetime module](https://docs.python.org/3/library/datetime.html) 

  - **Purpose**: A built-in Python module for handling dates and times, crucial for student age calculations and its related functionalities within the application.
  - **Licence**: Python Software Foundation Licence
  - **Ethical, legal and security impacts**: datetime is a secure module for handling date and time operations and does not introduce any security vulnerabilities.

7. ###  [Python Random Module](https://docs.python.org/3/library/random.html) 

  - **Purpose**: - A built-in Python module used to generate random unique student IDs for students in the application.
  - **Licence**: Python Software Foundation Licence
  - **Ethical, legal and security impacts**: The random module is suitable for generating unique IDs within the scope of this application. However, it is not intended for cryptographic purposes or secure applications beyond this context. For example, generating Secure Keys, Tokens or password hashing require high levels of randomness and unpredictability that go beyond what general-purpose modules like random can provide, typically to use in specialized cryptographic libraries.



## Using the application 
### Running the application

Navigate to the root directory of the project (where main.py is located).
```bash
# Start the application
python3 main.py
```
### Main Menu
Once application starts, you will be greeted with a welcome message, 2 management options to choose from (students or kitchen) and a third option to exit the application itself.

1. Students  
2. Kitchen
3. Exit

![screenshot for application main menu](docs/screenshots/main_menu.png)

### Option 1 - Student Management Menu
Choosing option 1 will lead you to the Student Management Menu

1. Add Student 
2. Delete Student
3. List Students
4. Display Parent/Guardian Details
5. Save changes or/and return to the main menu

![screenshot for student management menu](docs/screenshots/student_menu.png)

### Choice 1 - Add Student

You will be prompted one question at a time asking for the following input:

- Student's first name: 
- Student's last name:
- Student's birthday: *in YYYY-MM-DD format
- Does the student have any allergies?: *Yes or No answers
  - If yes, student will be prompted to enter what he/she is allergic to.
  - After entering allergy name, you will be prompted to enter if she has any more allergy.
  - If yes, prompt for allergy name again. If answer is no to allergy questions, you may proceed with parent/guardian details. 
- Enter guardian's first name:
- Enter guardian's last name:
- Enter guardian's contact number: 
- Enter guardian's email address:  

![screenshot for add student](docs/screenshots/assign_student.png)

Upon successfully entering all details above, you will be greeted with a confirmation message in yellow with black background that student is assigned to his/her respective classroom base on his/her age.
### Choice 2 - Delete Student

You will be prompted to enter student ID of student to be deleted:

- Enter the student's student ID to delete:

Upon entering a valid (existing student ID associated with a student enrolled in a class), a confirmation of deletion of student will be printed.

![screenshot for delete students](docs/screenshots/delete_student.png)

### Choice 3 - List Students

A lists of student categorised in their respective classrooms (Babies, Toddlers and Kindergarten) will be printed with their first and last names, age and student ID. Total number of students enrolled in the childcare service will also be shown.

![screenshot for list students](docs/screenshots/list_students.png)

### Choice 4 - Display Parent/Guardian Details

You will be prompted to enter student ID to view the particular student's parent/guardian details:

- Enter the student's student ID to view his/her guardian details:

Upon entering a valid (existing student ID associated with a student enrolled in a class), his/her guardian details (name, contact number and email) will be printed.

![screenshot for display parent/guardian](docs/screenshots/guardian_parent.png)

### Choice 5 - Save changes and return to the main menu

### Important:
***To successfully save changes*** made to students (Addition or deletion of student) so that it will load the changes when you exit the student management menu or start the application again, ***you have to choose option 5 - save changes and return to the main menu***.  

![screenshot for display save student menu](docs/screenshots/save_student_menu.png)

Ensure you ***see the confirmation prompt in yellow and black*** that changes in the student menu is successfully saved to confirm you have exited the student management menu and changes are saved.

---

## Option 2 - Kitchen Management Menu
Choosing option 2 will lead you to the kitchen Management Menu

1. Add/Update menu for the day
2. Delete menu for the Day
3. List menu for the Week
4. List students with allergies
5. Save changes or/and return to the main menu

![screenshot for kitchen management menu](docs/screenshots/kitchen_menu.png)

### Choice 1 - Add/Update menu for the day

You will be prompted one question at a time asking for the following input:

- Enter week number: Enter a number (inclusive of) between 1 to 52 to indicate which week of the year to add menu to.
- Enter the day of the week: Enter number only. i.e. (1 = Monday, 2 = Tuesday...5 = Friday)
Once successful, you will be prompted for:
- Enter name of breakfast dish:
- Enter name of lunch dish:
- Enter name of afternoon tea dish:   

![screenshot for display add/update kitchen menu](docs/screenshots/add_kitchen.png)

Upon successfully entering the information above, you will receive a confirmation stating menu for selected day in selected week is updated.

### Choice 2 - Delete menu for the day

You will be prompted one question at a time asking for the following input:

- Enter week number: Enter a number (inclusive of) between 1 to 52 to indicate which week of the year to delete menu from. 
- Enter the day of the week to delete menu from: Enter number only. i.e. (1 = Monday, 2 = Tuesday...5 = Friday)

![screenshot for delete students](docs/screenshots/delete_kitchen.png)

Upon successfully entering the information above, you will receive a confirmation stating that the menu for selected day in selected week has been deleted.

### Choice 3 - List menu for the week
      
You will be prompted one question at a time asking for the following input:

- Enter week number: Enter a number (inclusive of) between 1 to 52 to indicate which week of the year to list menu

![screenshot for list menu for the week](docs/screenshots/weekly_menu.png)

Upon successfully entering the information above, you will be shown the menu (Breakfast, Lunch and Afternoon Tea) for each day of the week.

### Choice 4 - List student with allergies
      
A list of students with allergies will be printed in a table. The list is sorted by the student's classrooms, i.e. students are grouped together by their classrooms.

![screenshot for list of student allergies](docs/screenshots/student_allergy.png)

### Choice 5 - Save changes and return to the main menu**

### Important:
***To successfully save changes*** made to the kitchen menu (add/update/delete) so that it will load the changes when you exit the kitchen management menu or start the application again, ***you have to choose option 5 - save changes and return to the main menu***.  

![screenshot for display save kitchen menu](docs/screenshots/save_kitchen_menu.png)

Ensure you ***see the confirmation prompt in yellow and black*** that changes in the kitchen menu is successfully saved to confirm you have exited the kitchen management menu and changes are saved.

---

## Option 3 - Exit

Choosing option 3 in the main menu will exit the application itself.

![screenshot for exit application message](docs/screenshots/exit_message.png)

Upon exiting the application, you will receive a thank you and see you again soon message.

---

## Testing