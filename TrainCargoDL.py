import os.path
from TrainCargo import TrainCargo

class TrainCargoDL:
    cargoList = []

    @staticmethod
    def addIntoList( cargo):
        TrainCargoDL.cargoList.append(cargo)

    @staticmethod
    def getCargoList():
        return TrainCargoDL.cargoList

    @staticmethod
    def getSingleObject( index):
        if(index >= 0 or index < TrainCargoDL.cargoList.count):
            return TrainCargoDL.cargoList[index]
        return None

    @staticmethod
    def ListCount():
        return len(TrainCargoDL.cargoList)

    @staticmethod
    def parseData(line):
        line = line.split(",")
        return line

    @staticmethod
    def loadDataFromFile( path):
        if(os.path.exists(path)):
            file = open(path, 'r')
            records = file.read().split("\n")
            file.close()

            for line in records :
                splittedRecord = line.split(',')
                TrainName = splittedRecord[0];       # cargo booked train name
                From = splittedRecord[1];            # departure station
                To = splittedRecord[2];              # arrival station
                Weight = int(splittedRecord[3]);     # weight of cargo
                Price = int(splittedRecord[4]);      # cargo booking price
                Booking_no = int(splittedRecord[5]); # booking number
                day = float(splittedRecord[6]);      # booking day
                month = float(splittedRecord[7]);    # booking month
                year = float(splittedRecord[8]);     # booking year
                date = float(splittedRecord[9]);     # calculated date for applying conditions
                cargo =  TrainCargo(TrainName, From, To, Weight, Price, Booking_no, day, month, year, date)

                TrainCargoDL.addIntoList(cargo) # adding into list of bookaed cargos


    @staticmethod
    def storeDataIntoFile( path):
        # writing cargo booking data into file
        file = open(path, 'w')
        idx = 0

        for c in TrainCargoDL.cargoList:
            file.write(c.trainName + "," + c.fromStation + "," + c.toStation + ",")
            file.write(c.weight + "," + c.price + "," + c.booking_no + ",")
            file.write(c.day + "," + c.month + "," + c.year + "," + c.date + ",")

            if (idx < TrainCargoDL.cargoList.count - 1):
                file.write("\n")
            idx += 1
        file.close() # closing file

    @staticmethod
    def sortCargoList():
        if (TrainCargoDL.cargoList != None):
            import operator
            sortedCargoList = sorted(TrainCargoDL.cargoList, key=operator.attrgetter('date'))
            return sortedCargoList
        return None

    # function for displaying booked cargo on screen
    @staticmethod
    def print_booked_cargo( sortedCargoList):
        flag = 0
        for c in sortedCargoList: # loop run for booked cargo
            # if ticket is buyed
            if (c.date != 0): # if date is not equal to zero
                c.print()
                flag += 1

        # if no ticket is buyed
        if (flag == 0):
            return False
        return True

    @staticmethod
    def isDateValid( d,  m,  y):
        # check on year 
        if (y >= 2022):
            # check on month
            if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
                # check on day range from 1 to 31
                if (d >= 1 and d <= 31):
                    return True
            # check on month
            elif (m == 4 or m == 6 or m == 9 or m == 11):
                # check on  day range from 1 to 30
                if (d >= 1 and d <= 30):
                    return True
            # check on month of febuary
            elif (m == 2):
                # check on day range from 1 to 28
                if (d >= 1 and d <= 28):
                    return True
        return False