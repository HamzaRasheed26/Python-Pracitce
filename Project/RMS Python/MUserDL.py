import os.path
from MUser import MUser
from CustomerDL import CustomerDL

class MUserDL:
    
    UsersList = []

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line[0], line[1], line[2]

    @staticmethod
    def readData( path):
        
        if(os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()

            for line in records:
                name, password, role = MUserDL.parseData(line)
                user = MUser(name, password, role)
                MUserDL.AddUserIntoList(user)
            return True
        else:
            return False

    @staticmethod
    def storeData( path):
        
        file = open(path, 'w')
        i = 0
        for user in MUserDL.UsersList:
            i += 1
            file.write(user.username + "," + user.password + "," + user.role )
            if (i < len(MUserDL.UsersList)):
                file.write("\n")
        file.close()

    @staticmethod
    def AddUserIntoList( User):
        MUserDL.UsersList.append(User)

    @staticmethod
    def isExist( u):
        for user in MUserDL.UsersList:
            if (user.getUsername() == u.getUsername() and user.getPassword() == u.getPassword()):
                return True
        return False

    @staticmethod
    def findUser( user):
        for u in MUserDL.UsersList:
            if (user.getUsername() == u.getUsername() and user.getPassword() == u.getPassword()):
                if (user.getRole() == "Customer"):
                    CustomerDL.initializeCustomer(u.getUsername())
                return u
        return None