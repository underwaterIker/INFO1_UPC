# Definition of the Airport class and its related functions
class Airport:
    def __init__(self):
        self.icaoCode = ""
        self.airportName = ""
        self.location = ""
        self.landingFees = 0
        self.freeParkingHours = 0
        self.additionalParkingCostPerHour = 0


# Definition of the function that, given the airport 'ap' and three text values containing the ICAO code of an airport, 's1', the official name of the airport, 's2', and of geographical coordinates of the airport, 's3', updates the airport information with the provided data
def set_ap_info(ap, s1, s2, s3):
    ap.icaoCode = s1
    ap.airportName = s2
    ap.location = s3

# Definition of the function that, given the airport 'ap' and three numerical values containing the cost of the runway, 'c1', of the number of free hours of parking, 'c2', and of the cost per hour of any additional parking, 'c3',updates the airport information with the provided data
def set_costs(ap, c1, c2, c3):
    ap.landingFees = c1
    ap.freeParkingHours = c2
    ap.additionalParkingCostPerHour = c3

# Definition of the function that, given one Airport 'ap' and a number 't' with the minutes of usage of the airport facilities, calculates the fee to be paid, including the landing fee and the payment of additional parking, if any
def calculate_fee(ap, t):
    if t <= (ap.freeParkingHours * 60):
        n = 0
    else:
        t = t - (ap.freeParkingHours * 60)
        w = t%60
        r = t//60
        if w == 0:
            n = (r * ap.additionalParkingCostPerHour)
        else:
            n = (r * ap.additionalParkingCostPerHour) + ap.additionalParkingCostPerHour
    q = ap.landingFees + n
    #print(q)
    return q

# Definition of the function that, having 'f' the name of a file containing the list of airports names and locations, reads each line of the file creating an airport for each line with the three data of the line
import os.path
def read_airports(f):
    o = os.path.exists(f)
    # print(os.path.exists(f))
    if o == False:
        B = []
        print("Error, the file doesn't exist")
        return B
    else:
        F = open(f, "r")
        l = F.readlines()
        q = len(l) - 1
        V = [0] * q
        k = [0] * q
        F.close()
        T = open(f, "r")
        p = T.readline()
        i = 0
        while i < q:
            AP = Airport()
            p = p.replace("\n", "")
            u = p.split(" ")

            if u[0] == "AIRP":
                i = i - 1
            else:
                AP.icaoCode = str(u[0])
                AP.airportName = str(u[2])
                AP.location = str(u[1])
                if len(u) == 5:
                    set_ap_info(AP, AP.icaoCode, AP.airportName, AP.location)
                    V[i] = AP
                else:
                    print("Error, incorrect format")
            p = T.readline()
            i += 1
        #print(V)
        T.close()
        return V

# Definition of the function that, given a vector of Airports 'v' and a string 's' with the ICAO code of an airport, searches this airport in the vector and returns the position of the airport in the vector
def search_airport_index(v, s):
    found = False
    i = 0
    while i < len(v):
        if str(v[i].icaoCode) == s:
            q = i
            found = True
        i += 1
    if found == False:
        #print("False")
        return -1
    if found == True:
        #print(q)
        return q

# Definition of the function that, given a vector of Airports, and a string 'f' with the name of a text file containing information of the airports costs, reads the content of the file to set the costs of the airports in the vector
def read_airport_costs(v, f):
    o = os.path.exists(f)
    # print(os.path.exists(f))
    if o == False:
        B = []
        print("Error, the file doesn't exist")
        return B
    else:
        F = open(f, "r")
        l = F.readlines()
        F.close()
        T = open(f, "r")
        w = T.readline()
        q = len(l)-1
        i = 0
        while i < q:
            w = w.replace("\n", "")
            u = w.split("   ")
            if u[0] == "AIRP RUNWAY FREE COSTxHH":
                i = i - 1
            else:
                if len(u) == 4:
                    if search_airport_index(v, str(u[0])) != -1:
                        #print(search_airport_index(v, str(u[0])))
                        c1 = int(u[1])
                        c2 = int(u[2])
                        c3 = int(u[3])
                        set_costs(v[search_airport_index(v, str(u[0]))], c1, c2, c3)
                    if search_airport_index(v, str(u[0])) == -1:
                        print("The airport in the cost file has not been found in the vector")
                        AP = Airport()
                        AP.icaoCode = str(u[0])
                        v.append(AP)
                else:
                    print("Error, incorrect format")
            w = T.readline()
            i += 1
    #print(v)
    T.close()
    return v

# Definition of the function that, given a vector of airports 'v', creates a new file 'Airports.kml' with the location of all the airports of the vector
def map_airports (v):
    if len(v) == 0:
        return False
    else:
        F = open("Airports.kml", "w")
        F.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
        F.write("<Document>\n")
        i = 0
        while i < len(v):
            F.write("\t<Placemark>\n")
            F.write("\t\t<name>")
            F.write(v[i].icaoCode)
            F.write("</name>\n")
            F.write("\t\t<description>")
            F.write(v[i].airportName)
            F.write(" Airport")
            F.write("</description>\n")
            F.write("\t\t<Point>\n")
            F.write("\t\t\t<coordinates>")
            F.write(v[i].location)
            F.write("</coordinates>\n")
            F.write("\t\t</Point>\n")
            F.write("\t</Placemark>\n")
            i += 1
        F.write("</Document>\n")
        F.write("</kml>\n")
        return True