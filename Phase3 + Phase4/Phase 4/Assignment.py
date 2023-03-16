# We import the file needed
import Aircraft
import Flight

# Definition of the Assignment class and its related functions
class Assignment:
    def __init__(self):
        self.Aircraft = None
        self.flightsAssignedToAircraft = []

# Definition of the function that adds aircraft to assignment
def assign_aircraft(assig, ac):
    if assig.Aircraft != None or len(assig.flightsAssignedToAircraft) != 0:
        return False
    else:
        assig.Aircraft = ac
        return True

# Definition of the function that adds flights to the list of flights assigned to the aircraft
def assign_flight(assig, f):
    if assig.Aircraft == None:
        return False
    a = Flight.convert_time(f.departureTime)
    compatible = False
    if len(assig.flightsAssignedToAircraft) == 0:
        if int(f.passengers) <= int(assig.Aircraft.maximumCapacity):
            compatible = True
        else:
            compatible = False
    if len(assig.flightsAssignedToAircraft) != 0:
        b = Flight.convert_time(str(assig.flightsAssignedToAircraft[len(assig.flightsAssignedToAircraft) - 1].arrivalTime))
        if assig.flightsAssignedToAircraft[len(assig.flightsAssignedToAircraft)-1].arrivalAirport == f.departureAirport:
            q = int(a) - int(b)
            if q >= 60:
                if int(f.passengers) <= int(assig.Aircraft.maximumCapacity):
                    compatible = True
        else:
            compatible = False

    if compatible is True:
        assig.flightsAssignedToAircraft.append(f)
        return True
    if compatible is False:
        return False

