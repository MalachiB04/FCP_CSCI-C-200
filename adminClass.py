import csv
from datetime import datetime
import os
from userClass import User
from random import randint
from colorama import Fore, Style
from studentClass import Student

class Admin(User):
    def __init__(self, username, password, course, name):
        super.__init__(username, password, name)


    def admin_log_validation():
        try:
            login = True
            counter = 5
            path = os.path.join('adminFolder', 'adminLogin.csv')
            if not os.path.exists(path):  # Check if the file exists
                raise FileNotFoundError

            # Load user data into a dictionary
            while counter > 0:
                username = input('Enter Username: ')
                password = input('Enter Password: ')
                with open(path, 'r') as fr:
                    reader = csv.DictReader(fr)
                    for row in reader:
                        if row['username'] == username:
                            if row['password'] == password:
                                print(f"Login Successful! Welcome {row['name']}")
                                print()
                                return True
                            else:
                                login = False
                        else:
                            login = False

                    if not login:
                        counter -= 1
                        print()
                        print(f"== Please Try Again: {counter} Attempts Remain ==")

                    if counter == 0:
                        print(f"== Login Unsuccessful --- {datetime.now().strftime('%I:%M %p')} ==")
                        return False

        except FileNotFoundError:
            Admin.file_not_found()

        except IndexError:
            Admin.index_error()


    def create_acct_teacher() -> None:
        try:

            roles = {
            '1': 'Assistant Professor',
            '2': 'Associate Professor',
            '3': 'Professor'
        }

            path = os.path.join('adminFolder', 'teacherFolder')

            os.makedirs(path, exist_ok=True)

            file_path = os.path.join(path, 'teacherLogin.csv')

            file_exists = os.path.exists(file_path)

            existing_user = []
            existing_id = []
            headers = ['teacher IDN', 'username', 'password', 'name', 'role','datetimeUpdated']
            with open(os.path.join(path, 'teacherLogin.csv'), 'a', newline='') as fw:
                writer = csv.writer(fw)
                teacher_idn = randint(111111,999999)

                if not file_exists:
                    writer.writerow(headers)
                else:
                    with open(file_path, 'r') as fr:
                        reader = csv.DictReader(fr)
                        for row in reader:
                            existing_id.append(row['teacher IDN'])
                            existing_user.append(row['username'])
                            while teacher_idn in existing_id:
                                teacher_idn = randint(111111,999999)

                username = input("Set Teacher Username >: ")
                password = input("Set Teacher Password >: ")
                name = input("Set Teacher Name >: ")

                if username in existing_user:
                    print(Style.BRIGHT + Fore.RED + "== ERROR: Teacher already in the System ==" + Style.RESET_ALL)
                    print()

                else:
                    print()
                    print("Please select role from the list below:")
                    for key, value in roles.items():
                        print(f"{key}: {value}")

                    role_choose = input("Set Role :> ")
                    counter = 5
                    while counter > 0:
                        if not all([username,password,name]):
                            raise Warning

                        elif role_choose in roles:
                            role = roles[role_choose]
                            writer.writerow([teacher_idn, username, password, name.title(), role, datetime.now().replace(microsecond=0)])
                            print(Style.BRIGHT + Fore.GREEN + "== Teacher Successfully Added ==" + Style.RESET_ALL)
                            break
                        else:
                            counter -= 1
                            print()
                            print(Style.BRIGHT + Fore.RED + "== Invalid Input: Please choose from the list ==" + Style.RESET_ALL)
                            role_choose = input("Set Role :> ")

                        if counter == 0:
                            print(Style.BRIGHT + Fore.RED + "== Server Timed Out ==\nReturning to main menu..." + Style.RESET_ALL)

        except FileNotFoundError:
            Admin.file_not_found()

        except Warning:
            print(Style.BRIGHT + Fore.RED +'== There was an error processing your request =='+ Style.RESET_ALL)


    def create_acct_student() -> None:
        try:
            path = os.path.join(os.getcwd(), 'adminFolder', 'studentFolder')
            os.makedirs(path,exist_ok=True)

            file_path = os.path.join(path,'studentLog.csv')
            file_exists = os.path.exists(file_path)

            headers = ['student IDN', 'username', 'password', 'name', 'enrollment status', 'courses', 'time added']
            with open(os.path.join(path,'studentLog.csv'), 'a', newline='') as fw:
                writer = csv.writer(fw)

                existing_user = []
                if not file_exists:
                    writer.writerow(headers)
                    with open(file_path, 'r') as fr:
                        reader = csv.reader(fr)
                        next(reader, None)
                        existing_user = [row[1] for row in reader]

                if file_exists:
                    with open(file_path, 'r') as fr:
                        reader = csv.reader(fr)
                        next(reader, None)
                        existing_user = [row[1] for row in reader]

                id_number = randint(111111,999999)
                while id_number in existing_user:
                    id_number = randint(111111,999999)

                counter = 5
                while counter > 0:
                    username = input('Set Student Username: ')
                    password = input('Set Student Password: ')
                    name = input('Set Student Name: ')

                    if not username in existing_user and all([username,password, name]) and not name.isdigit():
                        writer.writerow([id_number, username, password, name.title(), False, '', datetime.now().replace(microsecond=0)])
                        print(Style.BRIGHT + Fore.GREEN + f"{name.title()} Successfully Added!" + Style.RESET_ALL)
                        break
                    else:
                        print()
                        print(Style.BRIGHT + Fore.RED + '== An Error Has Occurred ==' + Style.RESET_ALL)
                        counter -= 1

                    if counter == 0:
                        print(Style.BRIGHT + Fore.RED +'== There was an error processing your request =='+ Style.RESET_ALL)

        except FileNotFoundError:
            Admin.file_not_found()

        except ValueError:
            print(Style.BRIGHT + Fore.RED +'== There was an error processing your request =='+ Style.RESET_ALL)


    def create_courses():
        try:
            teacher_list = []
            course_file_path = os.path.join("adminFolder", "courses.csv")
            file_exist_course = os.path.exists(course_file_path)

            teacher_path = Admin.path_for_teacher()
            teacher_exits = os.path.exists(teacher_path)
            if not teacher_exits:
                raise FileNotFoundError

            if not file_exist_course:
                headers = ['Course Number', 'Course Title', 'Instructor']
                with open(course_file_path, 'w', newline='') as fw:
                    writer = csv.writer(fw)
                    writer.writerow(headers)
                    print(Style.BRIGHT + Fore.GREEN + "== Welcome! Refresh to Add Teachers ==" + Style.RESET_ALL)

            else:
                counter = 5
                while counter >= 0:
                    course_name = input("Enter Name of Course: ").title()

                    if not course_name.isdigit():
                        course_name = str(course_name)
                        break

                    else:
                        print(Style.BRIGHT + Fore.RED + "== Invalid Input: Please try again ==" + Style.RESET_ALL)
                        counter -= 1
                        print()

                    if counter == 0:
                            print(Style.BRIGHT + Fore.RED + "== Server Timed Out ==\nReturning to main menu..." + Style.RESET_ALL)

                with open(User.path_for_teacher(), 'r') as fr:
                    reader = csv.reader(fr)
                    next(reader,None)  # Skip the header row
                    for row in reader:
                        teacher_list.append(row[3])  # Collect teacher names from the third column
                if len(teacher_list) == 0:
                    raise UserWarning

                print()
                print("Pick from the teachers below: ")
                for index, teachers in enumerate(teacher_list, start=1):
                    print(f"{index}: {teachers}")

                while True:
                    userInput = int(input(":> ").strip())
                    if 1 <= userInput <= len(teacher_list):
                        selected_teacher = teacher_list[userInput - 1]
                        break
                    else:
                        print(Style.BRIGHT + Fore.RED + "== Invalid Input: Please try again =="+ Style.RESET_ALL)

                existing_course_ID = []
                exists = False
                with open(course_file_path, 'r') as fr:
                    reader = csv.reader(fr)
                    for row in reader:
                        existing_course_ID.append(row[0])  # Need to loop through each row
                        if len(row) >= 3:  # Ensure the row has at least 3 columns
                            if course_name == row[1] or selected_teacher == row[2]:
                                exists = True
                                print(Style.BRIGHT + Fore.RED + "== Duplicate data detected: Please try again ==" + Style.RESET_ALL)
                    course_number = randint(111111,999999)
                    while course_number in existing_course_ID:
                        course_number = randint(111111,999999)

                # If no conflicts were found, append the new row
                if not exists:
                    with open(course_file_path, 'a', newline='') as fw:
                        writer = csv.writer(fw)
                        writer.writerow([course_number, course_name.title(), selected_teacher.title()])
                        print(Style.BRIGHT + Fore.GREEN + "== Course created successfully ==" + Style.RESET_ALL)

        except UserWarning:
            print(Style.BRIGHT + Fore.RED + "== No teachers currently available ==" + Style.RESET_ALL)

        except ValueError:
            Admin.input_error_message()

        except FileNotFoundError:
            Admin.file_not_found()

        except IndexError:
            Admin.index_error()

    def view_enrollment():
        try:
            file_exists = os.path.exists(Admin.get_student_file_path())

            if not file_exists:
                raise FileNotFoundError

            with open(Admin.get_student_file_path(), 'r') as fr:
                reader = csv.DictReader(fr)
                print("-"*30)
                print()
                for row in reader:
                    if row['enrollment status'] == 'True' and row['courses'] != '':
                        print(f"Name: {row['name']}\nEnrolled in: {row['courses']}\n")
                    else:
                        print(f"Name: {row['name']}\nEnrolled in: None\n")
                print("-"*30)
        except FileNotFoundError:
            Admin.file_not_found()


    def view_student_information_individual():
        pass
        try:
            file_exists = os.path.exists(User.get_student_file_path())
            if not file_exists:
                raise FileNotFoundError
            else:
                search = input("Input students 6 digit ID #: ").strip()

                with open(User.get_student_file_path(), 'r') as fr:
                    reader = csv.reader(fr)
                    existing_student_ID = []
                    for row in reader:
                        existing_student_ID.append(row[0])
                        if row[0] == search:
                            if row[4] == 'False':
                                print("-"*30)
                                print(f"Name: {row[3]}\nUsername: {row[1]}\nPassword: {row[2]}\nStudent ID: {row[0]}\nCourses: None")
                                print("-"*30)

                            elif row[4] == "True":
                                print("-"*30)
                                print(f"Name: {row[3]}\nUsername: {row[1]}\nPassword: {row[2]}\nStudent ID: {row[0]}\nCourses: {row[5]}")
                                print("-"*30)
                    if search == '' or search not in existing_student_ID:
                        print(Style.BRIGHT + Fore.RED + '== Student not found ==' + Style.RESET_ALL)

        except FileNotFoundError:
           Admin.file_not_found()


    def view_student_information_all():

        try:
            file_exist = os.path.exists(User.get_student_file_path())
            if not file_exist:
                raise FileNotFoundError
            else:
                with open(User.get_student_file_path(), 'r') as fr:
                    reader = csv.DictReader(fr)
                    print('-'*30)
                    for row in reader:
                        if row['courses'] == '':
                            row['courses'] = None
                        print(f"Name: {row['name']}\nUsername: {row['username']}\nPassword: {row['password']}\nStudent ID: {row['student IDN']}\nCourses: {row['courses']}")
                        print('-'*30)
        except FileNotFoundError:
            Admin.file_not_found()


    def view_teacher_information_all():
        try:
            file_exist = User.path_for_teacher()
            if not file_exist:
                raise FileNotFoundError
            else:
                with open(User.path_for_teacher(), 'r') as fr:
                    print('-'*30)
                    reader = csv.DictReader(fr)
                    for row in reader:
                        print(f"Name: {row['name']}\nUsername: {row['username']}\nPassword: {row['password']}\nTeacher ID: {row['teacher IDN']}\nRole: {row['role']}")
                        print('-'*30)
        except FileNotFoundError:
            User.file_not_found()


    def view_teacher_information_individual():
        try:
            file_exist = os.path.exists(User.path_for_teacher())
            if not file_exist:
                raise FileNotFoundError
            else:
                existing_IDN = []
                enter_ID = input("Input teacher 6 digit ID #: ")
                with open(User.path_for_teacher(), 'r') as fr:
                    reader = csv.reader(fr)
                    for row in reader:
                        existing_IDN.append(row[0])
                        if row[0] == enter_ID:
                            print('-'*30)
                            print(f"Name: {row[3]}\nUsername: {row[1]}\nPassword: {row[2]}\nTeacher ID: {row[0]}\nRole: {row[4]}")
                            print('-'*30)

                    if not enter_ID in existing_IDN:
                        print(Style.BRIGHT + Fore.RED + '== Teacher not found ==' + Style.RESET_ALL)

        except FileNotFoundError:
            Admin.file_not_found()


    def view_courses():
        try:
            file_path = os.path.join('adminFolder', 'courses.csv')
            file_exist = os.path.exists(file_path)
            if not file_exist:
                raise FileNotFoundError
            else:
                with open(file_path, 'r') as fr:
                    reader = csv.DictReader(fr)
                    print("-"*30)
                    for row in reader:
                        print(f"Course Name: {row['Course Title']}\nCourse Number: {row['Course Number']}\nInstructor: {row['Instructor'].title()}")
                        print("-"*30)
        except FileNotFoundError:
            Admin.file_not_found()

    def edit_enrollment():
        try:
            file_path = Admin.get_student_file_path()
            file_exist = os.path.exists(file_path)

            if not file_exist:
                raise FileNotFoundError

            else:
                with open(file_path, 'r') as fr:
                    reader = list(csv.reader(fr))
                    search_student = input('Enter student ID number:> ')
                    search_student = search_student
                    updated_rows = []
                    for row in reader:
                        if row[0] == search_student:
                            if row[4] == 'False':
                                print(f"Enrolling student {row[3]}...")
                                print()
                                Student.enroll(row[3])

                                return # Update enrollment status
                            elif row[4] == 'True':
                                remove_enrollment = input(f"Would you like to remove {row[3]} from enrollment? (y/n): ")
                                if remove_enrollment.lower() == 'y':
                                    row[4] = 'False'
                                    row[5] = ''  # Clear courses
                                    row[6] = datetime.now().replace(microsecond=0)  # Update timestamp

                                if remove_enrollment.lower() == 'n':
                                    print(Style.BRIGHT + Fore.GREEN + "Returning to main menu... ")
                                    return

                        updated_rows.append(row)
                    if all(search_student != row[0] for row in reader):
                        print(Style.BRIGHT + Fore.RED + "== Student not found ==" + Style.RESET_ALL)
                        return

                    with open(file_path, 'w', newline='') as fw:
                        writer = csv.writer(fw)
                        writer.writerows(updated_rows)
                        print(Style.BRIGHT + Fore.GREEN + "== Enrollment Updated ==" + Style.RESET_ALL)
                        return

        except FileNotFoundError:
            Admin.file_not_found()