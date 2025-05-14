import csv
from datetime import datetime
import os
from userClass import User

class Teacher(User):
    def __init__(self, name, username, password):
        super().__init__(name, username, password)

    def teacher_log_validation():
        try:
            file_exists = os.path.exists(Teacher.path_for_teacher())
            if not file_exists:
                raise FileNotFoundError
            else:
                counter = 5
                while counter > 0:
                    username = input('Enter Username: ')
                    password = input('Enter Password: ')
                    with open(Teacher.path_for_teacher(), 'r') as fr:
                        reader = csv.DictReader(fr)
                        for row in reader:
                            if row['username'] == username:
                                if row['password'] == password:
                                    print(f"Login Successful! Welcome {row['name']}")
                                    return row['name']
                                    print()
                                else:
                                    login = False
                            else:
                                login = False

                        if not login:
                            counter -= 1
                            print()
                            print(f"Please Try Again: {counter} Attempts Remain")

                        if counter == 0:
                            print(f"ERROR: Login Unsuccessful --- {datetime.now().replace(microsecond=0)}")
                            return False
        except FileNotFoundError:
            Teacher.file_not_found()

        except IndexError:
            Teacher.index_error()


    def view_courses(name):
        file_exist_teacher = os.path.exists(Teacher.path_for_teacher())
        file_path_course = os.path.join('adminFolder', 'courses.csv')
        file_exist_course = os.path.exists(file_path_course)
        teacher_name = ''

        if not file_exist_teacher or not file_exist_course:
            raise FileNotFoundError
        else:
            with open(Teacher.path_for_teacher(), 'r') as fr:
                reader = csv.reader(fr)
                for row in reader:
                    if row[3] == name:
                        teacher_name = name

                with open(file_path_course, 'r') as fr:
                    reader = csv.reader(fr)
                    for row in reader:
                        if row[2] in teacher_name:
                            print(f"You are teaching: {row[1]}")