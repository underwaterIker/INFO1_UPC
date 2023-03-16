# Definition of the Aircraft class and its related functions
class Aircraft:
    def __init__(self):
        self.callSign = ""
        self.aircraftType = ""
        self.maximumCapacity = 0

# Definition of the function that prints in the screen the data of the aircraft
def show_aircraft(t):
    if type(t.maximumCapacity) is int and type(t.aircraftType) is str and type(t.callSign) is str:
        print("Callsign =", t.callSign, "| Aircraft Type =", t.aircraftType, "| Maximum Capacity =", t.maximumCapacity)
# Check for errors
    else:
        print("Error, check that data has been input correctly")