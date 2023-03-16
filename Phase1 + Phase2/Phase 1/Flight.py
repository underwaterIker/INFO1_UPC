# Definition of the Flight class and its related functions
class Flight:
    def __init__(self):
        self.departureAirport = ""
        self.arrivalAirport = ""
        self.departureTime = 0
        self.arrivalTime = 0
        self.passengers = 0

# Definition of the function that prints in the screen the data of the flight
def show_flight(t):
# Operations to show the departure and arrival times in format HH:MM
    h1 = int(t.departureTime//60)
    m1 = int(t.departureTime % 60)
    h2 = int(t.arrivalTime // 60)
    m2 = int(t.arrivalTime % 60)
    if h1 < 10:
        b = 0
        h1 = str(b) + str(h1)
    if h2 < 10:
        b = 0
        h2 = str(b) + str(h2)
    if m1 < 10:
        b = 0
        m1 = str(b) + str(m1)
    if m2 < 10:
        b = 0
        m2 = str(b) + str(m2)
# Now that we have the departure and arrival times in format HH:MM, we print in the screen the data of the flight
    if [type(t.departureAirport) is str and type(t.arrivalAirport) is str and type(t.departureTime) is int and type(t.arrivalTime) is int and type(t.passengers) is int] or [type(t.departureAirport) is str and type(t.arrivalAirport) is str and type(t.departureTime) is float and type(t.arrivalTime) is float and type(t.passengers) is int]:
        print("Departure Airport =", t.departureAirport, "| Arrival Airport =", t.arrivalAirport, "| Departure Time =", h1,":",m1, "| Arrival Time =", h2,":",m2, "| Passengers =", t.passengers)
# Check for errors
    else:
        print("Error, check that data has been input correctly")

# Definition of the function that calculates the duration of the flight in minutes and prints it on the screen
def flight_duration(y):
    m = int(y.arrivalTime) - int(y.departureTime)
    if m > 0:
        print("The duration of the flight is:", m, "minutes")
# Check for errors
    else:
        print("Error, check that data has been input correctly")

# Definition of the function that takes into account the delay time, and reestablishes the departure and arrival times depending on the delay time
# Also, we make the function return a boolean depending if the delay time can be added correctly or not
def delay_flight(u, d):
    delay = True
# We sum the delay time to the departure and arrival times
    q = u.departureTime + d
    w = u.arrivalTime + d
# We set that if none of these sums overpass the total minuts of one day, the function returns the boolean True
    if q < 1440 and w < 1440:
        u.departureTime = q
        u.arrivalTime = w
        delay = True
# If one of the sums overpassses the total minuts of a day, we make the function return the boolean False
    else:
        delay = False
    return (bool(delay))

# Definition of the function that determines if the number of seats of the aircraft can allocate the total passengers of the flight
# Also, we make the function return a boolean depending if the number of seats of the aircraft can allocate the total passengers of the flight or not
def fits_flight_in_aircraft(s, a):
    allocate = True
# If the number of passengers is lower or equal than the number of seats, the function will return the boolean True
    if s.passengers <= a.maximumCapacity:
        allocate = True
# If the number of passengers is higher than the number of seats, the function will return the boolean False
    else:
        allocate = False
    return (bool(allocate))