from time import sleep
import os.path
from MUser import MUser
from MUserDL import MUserDL
from MUserUI import MUserUI

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