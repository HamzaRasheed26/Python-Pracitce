class MUser:
    username = ""
    password = ""
    role = ""

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def isAdmin(self):
        if(self.role == "Admin" or self.role == "admin"):
            return True
        else:
            return False

import os.path

class MUserDL:
    usersList = []

    @staticmethod
    def addUserIntoList(user):
        MUserDL.usersList.append(user)

    @staticmethod
    def SignIn(user):
        for storedUser in MUserDL.usersList:
            if(storedUser.username == user.username and storedUser.password == user.password):
                return storedUser
        return None

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readDataFromFile(path):
        if (os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            for line in records:
                username, password, role = MUserDL.parseData(line)
                user = MUser(username, password, role)
                MUserDL.addUserIntoList(user)
            return True
        else:
            return False

    @staticmethod
    def storeUserIntoFile(user, path):
        file = open(path, 'a')
        file.write("\n" + user.username + "," + user.password + "," + user.role)
        file.close()


class MUserUI:
    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignUp")
        option = int(input("Enter Option :"))
        return option

    @staticmethod
    def printList(usersList):
        for user in usersList:
            print(user.username, user.password, user.role)

    @staticmethod
    def TakeInputFromConsole():
        username = input("Enter UserName :")
        password = input("Enter UserPassword :")
        role = input("Enter UserRole :")
        user = MUser(username, password, role)
        return user

    @staticmethod
    def takeInputwithOutRole():
        username = input("Enter UserName :")
        password = input("Enter UserPassword :")
        user = MUser(username, password, None)
        return user

from time import sleep
# Defining Main Function
def main():
    path = "User.txt"
    MUserDL.readDataFromFile(path)
    option = 0
    while (option != 3):
        os.system("cls")
        option = MUserUI.menu()
        if (option == 1):
            user = MUserUI.takeInputwithOutRole()
            user = MUserDL.SignIn(user)
            if (user != None):
                if (user.isAdmin()):
                    print("This is Admin")
                    #Admin Menu
                else:
                    print("This is User")
                    #User Menu
                sleep(2)
        elif (option == 2):
            user = MUserUI.TakeInputFromConsole()
            MUserDL.addUserIntoList(user)
            MUserDL.storeUserIntoFile(user, path)


# Calling Main Function as the Code starts executing
if __name__ == "__main__":
    main()