# We import the files (done before) needed to to the test
import Flight
import Aircraft

# We input the characteristics of a Flight
F1 = Flight.Flight()
F1.departureAirport = "Gatwick"
F1.arrivalAirport = "Brasil"
F1.departureTime = 9.5*60
F1.arrivalTime = 12*60
F1.passengers = 143
F1.d = 50

# We input the characteristics of another Flight
F2 = Flight.Flight()
F2.departureAirport = "Brasil"
F2.arrivalAirport = "Argentina"
F2.departureTime = 13*60
F2.arrivalTime = 15*60
F2.passengers = 187
F2.d = 65

# We input the characteristics of an Aircraft
AC1 = Aircraft.Aircraft()
AC1.callSign = "1234"
AC1.aircraftType = "B777"
AC1.maximumCapacity = 185

# We call the function to prove that it works properly
Flight.show_flight(F1)
Flight.show_flight(F2)

# We call the function to prove that it works properly
Flight.flight_duration(F1)
Flight.flight_duration(F2)

# We call the function to prove that it works properly
Flight.delay_flight(F1, F1.d)
Flight.delay_flight(F2, F2.d)

# We call the function to prove that it works properly
Flight.fits_flight_in_aircraft(F1, AC1)
Flight.fits_flight_in_aircraft(F2, AC1)