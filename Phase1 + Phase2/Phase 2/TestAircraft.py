# We import the files (done before) needed to to the test
import Aircraft

# We input the characteristics of an Aircraft
AC1 = Aircraft.Aircraft()
AC1.callSign = "1234"
AC1.aircraftType = "B777"
AC1.maximumCapacity = 185

# We input the characteristics of another Aircraft
AC2 = Aircraft.Aircraft()
AC2.callSign = "5678"
AC2.aircraftType = "A380"
AC2.maximumCapacity = 200

# We call the function to prove that it works properly
Aircraft.show_aircraft(AC1)
Aircraft.show_aircraft(AC2)