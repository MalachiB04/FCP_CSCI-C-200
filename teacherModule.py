from colorama import Fore, Style
print(Fore.CYAN + Style.BRIGHT + "Welcome to Python INDY! (Teacher)" + Style.RESET_ALL)
from teacherClass import Teacher

teacher_login = Teacher.teacher_log_validation()
try:
    if teacher_login:
        print()
        Teacher.view_courses(teacher_login)
        print()
        print(Style.BRIGHT + Fore.GREEN + '== Thank you ==' + Style.RESET_ALL)

except KeyboardInterrupt:
    print("...\nUh oh! It broke! Refresh and try again! ")

