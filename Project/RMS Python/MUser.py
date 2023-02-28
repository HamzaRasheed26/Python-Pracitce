
class MUser:
    username = ""
    password = ""
    role = ""

    def __init__(self,  username,  password, role ):
        self.username = username
        self.password = password
        self.role = role

        #def MUser(string username, string password, string role)
       # {
        #    this.username = username;
         #   this.password = password;
          #  this.role = role;
       # }

    def getUsername(self):
        return self.username
        
    def getPassword(self):
        return self.password
    
    def getRole(self):
        return self.role

    def setUsername(self,username):
        self.username = username
        
    def setPassword(self, password):
        self.password = password
        
    def setRole(self, role):
        self.role = role