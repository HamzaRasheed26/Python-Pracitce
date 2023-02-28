from MUser import MUser
from MUserDL import MUserDL
from RMSUI import RMSUI
import os

class MUserUI:
    
    @staticmethod
    def SignUp():
        os.system("cls")
        username = input("Enter your Name : ")
        password = input("Enter Pasword : ")
        role = "user"
        user =  MUser(username, password, role)
        return user
        
    @staticmethod
    def signin():
        os.system("cls")
        RMSUI.head()
        username = input("Enter your Name : ")
        password = input("Enter Pasword : ")
        user =  MUser(username, password, None)
        return user

    @staticmethod
    def LoginPage():
        os.system("cls")
        RMSUI.head()
        print(" Login Page >>")
        print(" 1. Sign In")
        print(" 2. Sign Up")
        print(" 3. Exit")
        option = input("Your Option : ")
        return option
