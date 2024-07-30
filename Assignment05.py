# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   R.Root, 2030/01/01, Created Script
#   G.DuBuque, 2030/07/29, Updated script for Assignment 5 to use json files, dictionaries
#                          and exception handling. Removed unused variable json_data: str
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''    # Holds the first name of a student entered by the user.
student_last_name: str = ''     # Holds the last name of a student entered by the user.
course_name: str = ''           # Holds the name of a course entered by the user.
file = None                     # Holds a reference to an opened file.
menu_choice: str = ''           # Hold the choice made by the user.
student_data: dict = {}         # Holds data for one student in a dictionary (GD)
students: list = []             # List to hold all student dictionaries (json format) (GD)

# When the program starts read the contents of the json file into the students list (GD)
# Each row has the following keys: "FirstName", "LastName", "CourseName" (GD)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:  # Check if file does not exist (GD)
    print(f"Text file {FILE_NAME} must exist before running this script!\n")  # Added FILE_NAME (GD)
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:          # Check for other errors (GD)
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:  # Close file if still opened (GD)
    if not file.closed:
        file.close()

# Present and Process the data
while True:

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            # Check to make sure name does not include numbers (GD)
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            # Check to make sure name does not include numbers (GD)
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            # Add student data to dictionary, then add dictionary to students list (GD)
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Print invalid name entry message (GD)
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:  # Print other error message (GD)
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        # Updated with student data in dictionary format (GD)
        print("-" * 50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} "
                  f"is enrolled in {student["CourseName"]}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            # Changed print format to show data as is (dictionaries in json format) (GD)
            for student in students:
                print(student)
            continue
        # Check to make sure student data is in json format (GD)
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        # Check for other errors (GD)
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:  # Close file if still opened (GD)
            if not file.closed:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3 or 4")     # Added option 4 (GD)

print("Program Ended")
