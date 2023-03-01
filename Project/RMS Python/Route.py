class Route:
    # for train names
    trainName = ""
    stations = []
    # for prices of trains tickets
    ticketPrice = 0
    # for prices of trains freight rate
    cargoPrice = 0

    def __init__(self, trainName, stations, ticketPrice, cargoPrice):
        self.trainName = trainName
        self.stations = stations
        self.ticketPrice = ticketPrice
        self.cargoPrice = cargoPrice

    def getTrainName(self):
        return self.trainName
    def setTrainName(self, trainName):
        self.trainName = trainName

    def getStations(self):
        return self.stations
    def setStations(self, stations):
        self.stations = stations

    def getTicketPric(self):
        return self.ticketPrice
    def setTicketPrice(self, ticketPrice):
        self.ticketPrice = ticketPrice
    
    def getCargoPrice(self):
        return self.cargoPrice
    def setCargoPrice(self, cargoPrice):
        self.cargoPrice = cargoPrice

    # -------------------  Member Function ----------------------------------
    def setTicketPrice(self, price):
        if (price <= 2000 and price >= 100): # must be less than 2000 and greater than 100
            self.ticketPrice = price
            return True    
        return False

    def setCargoPrice(self, price):
        if (price <= 500 and price > 0): # must be less than 500 and greater than 0
            self.cargoPrice = price
            return True
        return False

    def isStationExist(self, name):
        for st in self.stations:
            if (name == st.stationName):
                return True
        return False
        
    def findStation(self, st):
        for station in self.stations:
            if (st == station.stationName): # it search the required station in ts1 array
                print(self.trainName , "\t\t" , station.ath , ":" , station.atm , "\t" , station.dth , ":" , station.dtm)
                return True
        return False