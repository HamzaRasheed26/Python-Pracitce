import os;
from RMSUI import RMSUI
from Customer import Customer
from CustomerDL import CustomerDL
from MUserDL import MUserDL
from MUserUI import MUserUI
from RouteDL import RouteDL
from RouteUI import RouteUI
from TrainTicketDL import TrainTicketDL
from TrainTicketUI import TrainTicketUI
from TrainCargoDL import TrainCargoDL
from TrainCargoUI import TrainCargoUI
from StationDL import StationDL

class Program:
        #-----------------------------  main function------------------------------------------
    @staticmethod
    def main():
            path1 = "Train_Routes_Data.txt"
            path2 = "tickets_data.txt"
            path3 = "booked_cargo_data.txt"
            path4 = "stations.txt"
            credentialFilePath = "Credentials.txt"

            MUserDL.readData(credentialFilePath)
            RouteDL.LoadDataFromFile(path1)
            TrainTicketDL.loadDataFromFile(path2)
            TrainCargoDL.loadDataFromFile(path3)
            StationDL.loadDataFromFile(path4)

            #______________________ Data structure _______________
            password = ""

            # -------------------- Actual Program Runs From Here

            Program.load_data( password)

            while (True): # loop for main menu
                # calling login function

                op = MUserUI.LoginPage()

                if (op == '1'):
                    # sign in
                    role = ""
                    u  = MUserUI.signin()
                    user = MUserDL.findUser(u)
                    if (user != None):
                        role = user.getRole()
                    else:
                        role = "nill"

                    # __________________________ Admin Portion ________________________
                    if (role == "admin"):
                        option = ""

                        while (True): # loop for admin option
                            os.system("cls")
                            RMSUI.head()
                            # calling admin menu
                            option = RMSUI.Admin_Menu()
                            os.system("cls")
                            sub_op = ""

                            if (option == '1'):
                                # admin menu option 1 starts

                                # calling function for printing list of trains
                                index = RouteUI.list_of_trains("Admin", "View Train Route", RouteDL.getRouteList())
                                # calling function for further train detail
                                route = RouteDL.GetSingleRouteByIndex(index)
                                os.system("cls")
                                RMSUI.head()
                                RouteUI.view_train_route_detail("Admin", "View Train Route", route)
                                # admin menu option 1 ends

                            elif (option == '2'):
                                # admin menu option 2 starts

                                # function for adding train
                                os.system("cls")
                                RMSUI.head()
                                route = RouteUI.add_train_route()
                                
                                RouteDL.addIntoList(route)
                                # admin menu option 2 ends
                            
                            elif (option == '3'):
                                # admin menu option 3 starts

                                sub_op = RouteUI.edit_route() # menu of edit route

                                if (sub_op == '1'): # for option 1
                                    os.system("cls")

                                    # calling lists of routeCount
                                    index = RouteUI.list_of_trains("Admin", "Delete Route", RouteDL.getRouteList())
                                    route = RouteDL.GetSingleRouteByIndex(index)
                                    if (RouteUI.delete_route(route.trainName)): # deleting route
                                        RouteDL.removeFromList(index)
                                elif (sub_op == '2'): # for option 2
                                    sub_op = RouteUI.modify_route() # modifying route

                                    if (sub_op == '1'):
                                        index = RouteUI.list_of_trains("Admin", "Route Route", RouteDL.getRouteList())
                                        route = RouteDL.GetSingleRouteByIndex(index)
                                        newName = RouteUI.change_train_name(route.trainName) # changing train name
                                        route.trainName = newName
                                    elif (sub_op == '2'):
                                        os.system("cls")
                                        idx = RouteUI.list_of_trains("Admin", "Moify Route", RouteDL.getRouteList())
                                        route = RouteDL.GetSingleRouteByIndex(idx)
                                        stationList = RouteUI.change_train_stations(route) # changing train station
                                        route.stations = stationList

                                # admin menu option 3 ends
                            
                            elif (option == '4'):
                                # admin menu option 4 starts

                                index = RouteUI.list_of_trains("Admin", "View Train Route", RouteDL.getRouteList())
                                os.system("cls")
                                RMSUI.head()

                                r = RouteDL.GetSingleRouteByIndex(index)
                                RouteUI.set_ticket_price(r)

                                # admin menu option 4 ends
                            elif (option == '5'):
                                # admin menu option 5 starts

                                index = RouteUI.list_of_trains("Admin", "View Train Route", RouteDL.getRouteList())
                                os.system("cls")
                                RMSUI.head()

                                route = RouteDL.GetSingleRouteByIndex(index)
                                RouteUI.set_freight_rate(route)

                                # admin menu option 5 ends
                            
                            elif (option == '6'):
                                # admin menu option 6 starts
                                RMSUI.head()
                                index = StationDL.station_schedule_menu("Admin")
                                os.system("cls")
                                RMSUI.head()
                                index -= 1
                                st = StationDL.GetSingleSingleByIndex(index)
                                StationDL.train_station_check("Admin", RouteDL.getRouteList(), st)

                                # admin menu option 6 ends
                            
                            elif (option == '7'):
                                # admin menu option 7 starts

                                RMSUI.add_notice()

                                # admin menu option 7 ends
                            
                            elif (option == '8'):
                                # admin menu option 8 starts

                                RMSUI.view_employers_data()

                                # admin menu option 8 ends
                            
                            elif (option == '9'):
                                # admin menu exit point
                                break
                            else:
                                print("Invalid Input !")
                                input("Press any key for continue....")
                                print()
                    # ________________________ User Portion ______________________________________
                    elif (role == "user"):
                        option = ""
                        while (True):
                            os.system("cls")
                            RMSUI.head()
                            option = RMSUI.user_menu()
                            os.system("cls")

                            if (option == "1"):
                                # user menu option 1 starts

                                index = RouteUI.list_of_trains("User", "View Train Route", RouteDL.getRouteList())
                                route = RouteDL.GetSingleRouteByIndex(index)
                                os.system("cls")
                                RMSUI.head()
                                RouteUI.view_train_route_detail("User", "View Train Route", route)

                                # user menu option 1 ends
                            
                            elif (option == "2"):
                                # user menu option 2 starts

                                RMSUI.head()
                                index = StationDL.station_schedule_menu("User")
                                os.system("cls")
                                RMSUI.head()
                                index -= 1
                                st = StationDL.GetSingleSingleByIndex(index)
                                StationDL.train_station_check("User", RouteDL.getRouteList(), st)

                                #sub_op = station_schedule_menu("User", stations);
                                #train_station_check("User", sub_op, RouteDL.getRouteList(), stations);

                                # user menu option 2 ends
                            
                            elif (option == "3"):
                                # user menu option 3 starts
                                RouteUI.view_tickets_price(RouteDL.getRouteList())

                                # user menu option 3 ends
                            
                            elif (option == "4"):
                                # user menu option 4 starts

                                index = RouteUI.list_of_trains("User", "Buy Ticket", RouteDL.getRouteList())

                                route = RouteDL.GetSingleRouteByIndex(index)
                                ticket = TrainTicketUI.buy_ticket(route)

                                if (ticket != None):
                                    ticket.Booking_no = TrainTicketDL.ListCount() + 1
                                    TrainTicketDL.addIntoList(ticket)

                                # user menu option 4 ends
                            
                            elif (option == "5"):
                                # user menu option 5 starts
                                sortedTicketList = TrainTicketDL.sortTicketList() # calling function for sorting
                                TrainTicketUI.my_tickets(sortedTicketList)

                                # user menu option 5 ends
                            
                            elif (option == "6"):
                                # user menu option 6 starts

                                RouteUI.view_freight_rate(RouteDL.getRouteList())

                                # user menu option 6 ends
                            elif (option == "7"):
                                # user menu option 7 starts

                                index = RouteUI.list_of_trains("User", "Book Cargo", RouteDL.getRouteList())

                                route = RouteDL.GetSingleRouteByIndex(index)
                                cargo = TrainCargoUI.book_cargo(route)

                                if (cargo != None):
                                    cargo.Booking_no = TrainCargoDL.ListCount() + 1
                                    cargo.calculateDate()
                                    TrainCargoDL.addIntoList(cargo)
                    
                                # user menu option 7 ends
                            
                            elif (option == "8"):
                                # user menu option 8 starts
                                sortedCargoList = TrainCargoDL.sortCargoList() # calling function for sortin
                                TrainCargoUI.my_booked_cargo(sortedCargoList)

                                # user menu option 8 ends
                            
                            elif (option == "9"):
                                # user menu option 9 starts

                                RMSUI.view_notice()

                                # user menu option 9 ends
                            
                            elif (option == "10"):
                                # user menu exit point
                                break
                            else:
                                print("Invalid Input !")
                                input("Press any key for continue....")
                                print()
                    
                    # if invalid input
                    else:
                        print("Invalid Input!")
                elif (op == '2'):
                    # sign up
                    user = MUserUI.SignUp()
                    if not(MUserDL.isExist(user)):
                        MUserDL.AddUserIntoList(user)

                        if (user.getRole() == "Customer"):
                            username = user.getUsername()
                            newCustomer = Customer(username)
                            CustomerDL.addIntoList(newCustomer)
                            #CustomerDL.storeData(customerFilePath)

                    MUserDL.storeData(credentialFilePath)
                # _____________________________ Logout statement ___________________________
                elif (op == '3'):
                    RouteDL.storeDataIntoFlie(path1)
                    TrainTicketDL.storeDataIntoFile(path2)
                    TrainCargoDL.storeDataIntoFile(path3)
                    StationDL.storeDataIntoFile(path4)
                    Program.store_data(password)

                    break

            RMSUI.developer()

        # ________________________________ Function Definitions _____________________________________________________________________
        # Railway management system head function

        # login page function
    @staticmethod
    def login_page(password):
            while (True): # loop run until user enter wrong value
                os.system("cls")
                RMSUI.head()

                print(" Login Page >>")
                print("_____________________________________________________________")
                print()
                print(" 1- Admin ")
                print(" 2- User ")
                print(" 3- Exit ")
                login = input("Your Option.....")

                if (login == "1"): # if user press 1
                    # lines for taking password input
                    pwd = input("Enter Password.........(123)..........:")
                    if (password == pwd): # if password is correct
                        return "admin"
                    else: # if password is wrong
                        print("Invalid Password!")
                        input("Press any key for continue....")
                        print()
                elif (login == "2"): # if user press 2 it return user
                    # lines for taking password input
                    pwd = input("Enter Password.........(123)..........:")
                    if (password == pwd): # if password is correct
                        return "user"
                    else: # if password is wrong
                        print("Invalid Password!")
                        input("Press any key for continue....")
                        print()

                elif (login == "3"): # if user press 3 it return logout
                    return "logout"
                else: # for wrong input
                    print("Invalid Input!")

    # function for loading data from file to arrays and variables
    @staticmethod
    def load_data( password):
            path2 = "user_password.txt"
            if(os.path.exists(path2)):
                fileVariable = open(path2, 'r')
                records = fileVariable.read().split("\n")
                fileVariable.close()

                for line in records:
                    password = line

    # function for storing data into file
    @staticmethod
    def store_data( password):
            path2 = "user_password.txt"
            # writing password into file
            file = open(path2, 'w')
            file.write(password)


Program.main()