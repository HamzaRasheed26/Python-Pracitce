from Station import Station

class StationUI:

    @staticmethod
    def takeStationInput():
        stationName = ""
        ath = 0
        atm = 0
        dth = 0
        dtm = 0

        stationName = input("\n Station name :") # station  name

        print(" Note : use 24 hours format for input time ")

        while (True): # validation on correcrt time
            print(" Arrival Time( hh:mm )") # arrival time station 
            ath = int(input("Hour : ")) # hour
            atm = int(input("Minute : ")) # minute

            if (ath >= 1 and ath <= 24 and atm >= 0 and atm <= 59):
                break
            print(" Invalid Time ! ")
        while (True): # validation on correcrt time
            print(" Departure Time( hh:mm )") # arrival time station 
            dth = int(input("Hour : "))  # hour
            dtm = int(input("Minute : ")) # minute

            if (dth >= 1 and dth <= 24 and dtm >= 0 and dtm <= 59):
                break
            print(" Invalid Time ! ")
        return Station(stationName, ath, atm, dth, dtm)
