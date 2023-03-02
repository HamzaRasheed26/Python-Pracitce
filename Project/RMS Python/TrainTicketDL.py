import os.path
from TrainTicket import TrainTicket

class TrainTicketDL:
    
    ticketList =[]

    @staticmethod
    def addIntoList( t):
        TrainTicketDL.ticketList.append(t)

    @staticmethod
    def getTicketList():
        return TrainTicketDL.ticketList

    @staticmethod
    def getSingleObject( index):        
        if(index >= 0 and index < TrainTicketDL.ticketList.count ):
            return TrainTicketDL.ticketList[index]
        return None

    @staticmethod
    def ListCount():
        return len(TrainTicketDL.ticketList)

    @staticmethod
    def loadDataFromFile( path):
        if(os.path.exists(path)):
            file = open(path, 'r')
            records = file.read().split("\n")
            file.close()

            for line in records :
                splittedRecord = line.split(',')
                traiName = splittedRecord[0];       # ticket train name
                fromStation = splittedRecord[1];    # departure station
                toStation = splittedRecord[2];      # arrival station
                quantity = int(splittedRecord[3]);  # quantity of tickets
                ticket_no = int(splittedRecord[4]); # ticket number
                price = int(splittedRecord[5]);     # price of tickets
                day = int(splittedRecord[6]);       # day of ticket
                month = int(splittedRecord[7]);     # month of ticket
                year = int(splittedRecord[8]);      # year of ticket
                date = float(splittedRecord[9]);    # calculated date for applying conditions
                # temporary for reding from files
                temp = TrainTicket(traiName, fromStation, toStation, quantity, price, ticket_no, month, day, year, date)
                TrainTicketDL.addIntoList(temp) # adding in the list of buyed tickets
                

    @staticmethod
    def storeDataIntoFile( path):
        # writing tickets data into file
        file = open(path, 'w')
        idx = 0
            
        for t in TrainTicketDL.ticketList :
            file.write(t.trainName + "," + t.fromStation + "," + t.toStation + ",")
            file.write(t.quantity + "," + t.booking_no + "," + t.price + ",")
            file.write(t.day + "," + t.month + "," + t.year + "," + t.date + ",")
                
            if (idx < TrainTicketDL.ticketList.count - 1):
                file.write("\n")
            idx += 1
        file.close()
       
        
    @staticmethod
    def sortTicketList():
        if (TrainTicketDL.ticketList != None):
            import operator
            sortedTicketList = sorted(TrainTicketDL.ticketList, key=operator.attrgetter('date'))
            return sortedTicketList    
        return None

    @staticmethod
    def isDateValid( d, m, y):
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
        return True