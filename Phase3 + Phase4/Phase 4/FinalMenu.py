import Aircraft
import Flight
import Airline
import Assignment
import Airport

def show_menu():
    print("\nUsers menu OPTIONS:\n")
    print("\t--initialize--")
    print("(i) read all data from the input files into the necessary main variables\n")
    print("\t--modification options--")
    print("(a) assign flights to the airline aircraft")
    print("(c) calculate current operational cost related to airports services")
    print("(d) enter a delay and check assignments\n")
    print("\t--output options--")
    print("(s) show airline information in the screen and the cost of the day operations")
    print("(k) write KML files of airports, flights and assignments")
    print("(p) plot the flights and the assignments of the airline")
    print("(w) write current airline assignment into a file\n")
    print("\t--end option--")
    print("(e) end program\n")

show_menu()

x = ""
while x != "i":
    x = input("Please, select an option entering one of the letters:")
    if x != "i":
        print("The variables are still empty")
    else:
        m = input("Enter the name of the file containing the list of Aircrafts:")
        n = input("Enter the name of the file containing the information of an Airline:")
        b = input("Enter the name of the file containing the list of Airports:")
        v = input("Enter the name of the file containing the list of Flights:")
        M = Aircraft.read_aircrafts(m)
        N = Airline.read_airline(n)
        B = Airport.read_airports(b)
        V = Flight.read_flights(v)


x = ""
while x != "e":
    show_menu()
    x = input("Please, select an option entering one of the letters:")
    if x != "a" and x != "c" and x != "d" and x != "s" and x != "k" and x != "p" and x != "w" and x != "e":
        print("Option not valid")
    else:
        if x == "a":
            Airline.assign_operations(N)
        if x == "c":
            Airline.calculate_day_costs(N, B)
        if x == "d":
            depAp = input("Enter the departure Airport of the flight:")
            depTm = input("Enter the departure Time of the flight:")
            min = input("Enter the number of minuts the flight has been delayed:")
            Airline.insert_delay(N, depAp, depTm, min)
            Airline.check_operations(N)
        if x == "s":
            Airline.show_airline(N)
            Airline.calculate_day_costs(N, B)
        if x == "k":
            Airport.map_airports(B)
            Flight.map_flights(V, B)
            assig = int(input("Enter the position of the Assigment inside the vector of Assignments:"))
            Assignment.map_assignment(N.assignments[assig], B)
        if x == "p":
            Flight.plot_flights(N.operations)
            Assignment.plot_assignments(N.assignments)
        if x == "w":
            filename = input("Enter the name of the file:")
            Airline.write_day_plan(N, filename)
        if x == "e":
            x = "e"