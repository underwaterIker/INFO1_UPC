# Definition of the Airline class and its related functions
class Airline:
    def __init__(self):
        self.companyName = ""
        self.fleet = []
        self.operations = []

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