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

import os.path
# Definition of the function that, having 'f' the name of a file containing the list of aircraft of a company, reads each line of the file creating an aircraft with the data found
def read_aircrafts(f):

    o = os.path.exists(f)
    #print(os.path.exists(f))
    if o == False:
        V = []
        print("Error, the file doesn't exist")
        return V
    else:
        '''F = open(f, "r")
        l = F.readlines()
        q = len(l) - 1
        V = [0]*q
        F.close()'''
        T = open(f, "r")
        lineas = T.readlines()
        i = 1
        '''g = T.readline()
        g = T.readline()'''
        V = []
        while i < len(lineas):
            g = lineas[i]
            AC = Aircraft()
            g = g.replace("\n", "")
            e = g.split(" ")
            AC.callSign = e[0]
            AC.aircraftType = e[1]
            AC.maximumCapacity = int(e[2])
            '''if e[0] == "CALLSIGN":
                i = i - 1'''

            if len(e) == 3:
                    V.append(AC)
            else:
                    print("Error, the Aircraft in the position", g, "has an incorrect format")
            i += 1
        #print (V)
        T.close()
        return V
