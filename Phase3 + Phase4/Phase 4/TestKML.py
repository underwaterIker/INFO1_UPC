import Airport
import Flight
import Assignment
import Aircraft
import Airline

f = "AP.txt"
g = "FL.txt"
h = "AC.txt"

va = Airport.read_airports(f)
vf = Flight.read_flights(g)
vac = Aircraft.read_aircrafts(h)

A = Airline.Airline()
A.fleet = vac
A.operations = vf
Airline.assign_operations(A)

#print(A.assignments[1].flightsAssignedToAircraft[3].departureAirport) #This Assignment has 4 flights assigned to the Aircraft
Airport.map_airports(va)
Flight.map_flights(vf, va)
Assignment.map_assignment(A.assignments[1], va)