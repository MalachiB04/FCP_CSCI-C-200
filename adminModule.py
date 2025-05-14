from adminClass import Admin
from colorama import Fore, Style
print(Fore.GREEN + Style.BRIGHT + "Welcome to PyINDY Admin Module!" + Style.RESET_ALL)

admin_verification = Admin.admin_log_validation()
inUse = True
while inUse:
    try:
        if admin_verification:
            print(Style.BRIGHT + Fore.GREEN + "Type 'Exit' in this menu to leave" + Style.RESET_ALL)
            welcome_user = input("Please choose from the options available: " \
            "\n[a] Add a new Student" \
            "\n[b] Add a new Teacher" \
            "\n[c] Add/Assign a course" \
            "\n[d] Edit/View enrollment" \
            "\n[e] View Student information" \
            "\n[f] View Teacher information" \
            "\n[g] View Course information" \
            "\nEnter Here:> ").strip().lower()

            if welcome_user == 'a':
                print()
                Admin.create_acct_student()
                print()

                """
                Must complete if no students in database
                """

            elif welcome_user == 'b':
                print()
                Admin.create_acct_teacher()
                print()

                """
                Must complete if no teachers in database
                """

            elif welcome_user == 'c':
                print()
                Admin.create_courses()
                print()

                """
                Must complete before students can enroll. Requires 2 classes minimum and teachers to teach the class
                """

            elif welcome_user == 'd':
                    print()
                    embedded_option_one = input("Would you like to\n[a]Edit enrollment\n[b]View Enrollment\n:> ")
                    if embedded_option_one.lower() == 'a':
                        print()
                        Admin.edit_enrollment()
                        print()
                    elif embedded_option_one.lower() == 'b':
                        print()
                        Admin.view_enrollment()
                        print()
                    else:
                        Admin.input_error_message()
                        print()

            elif welcome_user == 'e':
                print()
                embedded_option_two= input("\nWould you like to:\n[a]View specific student\n[b]View ALL student information \n:> ")

                if embedded_option_two == 'a':
                    print()
                    Admin.view_student_information_individual()
                    print()

                elif embedded_option_two == 'b':
                    print()
                    Admin.view_student_information_all()
                    print()

                else:
                    print()
                    Admin.input_error_message()

            elif welcome_user == 'f':
                embedded_option_three = input("\nWould you like to:\n[a]View specific teacher\n[b]View ALL teachers\n:> ")
                if embedded_option_three.lower() == 'a':
                    print()
                    Admin.view_teacher_information_individual()
                    print()
                elif embedded_option_three.lower() == 'b':
                    print()
                    Admin.view_teacher_information_all()
                    print()
                else:
                    print()
                    Admin.input_error_message()


            elif welcome_user == 'g':
                print()
                Admin.view_courses()
                print()

            elif welcome_user.title() == 'Exit':
                print()
                print(Style.BRIGHT + Fore.GREEN + '== Thank you ==' + Style.RESET_ALL)
                inUse = False
            else:
                print()
                Admin.input_error_message()
                print()

    except KeyboardInterrupt:
        print("...\nUh oh! It broke! Refresh and try again! ")
        break

    except EOFError:
        print("...\nUh oh! It broke! Refresh and try again! ")
        break