class Station:

    stationName = ""
    ath = 0
    atm = 0
    dth = 0
    dtm = 0

    def __init__(self, stationName, ath, atm, dth, dtm):
        self.stationName = stationName
        self.ath = ath
        self.atm = atm
        self.dth = dth
        self.dtm = dtm

    def getStationName(self):
        return self.stationName
    def setStationName(self, stationName):
        self.stationName = stationName

    def getAth(self):
        return self.ath
    def setAth(self, ath):
        self.ath = ath

    def getAtm(self):
        return self.atm
    def setAtm(self, atm):
        self.atm = atm

    def getDth(self):
        return self.dth
    def setDth(self, dth):
        self.dth = dth

    def getDtm(self):
        return self.dtm
    def setDtm(self, dtm):
        self.dtm = dtm

    def print(self):
        print(" " , self.stationName , "\t" , self.ath , "\t" , self.atm , "\t" , self.dth , "\t" , self.dtm)