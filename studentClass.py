'''
Author: Malachi Butler
fileName: studentClass.py
Purpose: demonstrate classes, file handling, exception handling, input validation, inheritance.
Special Requirements: v3.10, userClass.py
Version: 3.10
Date created: 4/14/25
Last Updated: 4/30/25
'''
import csv
import os
from datetime import datetime
from userClass import User
from colorama import Style, Fore

class Student(User):

    def __init__(self, username, password, name):
        super().__init__(username, password, name)


    def student_log_validation():
        try:
            file_path = Student.get_student_file_path()
            file_exist = os.path.exists(file_path)

            if not file_exist:
                raise FileNotFoundError


            student_validation = {}
            with open(file_path, 'r') as fr:
                reader = csv.reader(fr)

                for row in reader:
                    student_validation[row[1]] = {'password': row[2],
                                            'name': row[3],
                                            'enrollment status': row[4],
                                            'courses': row[5]}

            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()
            counter = 5

            while counter > 0:
                if username in student_validation and password == student_validation[username]["password"]:
                    print()
                    print(f"Welcome {student_validation[username]['name']}".title())
                    return student_validation[username]['name']

                else:
                    counter -= 1
                    print()
                    print(f"Please Try Again: {counter} Attempts Remain")

                if counter == 0:
                    print(f"== Login Unsuccessful --- {datetime.now().strftime('%I:%M %p')} ==")
                    return False

                else:
                    username = input("Enter Username: ").strip()
                    password = input("Enter Password: ").strip()

        except IndexError:
            Student.index_error()

        except FileNotFoundError:
            Student.file_not_found()

        except Warning:
            print("== Fields cannot be blank ==\nReturning to main menu...")


    def view_classes(name):
        file_path = Student.get_student_file_path()
        file_exists = os.path.exists(file_path)
        try:
            if not file_exists:
                raise FileNotFoundError

            with open(file_path, 'r') as fr:
                reader = csv.DictReader(fr)

                for row in reader:
                    if row['name'] == name:
                        if row['courses'] == '':
                            print("== Not Enrolled ==")
                        else:
                            print("You are enrolled in: ")
                            courses = row['courses'].split(";")
                            for course in courses:
                                print(course)
                        break

        except FileNotFoundError:
            Student.file_not_found()


    def enroll(name):
        try:
            file_exists = os.path.exists(Student.get_student_file_path())
            if not file_exists:
                raise FileNotFoundError

            selected_classes = []
            updated_rows = []
            already_enrolled = False
            available_course = []

            with open(Student.get_student_file_path(), 'r') as fr:
                student_reader = csv.reader(fr)
                for row in student_reader:
                    updated_rows.append(row)
                    if row[3] == name:
                        if row[4] == "True":
                            already_enrolled = True
                            print(Style.BRIGHT + Fore.YELLOW + "== Already Enrolled ==\nReturning to main menu...", Style.RESET_ALL)
                            return

                if not already_enrolled:
                    with open(os.path.join('adminFolder', 'courses.csv')) as fr:
                        reader = csv.reader(fr)
                        next(reader, None)
                        for row in reader:
                            available_course.append(row[1])

                    courses_exits = len(available_course)
                    counter = 3
                    if courses_exits < 3:
                        counter = len(available_course)

                    if courses_exits == 0:
                        raise Warning("== No classes available at this time ==\nContact Admin with Questions\nReturning to main menu...")

                    else:
                        print("Pick from the classes below: ")
                        for key, value in enumerate(available_course, start=1):
                            print(f"{key}: {value}")

                        while counter > 0:
                            class_choice = input(f"Choose {counter} more classes:> ")
                            if class_choice.isdigit() and 1 <= int(class_choice) <= len(available_course) and class_choice not in selected_classes:
                                selected_classes.append(class_choice)
                                counter -= 1
                            else:
                                print("== There was an error processing your request ==\nReturning to main menu...")

                            if counter == 0:
                                with open(Student.get_student_file_path(), 'w', newline='') as fw:
                                    fieldnames = ['student IDN','username', 'password', 'name', 'enrollment status', 'courses', 'last updated']
                                    writer = csv.DictWriter(fw, fieldnames=fieldnames)
                                    for row in updated_rows:
                                        if row[3] == name:
                                            writer.writerow({
                                                'student IDN': row[0],
                                                'username': row[1],
                                                'password': row[2],
                                                'name': row[3],
                                                'enrollment status': "True",
                                                'courses': ";".join([available_course[int(choice) - 1] for choice in selected_classes]),
                                                'last updated': datetime.now().replace(microsecond=0)
                                            })
                                        else:
                                            writer.writerow({
                                                'student IDN': row[0],
                                                'username': row[1],
                                                'password': row[2],
                                                'name': row[3],
                                                'enrollment status': row[4],
                                                'courses': row[5],
                                                'last updated': row[6]
                                            })
                                    print(Style.BRIGHT + Fore.GREEN + "== Course(s) successfully added ==\nReturning to main menu...", Style.RESET_ALL)
        except FileNotFoundError:
            Student.file_not_found()

        except Exception as e:
            print(f"An error occurred: {e}")