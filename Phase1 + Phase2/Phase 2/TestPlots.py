import Flight
import Airline
import TestFlight as TF

# We input the characteristics of a Flight
F1 = Flight.Flight()
F1.departureAirport = "El Prat"
F1.arrivalAirport = "Gatwick"
F1.departureTime = 5.5*60
F1.arrivalTime = 9*60
F1.passengers = 189

# We input the characteristics of an Airline
A1 = Airline.Airline()
A1.operations = [TF.F1, TF.F2]

# We call the function to prove that it works properly
Flight.plot_flight(F1)

# We call the function to prove that it works properly
Flight.plot_flights(A1.operations)