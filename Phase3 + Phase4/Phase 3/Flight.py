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
    h1 = int(float(t.departureTime)//100)
    m1 = int(float(t.departureTime) % 100)
    h2 = int(float(t.arrivalTime) // 100)
    m2 = int(float(t.arrivalTime) % 100)
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
    # If one of the sums overpasses the total minuts of a day, we make the function return the boolean False
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

# We import matplotlib in order to do the plots
import matplotlib.pyplot as plt

# Definition of the function that shows a horizontal bar that shows the flight duration
def plot_flight(f):
    h1 = f.departureTime // 60
    h2 = f.arrivalTime // 60
    h11 = (f.departureTime % 60)/60
    h22 = (f.arrivalTime % 60)/60
    h111 = h1 + h11
    h222 = h2 + h22
    plt.title("Flight Duration")
    plt.xlabel("Hours")
    plt.grid(color='grey', linestyle='dashed', linewidth=0.6)
    plt.yticks([1], [f.departureAirport + "\n" + f.arrivalAirport])
    plt.barh([1], [24], color="white", edgecolor="black")
    plt.barh([1], [h222], color="palegreen", edgecolor="black")
    plt.barh([1], [h111], color="white", edgecolor="black")
    plt.show()

# Definition of the function that shows a horizontal bar that shows the flight duration of a vector of flights
def plot_flights(vf):
    i = 0
    while i < len(vf):
        V = [0] * len(vf)
        B = [0] * len(vf)
        t = 0
        while t < len(vf):
            V[t] = t
            t = t + 1
        l=0
        while l < len(vf):
            B[l]= str(vf[l].departureAirport + "\n" + vf[l].arrivalAirport)
            l += 1
        h1 = vf[i].departureTime // 60
        h2 = vf[i].arrivalTime // 60
        h11 = (vf[i].departureTime % 60) / 60
        h22 = (vf[i].arrivalTime % 60) / 60
        h111 = h1 + h11
        h222 = h2 + h22
        plt.title("Flight Duration")
        plt.yticks(V, B)
        plt.xlabel("Hours")
        plt.grid(color='grey', linestyle='dashed', linewidth=0.6)
        plt.barh([i], [24], color="white", edgecolor="black")
        plt.barh([i], [h222], color="palegreen", edgecolor="black")
        plt.barh([i], [h111], color="white", edgecolor="black")
        i += 1
    plt.show()

# Definition of the function that, given a string with a time in the format HHMM (HH is the hour and MM is the minute), converts it to minutes and returns a value between 0 and 1440 (24*60)
def convert_time(hhmm):
    if type(hhmm) != str:
        print("Error, the format is not correct")
        return -1
    else:
        q = int(hhmm) // 100
        qq = q*60
        w = int(hhmm) % 100
        e = qq + w
        if q > 23 or w > 60 or e > 1440:
            print("Error, the format is not correct")
            return -1
        else:
            #print(e)
            return e

import os.path
# Definition of the function that, having 'f' the name of a file containing the list of flights to be managed by an airline company in one day, sorted by departure time, reads each line of the file creating a flight with the data found
def read_flights(f):
    o = os.path.exists(f)
    #print(os.path.exists(f))
    if o == False:
        B = []
        print("Error, the file doesn't exist")
        return B
    else:
        F = open(f, "r")
        l = F.readlines()
        q = len(l) - 1
        V = [0]*q
        k = [0]*q
        F.close()
        T = open(f, "r")
        p = T.readline()
        i = 0
        while i < q:
            FL = Flight()
            p = p.replace("\n", "")
            u = p.split(" ")

            if u[0] == "TIMD":
                i = i - 1
            else:
                FL.departureAirport = str(u[2])
                FL.arrivalAirport = str(u[3])
                FL.departureTime = str(u[0])
                FL.arrivalTime = str(u[1])
                FL.passengers = int(u[4])
                if len(u) == 5:
                    k[i] = int(u[0])
                    if k[i - 1] > k[i]:
                        print("Error. The flight in the position", i+1, " has a departure time that is earlier than the previous flight")
                    else:
                        V[i] = FL
                else:
                    print("Error, incorrect format")
            p = T.readline()
            i += 1
        #print(V)
        T.close()
        return V