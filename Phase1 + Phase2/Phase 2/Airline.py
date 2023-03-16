import Assignment
import Flight

# Definition of the Airline class and its related functions
class Airline:
    def __init__(self):
        self.companyName = ""
        self.fleet = []
        self.operations = []
        self.assignments = []

# Definition of the function that prints in the screen the data of the Airline
def show_airline(t):
    print("Airline information:")
    print("     Company name:", t.companyName)
    print("     It has a fleet of", len(t.fleet), "Aircraft:")

    i = 0
    while i < len(t.fleet):
        print("         ", t.fleet[i].callSign, "(",t.fleet[i].aircraftType, "with", t.fleet[i].maximumCapacity, "seats.)")
        i += 1
    print("     Operations today are", len(t.operations),":")
    e = 0
    while e < len(t.operations):
        h1 = str(int(t.operations[e].departureTime // 60))
        h1 = h1.zfill(2)
        m1 = str(int(t.operations[e].departureTime % 60))
        m1 = m1.zfill(2)
        h2 = str(int(t.operations[e].arrivalTime // 60))
        h2 = h2.zfill(2)
        m2 = str(int(t.operations[e].arrivalTime % 60))
        m2 = m2.zfill(2)
        print("         ", h1,":",m1, t.operations[e].departureAirport, "to", h2,":",m2, t.operations[e].arrivalAirport, "with", t.operations[e].passengers, "passengers.")
        e += 1
    e = 0
    print("     Assignments are:")
    while e < len(t.assignments):
        r = e + 1
        print("         Assignment", r,":")
        print("             Aircraft call sign:", t.assignments[e].Aircraft.callSign)
        print("             Aircraft type:", t.assignments[e].Aircraft.aircraftType)
        print("             Flights assigned to the Aircraft:")
        y = 0
        while y < len(t.assignments[e].flightsAssignedToAircraft):
            f = y + 1
            print("                 Flight", f,":")
            print("                     Departure airport:", t.assignments[e].flightsAssignedToAircraft[y].departureAirport)
            print("                     Arrival airport:", t.assignments[e].flightsAssignedToAircraft[y].arrivalAirport)
            print("                     Departure time:", t.assignments[e].flightsAssignedToAircraft[y].departureTime)
            print("                     Arrival time:", t.assignments[e].flightsAssignedToAircraft[y].arrivalTime)
            print("                     Passengers:", t.assignments[e].flightsAssignedToAircraft[y].passengers)
            y += 1
        e += 1

# Definition of the function that adds the aircraft to the fleet of the Airline only if it's not there yet
# Also, we make the function return a boolean depending if the aircraft can be added to the fleet of the Airplane or not
def add_aircraft(y, ac):
    norepeat = True
    i = 0
    # We search if the aircraft is already in the fleet of the Airline, if we find it, we set the boolean to False
    while i < len(y.fleet) and norepeat:
        if y.fleet[i].callSign == ac.callSign:
            norepeat = False
        i += 1
    # In case of not finding the aircraft in the fleet, we add the aircraft to the fleet. And set the boolean to True
    if norepeat is True:
        y.fleet.append(ac)
    return (bool(norepeat))

# Definition of the function that adds the flight to the operations of the Airlane if it's not there yet
# Also, we make the function return a boolean depending if the flight can be added to the operations of the Airplane or not
def add_operation(u, f):
    norepeat = True
    i = 0
# We search if the flight is already in the operations of the Airline, if we find it, we set the boolean to False
    while i < len(u.operations) and norepeat:
        if u.operations[i].departureAirport == f.departureAirport:
            if u.operations[i].arrivalAirport == f.arrivalAirport:
                if u.operations[i].departureTime == f.departureTime:
                    norepeat = False
        i += 1
# In case of not finding the flight in the opertions, we add the flight to the operations. And set the boolean to True
    if norepeat is True:
        u.operations.append(f)
    return (bool(norepeat))

# We import matplotlib in order to do the plots
import matplotlib.pyplot as plt

# Definition of the function that, given an airline with a list of flight operations, plots all its flights in separate bars
# Tested in TestAirline.py
def plot_flights(a):
# We call the former function in module Flight.py
    Flight.plot_flights(a.operations)

# Definition of the function that given an airline with a list of flight operations and a fleet of aircraft, allocates the flights to the fleet
def assign_operations(a):
    A = [Assignment.Assignment()]*len(a.fleet)
    V = []
    p = 0
    while p < len(a.fleet):
        A[p]=Assignment.Assignment()
        A[p].Aircraft = None
        Assignment.assign_aircraft(A[p], a.fleet[p])
        V.append(A[p])
        #print(V[p].Aircraft.callSign)
        p += 1
    #print(V[0].Aircraft.callSign)
    #print(V[1].Aircraft.callSign)

    #i = 0
    w = 0
    #print(V)
    #print("--------------------------")
    while w < len(a.operations):
        i = 0
        while i < len(V):
            #print(i)
            #print(w)
            B = Assignment.assign_flight(V[i], a.operations[w])
            #print(bool(B))
            #print(V[i])
            if bool((B)) == False:
                i = i + 1
            if bool((B)) == True:
                #a.assignments.append(V[i])
                #print(a.operations)
                i = len(V)
                #print(a.operations)
        if bool(B) == False:
            print("The following flight CAN'T be added to an assignment:")
            Flight.show_flight(a.operations[w])
        w += 1
    #print("-----------------")
    #print(a.assignments)
    #print(V[0].flightsAssignedToAircraft)
    #print(V[1].flightsAssignedToAircraft)
    k = 0
    while k < len(V):
        #print(V[k].flightsAssignedToAircraft)
        a.assignments.append(V[k])
        k += 1

# Definition of the function that, given an airline a with a list of assignments, plots all its flights grouped by aircraft
def plot_assignments(a):
    Assignment.plot_assignments(a.assignments)

# Definition of the function that, given an airline a, the information to identify a flight (the airport of departure depAp and the time of departure depTm), and the number of minutes d that this flight has been delayed, updates the information of the given flight
def insert_delay(a, depAp, depTm, d):
    found = False
    i = 0
    while i < len(a.operations):
        if a.operations[i].departureAirport == depAp and a.operations[i].departureTime == depTm:
            found = True
            p = i
        i += 1
    if found == True:
        Flight.delay_flight(a.operations[p], d)
        return True
    if found == False:
        return False

# Definition of the function that, given an airline, checks the compatibility of the current allocation of the flights
def check_operations(a):
    compatible = True
    i = 0
    p = 0
    while i < len(a.assignments):
        compatible = True
        o = 0
        while o < len(a.assignments[i].flightsAssignedToAircraft):
            if (o + 1) >= len(a.assignments[i].flightsAssignedToAircraft):
                compatible = True
                o = len(a.assignments[i].flightsAssignedToAircraft)
            if (o + 1) < len(a.assignments[i].flightsAssignedToAircraft):
                if a.assignments[i].flightsAssignedToAircraft[o].arrivalAirport != a.assignments[i].flightsAssignedToAircraft[o+1].departureAirport:
                    compatible = False
                q = a.assignments[i].flightsAssignedToAircraft[o+1].departureTime - a.assignments[i].flightsAssignedToAircraft[o].arrivalTime
                if q < 60:
                    compatible = False
                if a.assignments[i].flightsAssignedToAircraft[o].passengers > a.assignments[i].Aircraft.maximumCapacity:
                    compatible = False
            if compatible == False:
                p = p + 1
                print("The flight:")
                Flight.show_flight(a.assignments[i].flightsAssignedToAircraft[o+1])
                print("is not compatible with the previous flight:")
                Flight.show_flight(a.assignments[i].flightsAssignedToAircraft[o])
            o += 1
        i += 1
    if p == 0:
        return True
    if p != 0:
        return False
