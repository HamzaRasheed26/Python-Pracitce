class MUser:
    username = ""
    password = ""
    role = ""

    def init (self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def isAdmin(self):
        if(self.role == "Admin"):
            return True
        else:
            return False

import os.path

class MUserDL:
    usersList = []

    @staticmethod
    def addUserIntoList(user):
        MUserDL.UserList.append(user)

    @staticmethod
    def SignIn(user):
        for storedUser in MUserDL.usersList:
            if(storedUser.userName == user.userName and storedUser.userPassword == user.userPassword):
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
                userName, userPassword, userRole = MUserDL.parseData(line)
                user = MUser(userName, userPassword, userRole)
                MUserDL.addUserIntoList(user)
            return True
        else:
            return False

    @staticmethod
    def storeUserIntoFile(user, path):
        file = open(path, 'a')
        file.write("\n" + user.userName + "," +
        user.userPassword + "," + user.userRole)
        file.close()


class MUserUI:
    @staticmethod
    def menu():
        print("1. SignIn")
        print("2. SignUp")
        print("Enter Option")
        option = int(input())
        return option

    @staticmethod
    def printList(usersList):
        for user in usersList:
            print(user.userName, user.userPassword, user.userRole)

    @staticmethod
    def TakeInputFromConsole():
        userName = input("Enter UserName")
        userPassword = input("Enter UserPassword")
        userRole = input("Enter UserRole")
        user = MUser(userName, userPassword, userRole)
        return user

    @staticmethod
    def takeInputwithOutRole():
        userName = input("Enter UserName")
        userPassword = input("Enter UserPassword")
        user = MUser(userName, userPassword, None)
        return user

from time import sleep
# Defining Main Function
def main():
    path = "Data.txt"
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
                sleep(3)
        elif (option == 2):
            user = MUserUI.TakeInputFromConsole()
            MUserDL.addUserIntoList(user)
            MUserDL.storeUserIntoFile(user, path)


# Calling Main Function as the Code starts executing
if __name__ == "__main__":
    main()