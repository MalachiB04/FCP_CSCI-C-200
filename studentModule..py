'''
Author: Malachi Butler
fileName: studentModule.py
Purpose: demonstrate classes, file handling, exception handling, input validation.
Special Requirements: v3.10, studentClass.py
Version: 3.10
Date created: 4/14/25
Last Updated: 5/03/25
'''
from studentClass import Student
from colorama import Fore, Style

#simple welcome card
print(Fore.YELLOW + Style.BRIGHT + "Welcome to Python INDY! (Student)" + Style.RESET_ALL)
in_use = True
student_log_in = Student.student_log_validation()
while in_use:
    try:
        if student_log_in:
            print(Style.BRIGHT + Fore.GREEN + "Type 'Exit' in this menu to leave" + Style.RESET_ALL)
            menu_selection = input("Please choose from the options available: " \
                "\n[a]Enroll" \
            "    \n[b]View classes" \
            "    \nEnter here :> ").strip().lower()

            if menu_selection == 'a':
                    '''
                    Allows Student to choose their class for the semester. "enrollment status" in CSV becomes
                    TRUE so Admin can differentiate between "enrolled" students and "unenrolled" students
                    '''
                    print()
                    Student.enroll(student_log_in)
                    print()


            elif menu_selection == 'b':
                    '''
                    Allows Student to view classes they're enrolled in currently
                    '''
                    print()
                    Student.view_classes(student_log_in)
                    print()


            elif menu_selection.title() == 'Exit':
                 print()
                 print(Style.BRIGHT + Fore.GREEN + '== Thank you ==' + Style.RESET_ALL)
                 in_use = False
            else:
                Student.input_error_message()

    except KeyboardInterrupt:
        print("...\nUh oh! It broke! Refresh and try again! ")

    except EOFError:
        print("...\nUh oh! It broke! Refresh and try again! ")