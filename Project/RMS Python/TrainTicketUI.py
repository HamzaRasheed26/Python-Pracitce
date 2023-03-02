import os
from RMSUI import RMSUI
from TrainTicketDL import TrainTicketDL
from TrainTicket import TrainTicket

class TrainTicketUI:

    # function for buying ticket of train
    @staticmethod
    def buy_ticket( route):
        
            trainName = ""; fromStation = ""; toStation = ""
            price = 0
            day = 0; month = 0; year = 0; quantity = 0

            trainName = route.trainName

            os.system("cls")
            RMSUI.head()

            print(" User >> Buy Tickets ")
            print("_____________________________________________________________")
            print()
            print("Train Name :" , trainName)

            # this line print the stations name that are available on this train route
            print("_____________________________________________________________")
            print("Stations available :")
            idx = 1
            for st in route.stations:
                print("\t" , idx , ". " , st.stationName)
                idx += 1

            print("_____________________________________________________________")
            print()
            print(" Select the station from above...")
            print(" ")

            while (True): # this loop run until user enter correct value
                fromStation = input(" From Station : ")
               
                # check station name entered by user is valid or not
                
                if (route.isStationExist(fromStation)):
                    break
                else: # if station name does not match
                    print(" Invalid Station Name !")
                    print(" Again Input ")
            while (True): # this loop run until user enter correct value
                toStation = input(" To Station :")
                
                # check station name entered by user is valid or not
                if (route.isStationExist(toStation)):
                    break
                else: # if station name does not match
                    print(" Invalid Station Name !")
                    print(" Again Input ")

            while (True): # validation for date
                print(" Enter date ( dd mm yyyy)")
                day = int(input("Day: "))
                month = int(input("Month: "))
                year = int(input("Year: "))
                
                if (TrainTicketDL.isDateValid(day, month, year)):
                    break
                print("\n Invalid Date ! ")
                print(" Again enter date please.")

            print(" Ticket price is :" , route.ticketPrice)

            while (True): # validation for quantity
                quantity = int(input(" Enter quantity of tickets :"))

                if (quantity > 12 or quantity <= 0): # quantity cannot be greater than 12
                   print(" Error You cannot buy more than 12 quantity ! ")
                else:
                    break

            price = route.ticketPrice * quantity

            print("Total price for " , quantity , " tickets :" , price)
            # confirming for buying ticket
            op = input("You want to buy Ticket (1 for yes, 0 for not) :")

            buy = TrainTicket(trainName, fromStation, toStation, quantity, price, 0, day, month, year, 0)
            
            if (TrainTicketUI.buying_ticket_message(op, buy)):
                return buy
            else:
                return None

    # function for printing on screen that ticket buyed
    @staticmethod
    def buying_ticket_message(flag, buy):
            check = False
            if (flag == '1'): # message of buying ticket
                os.system("cls")
                RMSUI.head()
                print(" User >> Buy Tickets ")
                print("_____________________________________________________________")
                print()
                print(" You buy Ticket Succesfully ***")
                print()
                buy.print()
                print(" ****Thanks for buying Ticket****")
                buy.calculateDate()
                check = True
            else: # if not buyed than 
                print()
                print(" Ticket not Buyed !")
                check = False

            print()
            input("Press any key for continue....")
            print()
            return check

    # function for viewing my ticket
    @staticmethod
    def my_tickets( ticketList):
            RMSUI.head()
            print(" User >> My Tickets ")
            print("_____________________________________________________________")
            print()

            if not(TrainTicketUI.print_tickets(ticketList)): # calling function for displaying tickets
                print("No Ticket is buyed")
            print()
            input("Press any key for continue....")
            print()

    # function for displaying tickets on screen
    @staticmethod
    def print_tickets( ticketList):
            flag = 0
            for ticket in ticketList: # loop run for buyed ticket in list
                # if ticket is buyed
                if (ticket.date != 0): # if date is not equal to zero
                    ticket.print()
            # if no ticket is buyed
            if (flag == 0):
                return False
            return True