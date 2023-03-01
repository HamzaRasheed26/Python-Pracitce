import os.path
from Station import Station
from Route import Route

class RouteDL:
    
    routeList = []

    @staticmethod
    def getRouteList():
        return RouteDL.routeList

    @staticmethod
    def GetSingleRouteByIndex( idx):
        count = len(RouteDL.routeList)
        if(idx >= 0 and idx < count):
            return RouteDL.routeList[idx]
        return None

    @staticmethod
    def addIntoList( r):
        RouteDL.routeList.append(r)

    @staticmethod
    def removeFromList( index):
        RouteDL.routeList.pop(index)

    @staticmethod
    def isTrainNameExist( trainName):
        for r in RouteDL.routeList:
            if(trainName == r.trainName):
                return True
        return False

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line

    @staticmethod
    def LoadDataFromFile( path):
        
        if(os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()

            for line in records:
                splittedRecord = line.split(",")
                x=0
                trainName = splittedRecord[x]
                x += 1
                count = int(splittedRecord[x])
                x += 1
                stations = []
                for i in range(0, count):
                    stationName = splittedRecord[x]
                    x += 1
                    ath = int(splittedRecord[x])
                    x += 1
                    atm = int(splittedRecord[x])
                    x += 1
                    dth = int(splittedRecord[x])
                    x += 1
                    dtm = int(splittedRecord[x])
                    x += 1
                    stations.append(Station(stationName, ath, atm, dth, dtm))
                ticketPrice = int(splittedRecord[x])
                x += 1
                cargoPrice = int(splittedRecord[x])
                x += 1

                readRoute = Route(trainName, stations, ticketPrice, cargoPrice) # temporary for reding from files

                RouteDL.addIntoList(readRoute) # adding in the list of routes of 
            return True
        else:
            return False

    @staticmethod
    def storeDataIntoFlie( path):
        # writing data of train routeCount into file
        file = open(path, 'w')
        idx = 0
        for  r in RouteDL.routeList :  #   changing index of arrays
            file.write(r.trainName + "," + r.stations.count + ",")
            for st in r.stations:
                file.write(st.stationName + ",")
                file.write(st.ath + "," + st.atm + "," + st.dth + "," + st.dtm + ",")
            file.write(r.ticketPrice + "," + r.cargoPrice + ",")
            if (idx < RouteDL.routeList.count - 1):
                file.write("\n")
            idx += 1
        file.close() # closing file