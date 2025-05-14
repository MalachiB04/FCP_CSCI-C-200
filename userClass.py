import os 
from colorama import Style, Fore
import csv

class User:
    def __init__(self, name, username, password): 
        self.username = username
        self.password = password
        self.name = name
    
    def __str__(self): 
        return f'Name: {self.name}\nUsername: {self.username}\nPassword: {self.password}'
    
    def set_username(self,username): 
        self.username = username
    
    def set_password(self, password):
        self.password = password
    
    def set_name(self, name): 
        self.name = name


    def get_username(self): 
        return self.username
    
    def get_password(self):
        return self.password
    
    def get_name(self): 
        return self.name
    

    def path_for_teacher(): 
        return os.path.join('adminFolder', 'teacherFolder', 'teacherLogin.csv' )

    def get_student_file_path():
        return os.path.join(os.getcwd(), 'adminFolder', 'studentFolder', 'studentLog.csv')
    
    def input_error_message(): 
        print(Style.BRIGHT + Fore.RED + '== Invalid Input ==' + Style.RESET_ALL)
    
    def file_not_found(): 
        print(Style.BRIGHT + Fore.RED + "== Unable to connect to Database ==" + Style.RESET_ALL)
    
    def index_error(): 
        print(Style.BRIGHT + Fore.RED + "== Unable to connect to Database ==" + Style.RESET_ALL)