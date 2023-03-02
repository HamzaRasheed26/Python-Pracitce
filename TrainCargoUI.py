import os
from RMSUI import RMSUI
from TrainCargoDL import TrainCargoDL
from TrainCargo import TrainCargo

class TrainCargoUI:
    
    # function for booking cargo
    @staticmethod
    def book_cargo( route):
        #TrainCargo read = new TrainCargo();

        trainName = ""; fromStation = ""; toStation = ""
        price = 0; weight = 0
        day = 0; month = 0; year = 0

        os.system("cls")
        RMSUI.head()
        print(" User >> Book Cargo ")
        print("_____________________________________________________________")
        print()
        print("Train Name :" , route.trainName)
        trainName = route.trainName

        # this line print the stations name that are available on this train route
        print("_____________________________________________________________")
        print("Stations available :")
        idx = 1
        for st in route.stations:
            print("\t" , idx  , ". " , st.stationName)
            idx += 1
        print("_____________________________________________________________")
        print()
        print(" Select the station from above...\n")

        while (True): # this loop run until user enter correct value
            fromStation = input(" From Station :")
                
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

            if(TrainCargoDL.isDateValid(day, month, year)):
                break
            print("\n Invalid Date ! ")
            print(" Again enter date please.")
        print()
        print("Price per kg :" , route.cargoPrice)

        while (True): # validation on weight
            weight = float(input("Enter the cargo weight (kg) :"))

            if (weight > 500 or weight <= 0): # user canot enter more than 500 kg weight
                print("You can not add weight more than 500 kg ! ")
                print("Again Input ")
            else: # if less than 500
                break

        # calculkating cargo price by formula
        price = route.cargoPrice * weight

        print()
        print("You have to pay :" , price)
        op = input("You want to book cargo (1 for yes, 0 for not) :")

        readData = TrainCargo(trainName, fromStation, toStation, weight, price, 0, day, month, year,0)

        if (TrainCargoUI.confirming_book_cargo(op, readData)):
            return readData
        else:
            return None

    # function for printing on screen that cargo booked or not
    @staticmethod
    def confirming_book_cargo( flag,  read):
            check = False
            if (flag == '1'): # message of cargo booked
                print()
                os.system("cls")
                RMSUI.head()
                print(" User >> Booked cargo ")
                print("_____________________________________________________________")
                print()
                print(" Your Cargo Booked Succesfully ***")
                print()

                read.print()

                print(" **** Your cargo succesfully booked ***")
                print()
                check = True
            else: # if not booked creating arrays index null
                print()
                print(" Your cargo not booked ! ")
                print()
                check = False

            print()
            input("Press any key for continue....")
            print()
            return check

    @staticmethod
    def my_booked_cargo( sortedCargoList):
            RMSUI.head()
            print(" User >> My Booked Cargo ")
            print("_____________________________________________________________")
            print()

            check = False
            if (sortedCargoList != None):
                check = TrainCargoDL.print_booked_cargo(sortedCargoList) # calling function for displaying tickets
            if(check == False):
                print("  You Have No Cargo Booked ! ")
            print()
            input("  Press any key for continue....")
            print()