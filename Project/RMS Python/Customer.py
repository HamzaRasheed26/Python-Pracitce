class Customer:

    name = ""
    cargoBooked = []
    tickets = []

    def init(self, name, cargoBooked,tickets):
        self.name = name
        self.cargoBooked = cargoBooked
        self.tickets = tickets
    
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    
    def getCargoBooked(self):
        return self.cargoBooked
    def setCargoBooked(self, cargoBooked):
        self.cargoBooked =cargoBooked

    def getTickets(self):
        return self.tickets
    def setTickets(self, tickets):
        self.tickets = tickets