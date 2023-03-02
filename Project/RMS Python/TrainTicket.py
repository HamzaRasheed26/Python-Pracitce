from Booking import Booking
class TrainTicket(Booking) : 
    quantity = 0 # for quantity of tickets

    def __init__(self, trainName, fromStation, toStation, quantity, price, booking_no, day, month, year, date): 
        self.quantity = quantity
        Booking.__init__(self, trainName, fromStation, toStation, price, booking_no, day, month, year, date)

    def getQuantity(self):
        return self.quantity
    def setQuantity(self, quantity):
        self.quantity = quantity

    def print(self):
        print("  *** Ticket no. " , self.booking_no , " ***")
        print("   Train    : " , self.trainName)
        print("   From     : " , self.fromStation)
        print("   To       : " , self.toStation)
        print("   Date     : " , self.day , "-" , self.month , "-" , self.year)
        print("   Quantity : " , self.quantity)
        print("   Price    : " , self.price)
        print("\n")