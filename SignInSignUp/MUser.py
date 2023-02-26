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
