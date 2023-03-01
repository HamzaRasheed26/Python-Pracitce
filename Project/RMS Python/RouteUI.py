import os
from RMSUI import RMSUI
from StationUI import StationUI
from StationDL import StationDL
from Route import Route
from RouteDL import RouteDL

class RouteUI:
    
    # List of trains for selection of only one train from list function
    @staticmethod
    def list_of_trains( name, title, routeList):
        a = 1
        op = 0

        RMSUI.head()
        # in place of "name" there we pass "user/admin" from function call
        # or in place of "title" we pass the title accordimg to our need in program
        print(" ", name, " >> ", title)
        print("_____________________________________________________________")
        print()
        print(" Select any Train from the following.....")
        print()
        print("Train names:")
        print()

        for route in routeList: # for printing train names from array
            print(" ",a ,". ", route.trainName)
            a += 1

        while (True): # loop run until user eneter correct value
            print()
            op = int(input("Select one option.....:"))

            if (op > a - 1 or op <= 0): # if user enter wrong value
                print("\nInvalid Option !")
                print("Again Input ")
            else: # if correct value than break
                break
        op -= 1
        return op

    # view train routeCount station name and arrival departure times function
    @staticmethod
    def view_train_route_detail( name, title, route):
        # in place of "name" there we pass "user/admin" from function call
        # or in place of "title" we pass the title accordimg to our need in program
        print(" " , name , " >> " , title)
        print("_____________________________________________________________")
        print()
        print(" Train Name : " , route.trainName)
        print()

        # printing the stations name their arrival times and departure time
        print(" Stations\tArrival\t\tDeparture ")
        print()

        for st in route.stations:
            st.print()

        print()
        input(" Press any key for continue....")
        print()
        

    # Add new train route function
    @staticmethod
    def add_train_route():
        ticketPrice = ""
        cargoPrice = ""

        stations = []

        print(" Admin >> Add new Train Route")
        print("_____________________________________________________________")
        print()
        trainName = input(" Enter train name :") # train name

        entry = True
        count = 1
        while (entry):
            
            print(" *** For Station " , count)

            station = StationUI.takeStationInput()

            StationDL.add_station_to_array(station.stationName) # calling an functin for adding station to stations array
            stations.append(station)
            count += 1
            if (count > 4):
                op = input("\n Do You want to add another station...(y/n)...:")
                if (op != "y" or op != "Y"):
                    break
                    
        while (True): # validation on correcrt ticket price
            ticketPrice = int(input(" Set Ticket Price :")) # ticket price for train

            if (ticketPrice <= 2000 and ticketPrice > 100): # must be less than 2000 and greater than 100
                break
            print(" Train Ticket Price Cannot be greater than 2000 Rs and cannot be less than 100 Rs. ")

        while (True): # validation on correcrt cargo price
            cargoPrice = int(input(" Set cargo rate per kg :")) # cargo rate for that train

            if (cargoPrice <= 500 and cargoPrice > 0): # must be less than 500 and greater than 0
                break
            print(" Price must be less than 500 per kg and greater than 0.")

        print()
        print("*** New Route Successfully Added ***")

        takeData = Route(trainName, stations, ticketPrice, cargoPrice)
        return takeData

    # function for daleting already exist rout
    @staticmethod
    def delete_route(trainName):
        flag = ""
        check = False

        print()
        # asking are you sure
        print("Are you sure you want to delete the route! ")
        flag = input("Press 1 for Yes or Press any key for Not ")

        if (flag == '1'): # if he want to delete route
            print("\n Route : " , trainName)
            print(" *** Deleted Successfully *** ")
            check = True
        else:
            check = False
        print()
        input("Press any key for continue....")
        print()
        return check

    # Function for changing already exist Train nam
    @staticmethod
    def  change_train_name( oldName):
        print("\n\n")
        print(" Old Train Name " , oldName) # old train name
        trainName = ""
        while (True):
                
            trainName = input(" Enter New train name ") # taking input of new trin name

            if(trainName == oldName):
                break
            elif(RouteDL.isTrainNameExist(trainName)):
                print()
                print(" This Train already exist !")
                print(" Enter another name ")
            else:  # if name met all conditions than change name
                #routeList[idx].changeTrainName(trainName);
                break

        print(" Train name changed Succesfully.")
        print()
        input("Press any key for continue....")
        print()
        return trainName

    # function for changing stations of alraedy exist train route
    @staticmethod
    def change_train_stations( route):
        print()
        print("Train Name : " , route.trainName)

        stationList = []

        y = 1
        for station in route.stations :
            print(" *** For Station " , y )
            print("Old Station " , y , " Name : " , station)
            y += 1
            station = StationUI.takeStationInput()

            StationDL.add_station_to_array(station.stationName) # calling an functin for adding station to stations array
            stationList.append(station)

        print(" Train Stations changed Succesfully.")
        print()
        input("Press any key for continue....")
        print()

        return stationList

    # set ticket prices function
    @staticmethod
    def set_ticket_price( route):
        print(" Admin >> Set Ticket Prices")
        print("_____________________________________________________________")
        print()
        print(" Train Name : " , route.trainName)
        print(" Old ticket price is : " , route.ticketPrice) # old price of ticket
        while (True):
            price = int(input(" Enter new ticket price :")) # taking input new price of ticket
            if (route.setTicketPrice(price)): # must be less than 2000 and greater than 100
                break
            print(" You can not enter price more than 2000 and less than 100. ")

    # set freight prices of trains function
    @staticmethod
    def set_freight_rate( route):
        print(" Admin >> Set Freight Rate ")
        print("_____________________________________________________________")
        print()
        print("Train Name : " , route.trainName)
        print()
        print("Old cargo rate of train : " , route.cargoPrice) # old price of cargo
        while (True):
            price = int(input("Enter new cargo rate per kg :")) # taking input new price of cargo
            if (route.setCargoPrice(price)): # must be less than 500 and greater than 0
                break
            print("You cannot enter rate more than 500 per kg and less than 0.")

    # function for viewing tickets pries of trains
    @staticmethod
    def view_tickets_price( routeList):
        RMSUI.head()

        print(" User >> View Tickets Price ")
        print("_____________________________________________________________")
        print("Train Name\t\tTicket Price")
        print()

        a = 1
        # prints all train names with their tickets prices
        for route in routeList:
            print(" " , a , ". " , route.trainName , "\t\t" , route.ticketPrice)
            a = a + 1
        print()
        input("Press any key for continue....")
        print()

    # function for displaying prices of freight/cargo
    @staticmethod
    def view_freight_rate( routeList):
        RMSUI.head()
        print(" User >> View Freight Rates ")
        print("_____________________________________________________________")
        print()
        print("Train Name\t\tRate/kg   ")
        print()

        a = 1
        # prints all train names with their cargo/freight prices per kg
        for route in routeList:
            print(" " , a , ". " , route.trainName , "\t" , route.cargoPrice)
            a += 1

        print()
        input("Press any key for continue....")
        print()

    # function for edit already exist route
    @staticmethod
    def edit_route():
        option = ""
        RMSUI.head()
        print(" Admin >> Edit Route ")
        print("_____________________________________________________________")
        print()

        print(" 1. Delete Route ")
        print(" 2. Modify Route ")
        print(" 3. Exit ")

        while (True): # validation on option
            option = input("\n Your Option : ")

            if (option >= '1' and option <= '3'):
                return option # return option selected
            print(" Invalid Option! ")
            print(" Again Input ")


    # function for mofdify all ready exist train route
    @staticmethod
    def modify_route():
        os.system("cls")
        RMSUI.head()
        print(" Admin >> Modify Route ")
        print("_____________________________________________________________")
        print()
        print(" 1. Change Train Name ")
        print(" 2. Change Stations ")
        print(" 3. Exit ")
        op = ""
        while (True): # validation on option
            op = input(" Your Option... : ")
            if (op >= '1' and op <= '3'):
                return op