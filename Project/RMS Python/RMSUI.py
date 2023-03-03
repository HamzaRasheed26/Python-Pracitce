import os

class RMSUI:
    
    @staticmethod
    def head():
        print("*************************************************************")
        print("*                  RAILWAY MANAGEMENT SYSTEM                *")
        print("*************************************************************")
        print()

    # Admin menu page function
    @staticmethod
    def Admin_Menu():
        print(" Admin >> Menu")
        print("_____________________________________________________________")
        print()
        print("Select one of the following options........")
        print()
        print(" 1. View of all route of trains")
        print(" 2. Add new route of train")
        print(" 3. Edit Route ")
        print(" 4. Set tickets prices")
        print(" 5. Set Freight rates")
        print(" 6. View schedule of stations")
        print(" 7. Add important notices")
        print(" 8. View employers data")
        print(" 9. EXit")
        print()
        option = input("Select any option........:")
        return option

    # this function is hardcode its only print data of employers
    # we cannot edit this data
    @staticmethod
    def view_employers_data():
        RMSUI.head()
        print(" Admin >> View Employers Data ")
        print("_____________________________________________________________")
        print("      Train Drivers  ")
        print(" 1. Ahmed       2. Sajid   ")
        print(" 3. Ali         4. Akhtar  ")
        print(" 5. Hamid       6. Asif    ")
        print("      Train Police")
        print(" 1. Inspector Hassan")
        print(" 2. Sub Inspector Faheem")
        print(" 3. Sub Inspector Qasim")
        print(" 4. Sub Inspector Umar")
        print(" 5. Sub Inspector Taha")
        print()
        print("     Station Incharge")
        print(" 1. Babar")
        print(" 2. Rizwan")
        print(" 3. Fakhar")
        print(" 4. Asim")
        print(" 5. Zia")
        print(" 6. Zohaib")
        print(" 7. Talha")
        print()
        input("Press any key for continue....")
        print()

    # function for showing user menu on screen
    @staticmethod
    def user_menu():
        print(" User >> Menu")
        print("_____________________________________________________________")
        print("Select one of the following options........")
        print()
        print(" 1. View of all route of trains")
        print(" 2. View Stations Schedule")
        print(" 3. View tickets prices")
        print(" 4. Buy Tickets")
        print(" 5. View My Tickets")
        print(" 6. View Freight Rates")
        print(" 7. Book Cargo")
        print(" 8. View My Booked Cargo")
        print(" 9. View Notices")
        print(" 10. EXit")
        print()
        option = input("Select any option........:")
        return option

    # functoin for developer name
    @staticmethod
    def developer():
        os.system("cls")
        print("\n\n")
        print("************** THANKS FOR USING RAILWAY MANAGEMENT SYSTEM ***************")
        print("*                                                                       *")
        print("*            Developer : *** Hamza Rasheed 2021-CS-26  ***              *")
        print("*                                                                       *")
        print("*************************************************************************")
        print()

    notice = "No_notice"

    # Function for posting notices for user
    @staticmethod
    def add_notice():
        RMSUI.head()

        print(" Admin >> Add Notice ")
        print("_____________________________________________________________")
        print("Write your notice here.....:")
        print()

        notice = input() # string varaible for taking  notice as input

        print()
        input("Press any key for continue....")
        print()

    # function for viewing notic
    @staticmethod
    def view_notice():
        RMSUI.head()
        print(" User >> View Notice ")
        print("_____________________________________________________________")
        print()
        print("Notice Board......")
        print()
        print(RMSUI.notice) # string notice variable

        print()
        input("Press any key for continue....")
        print()