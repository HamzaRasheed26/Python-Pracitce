from Booking import Booking
class TrainCargo(Booking):
    weight = 0.0  # for weight of cargo  

    def __init__(self, trainName, fromStation, toStation, weight, price, booking_no, day, month, year, date): 
        self.weight = weight
        Booking.__init__(self, trainName, fromStation, toStation, price, booking_no, day, month, year, date)

    def getWeight(self):
        return self.weight
    def setWeight(self, weight):
        self.weight = weight
    
    def print(self):
        print("  *** Booking no. " , self.booking_no , " ***")
        print("   Train  : " , self.trainName)
        print("   From   : " , self.fromStation)
        print("   To     : " , self.toStation)
        print("   Date   : " , self.day , "-" , self.month , "-" , self.year)
        print("   Weight : " , self.weight)
        print("   Price  : " , self.price)
        print("\n")