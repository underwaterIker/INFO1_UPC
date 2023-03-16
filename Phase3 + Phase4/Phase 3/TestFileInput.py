import Aircraft
import Flight
import Airline

# We input the characteristics we need in order to be able to call the functions lately
f = "AC.txt"

hhmm = "0930"

t = "FL.txt"

n = "PrimeraAir.txt"

c = "DayPlan.txt"

# We call the functions to prove they work properly
V = Aircraft.read_aircrafts(f)
for x in V:
    Aircraft.show_aircraft(x)

Flight.convert_time(hhmm)
Flight.read_flights(t)
A = Airline.read_airline(n)
Airline.write_day_plan(A, c)