from MUser import MUser

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