# Definition of the function that prints in the screen the data of the Assignment, including all the flights and the aircraft
def show_assignment(assig):
    print("The aircraft characteristics are:")
    print("     Aircraft call sign:", assig.Aircraft.callSign)
    print("     Aircraft type:", assig.Aircraft.aircraftType)
    print("     Aircraft maximum capacity:", assig.Aircraft.maximumCapacity)
    print("The flights assigned to the Aircraft are:")
    i = 0
    while i < len(assig.flightsAssignedToAircraft):
        print("     Flight", (i+1),":")
        print("         Departure Airport:", assig.flightsAssignedToAircraft[i].departureAirport)
        print("         Arrival Airport:", assig.flightsAssignedToAircraft[i].arrivalAirport)
        h1 = int(int(assig.flightsAssignedToAircraft[i].departureTime) // 100)
        m1 = int(int(assig.flightsAssignedToAircraft[i].departureTime) % 100)
        h2 = int(int(assig.flightsAssignedToAircraft[i].arrivalTime) // 100)
        m2 = int(int(assig.flightsAssignedToAircraft[i].arrivalTime) % 100)
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
        print("         Departure Time:", h1,":",m1)
        print("         Arrival Time:", h2,":",m2)
        print("         Passengers:", assig.flightsAssignedToAircraft[i].passengers)
        i += 1

# We import matplotlib in order to do the plots
import matplotlib.pyplot as plt

# Definition of the function that plots the duration of the flights assigned in Assignment
def plot_assignment(assig):
    plt.barh([1], [24], color="white", edgecolor="black")
    i = 0
    while i < len(assig.flightsAssignedToAircraft):
        h1 = [0] * len(assig.flightsAssignedToAircraft)
        h2 = [0] * len(assig.flightsAssignedToAircraft)
        h11 = [0] * len(assig.flightsAssignedToAircraft)
        h22 = [0] * len(assig.flightsAssignedToAircraft)
        h111 = [0] * len(assig.flightsAssignedToAircraft)
        h222 = [0] * len(assig.flightsAssignedToAircraft)
        u = i+1
        d = len(assig.flightsAssignedToAircraft)-u
        h1[d] = assig.flightsAssignedToAircraft[d].departureTime // 100
        h2[d] = assig.flightsAssignedToAircraft[d].arrivalTime // 100
        h11[d] = (assig.flightsAssignedToAircraft[d].departureTime % 100) / 60
        h22[d] = (assig.flightsAssignedToAircraft[d].arrivalTime % 100) / 60
        h111[d] = h1[d] + h11[d]
        h222[d] = h2[d] + h22[d]
        plt.title("Duration of the flights assigned to Assignment")
        plt.xlabel("Hours")
        plt.grid(color='grey', linestyle='dashed', linewidth=0.6)
        plt.yticks([1], [assig.Aircraft.callSign + "("+assig.Aircraft.aircraftType+")"])
        plt.barh([1], [h222[d]], color="cornflowerblue", edgecolor="black")
        plt.barh([1], [h111[d]], color="white", edgecolor="black")
        i += 1
    plt.show()

# Definition of the function that plots the duration of the flights assigned in Assignment, of all the Assignments inside the vector that contains all the Assignments
def plot_assignments(vector_assig):
    H = [""] * 24
    W = [0] * 24
    m = 0
    while m < len(H):
        j = m+4
        j = str(j)
        j = j.zfill(2)
        H[m] = str(j+":00")
        W[m] = m+4
        m += 4
    n = 0
    while n < len(vector_assig):
        plt.barh([n], [24], color="white", edgecolor="black")
        n += 1
    i = 0
    while i < len(vector_assig):
        V = [0] * len(vector_assig)
        B = [0] * len(vector_assig)
        t = 0
        while t < len(vector_assig):
            V[t] = t
            t = t + 1
        l = 0
        while l < len(vector_assig):
            B[l] = (vector_assig[l].Aircraft.callSign + "("+vector_assig[l].Aircraft.aircraftType+")")
            l += 1
        h1 = [0] * len(vector_assig)
        h2 = [0] * len(vector_assig)
        h11 = [0] * len(vector_assig)
        h22 = [0] * len(vector_assig)
        h111 = [0] * len(vector_assig)
        h222 = [0] * len(vector_assig)
        u = i + 1
        d = len(vector_assig)-u
        o = 0
        while o < len(vector_assig[i].flightsAssignedToAircraft):
            c = o + 1
            k = len(vector_assig[i].flightsAssignedToAircraft)-c
            h1[d] = int(vector_assig[i].flightsAssignedToAircraft[k].departureTime) // 100
            h2[d] = int(vector_assig[i].flightsAssignedToAircraft[k].arrivalTime) // 100
            h11[d] = (int(vector_assig[i].flightsAssignedToAircraft[k].departureTime) % 100) / 60
            h22[d] = (int(vector_assig[i].flightsAssignedToAircraft[k].arrivalTime) % 100) / 60
            h111[d] = h1[d] + h11[d]
            h222[d] = h2[d] + h22[d]
            plt.title("Duration of the flights assigned to each Assignment")
            plt.yticks(V, B)
            plt.xticks(W, H)
            plt.xlabel("Hours")
            plt.grid(color='grey', linestyle='dashed', linewidth=0.6)
            plt.barh([i], [h222[d]], color="cornflowerblue", edgecolor="black")
            plt.barh([i], [h111[d]], color="white", edgecolor="black")
            o += 1
        i += 1
    plt.show()

import Airport
# Definition of the function that, given an Assignment with the information of the flights to be done by one aircraft in one day, creates a new file 'name.kml', wher 'name' is the Callsign of the Aircraft in the Assignment
def map_assignment(assig, va):
    if len(assig.flightsAssignedToAircraft) == 0:
        return False
    else:
        name = str(assig.Aircraft.callSign)+".kml"
        F = open(name, "w")
        F.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        F.write("<Document>\n")
        i = 0
        while i < len(assig.flightsAssignedToAircraft):
            a = Airport.search_airport_index(va, str(assig.flightsAssignedToAircraft[i].departureAirport))
            b = Airport.search_airport_index(va, str(assig.flightsAssignedToAircraft[i].arrivalAirport))
            if a == -1 or b == -1:
                print("One of the 2 Airports of the flight couldn't be found")
                i += 1
            else:
                F.write("\t<Placemark>\n")
                F.write("\t\t<name>")
                F.write(assig.flightsAssignedToAircraft[i].departureAirport)
                F.write(" to ")
                F.write(assig.flightsAssignedToAircraft[i].arrivalAirport)
                F.write("</name>\n")
                F.write("\t\t<LineString>\n")
                F.write("\t\t\t<extrude>1</extrude>\n")
                F.write("\t\t\t<tessellate>1</tessellate>\n")
                F.write("\t\t\t\t<coordinates>\n")
                F.write("\t\t\t\t\t")
                F.write(va[a].location)
                F.write("\n")
                F.write("\t\t\t\t\t")
                F.write(va[b].location)
                F.write("\n")
                F.write("\t\t\t\t</coordinates>\n")
                F.write("\t\t</LineString>\n")
                F.write("\t</Placemark>\n")
                i += 1
        F.write("</Document>\n")
        F.write("</kml>\n")
        return True