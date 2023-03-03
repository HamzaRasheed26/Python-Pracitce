class Booking:

    trainName = ""   # for storing the name of train in which cargo is booked
    fromStation = "" # for storing the name of departure station
    toStation = ""   # for storing the name of arrival station
    price = 0.0      # for cargo deleviring price user have to pay
    booking_no = 0   # for the number of booking
    # for date of booking
    day = 0.0
    month = 0.0
    year = 0.0
    date = 0.0


    def __init__(self, trainName,  fromStation, toStation, price, booking_no, day, month, year, date):
        self.trainName = trainName
        self.fromStation = fromStation
        self.toStation = toStation
        self.price = price
        self.booking_no = booking_no
        self.day = day
        self.month = month
        self.year = year
        self.date = date
        
    def getTrainNmae(self):
        return self.trainName
    def setTrainName(self, trainName):
        self.trainName = trainName
    
    def getFromStation(self):
        return self.fromStation
    def setFromStation(self, fromStation):
        self.fromStation = fromStation

    def getToStation(self):
        return self.toStation
    def setToStation(self, toStation):
        self.toStation = toStation

    def getPrice(self):
        return self.price
    def setPrice(self, price):
        self.price = price

    def getBookingNo(self):
        return self.booking_no
    def setBookingNo(self, bookingNo):
        self.booking_no = bookingNo

    def getDay(self):
        return self.day
    def setDay(self, day):
        self.day = day

    def getMonth(self):
        return self.month
    def setMonth(self, month):
        self.month = month

    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year

    def getDate(self):
        return self.date
    def setDate(self, date):
        self.date = date

    def calculateDate(self):
        self.date = self.day + self.month * 30.417
        return self.date
