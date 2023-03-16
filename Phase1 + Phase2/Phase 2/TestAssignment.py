import Flight
import Assignment
import Aircraft
import Airline

# We input the characteristics of the Aircraft
AC1 = Aircraft.Aircraft()
AC1.callSign = "AC1"
AC1.aircraftType = "B777"
AC1.maximumCapacity = 185

# We input the characteristics of another Aircraft
AC2 = Aircraft.Aircraft()
AC2.callSign = "AC2"
AC2.aircraftType = "A380"
AC2.maximumCapacity = 200

# We input the characteristics of a Flight
F1 = Flight.Flight()
F1.departureAirport = "Gatwick"
F1.arrivalAirport = "El Prat"
F1.departureTime = 17*60
F1.arrivalTime = 19*60
F1.passengers = 143
F1.d = 50

# We input the characteristics of another Flight
F2 = Flight.Flight()
F2.departureAirport = "Brasil"
F2.arrivalAirport = "Gatwick"
F2.departureTime = 13*60
F2.arrivalTime = 15*60
F2.passengers = 187
F2.d = 65

# We input the characteristics of another Flight
F3 = Flight.Flight()
F3.departureAirport = "Istambul"
F3.arrivalAirport = "Budapest"
F3.departureTime = 17*60
F3.arrivalTime = 18.5*60
F3.passengers = 140
F3.d = 10

# We input the characteristics of another Flight
F4 = Flight.Flight()
F4.departureAirport = "Budapest"
F4.arrivalAirport = "Barcelona"
F4.departureTime = 20*60
F4.arrivalTime = 23*60
F4.passengers = 97
F4.d = 15

# We call the function to prove that it works properly
Flight.delay_flight(F1, F1.d)
Flight.delay_flight(F2, F2.d)
Flight.delay_flight(F3, F3.d)
Flight.delay_flight(F4, F4.d)

# We input the characteristics of the Assignment
As = Assignment.Assignment()
As.Aircraft = AC2
As.flightsAssignedToAircraft = [F2]

# We input the characteristics of another Assignment
As2 = Assignment.Assignment()
As2.Aircraft = AC1
As2.flightsAssignedToAircraft = [F3, F4]

# We input the characteristics of the vector of Assignments
Ai = Airline.Airline()
Ai.assignments = [As, As2]

# We call the function to prove that it works properly
Assignment.assign_aircraft(As, AC1)

# We call the function to prove that it works properly
Assignment.assign_flight(As, F1)

# We call the function to prove that it works properly
Assignment.show_assignment(As)

# We call the function to prove that it works properly
Assignment.plot_assignment(As)

# We call the function to prove that it works properly
Assignment.plot_assignments(Ai.assignments)