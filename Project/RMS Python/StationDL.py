import os.path

class StationDL:
    
    stationsList = []

    @staticmethod
    def getList():
        return StationDL.stationsList

    @staticmethod
    def GetSingleSingleByIndex( idx):
        if (idx >= 0 and idx < len(StationDL.stationsList)):
            return StationDL.stationsList[idx]
        return None

    @staticmethod
    def addIntoList( station):
        StationDL.stationsList.append(station)

    # function for adding new station in array
    @staticmethod
    def add_station_to_array( st):
        n1 = 0
        for  station in StationDL.stationsList: # loop for checking is name already exist or not
            if (station != st): # checking name in station 1 array
                n1 += 1
                if (n1 == len(StationDL.stationsList)): # if name does not find
                    StationDL.stationsList.append(st) # than add it in array

    @staticmethod
    def loadDataFromFile( path):
        if(os.path.exists(path)):
            fileVariable = open(path, 'r')
            records = fileVariable.read().split("\n")
            fileVariable.close()
            
            for line in records:
                StationDL.addIntoList(line)

    @staticmethod
    def storeDataIntoFile( path):
        # writing stations names into file
        fileVariable = open(path, 'w')
       
        for idx in len(StationDL.stationsList):
            fileVariable.write(StationDL.stationsList[idx])
            if (idx < len(StationDL.stationsList)-1):
                fileVariable.write("/n")
        fileVariable.close()

    # view station schedule that wich trains come on station function
    @staticmethod
    def station_schedule_menu( name):
        # in place of "name" there we pass "user/admin" from function call
        print(" " , name , " >> View Station Schedule  ")
        print("_____________________________________________________________")
        print("Select any from available stations......")
        # stations name available
        a = 1
        # loop for showing all stations name from array
        for station in StationDL.stationsList:
            print(" " , a , ". " , station)
            a += 1

        sub_op = ""

        while (True): # loop run until user enter correct option
            sub_op = input("Your Option.....:")

            if (sub_op >= '1' and int(sub_op) <= a + 47): # if option is correct than break
                break
            else: # if option is incorrect than take input again
                print("\nInvalid option ! ")
                print("Again select the option ")   
        op = int(sub_op)
        return op

    # function for serching the given stations in the stations of trains
    @staticmethod
    def train_station_check( name, route, station):
        # in place of "name" there we pass "user/admin" from function call
        print(" " , name , " >> View Station Schedule ")
        print("_____________________________________________________________")
        print()
        print("Station Name : " , station)
        print()
        print("Train Name\t\tArrival\tDeparture ")

        for r in route: # loop run for all train station array
            r.findStation(station)
            
        print()
        input("Press any key for continue....")
        print()