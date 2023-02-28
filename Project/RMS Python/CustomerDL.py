import os.path
from Customer import Customer

class CustomerDL:
    
    customerList = []
    presentCustomer = Customer()

    @staticmethod
    def initializeCustomer(self, name):
        CustomerDL.presentCustomer =  Customer(name)   

    @staticmethod
    def getList(self):
        return CustomerDL.customerList

    @staticmethod
    def addIntoList(self, c):
        CustomerDL.customerList.append(c)

    @staticmethod
    def getByIndex(self, index):
        if (index >= 0 and index < CustomerDL.customerList.Count):
            return CustomerDL.customerList[index]
        return None