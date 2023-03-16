#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Program to test project phase 1
import Aircraft
import Flight
import Airline

def createXicaAirline ():
    """ Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    """ 
    # creates first aircraft with some values
    AC1 = Aircraft.Aircraft()
    AC1.callSign = "EC234"
    AC1.aircraftType = "A320"
    AC1.maximumCapacity = 280
    # creates a second aircraft with other values
    AC2 = Aircraft.Aircraft()
    AC2.callSign = "EC504"
    AC2.aircraftType = "A321"
    AC2.maximumCapacity = 310

    # creates first flight with some values
    FL1 = Flight.Flight()
    FL1.departureAirport = "Barcelona"
    FL1.arrivalAirport = "Budapest"
    FL1.departureTime = 8*60
    FL1.arrivalTime = 11*60
    FL1.passengers = 54
    # creates second flight with some values
    FL2 = Flight.Flight()
    FL2.departureAirport = "Barcelona"
    FL2.arrivalAirport = "Istambul"
    FL2.departureTime = 9*60
    FL2.arrivalTime= 12.5*60
    FL2.passengers = 154
    Flight.delay_flight(FL2, 60)
    # creates third flight with some values
    FL3 = Flight.Flight()
    FL3.departureAirport = "Istambul"
    FL3.arrivalAirport = "Budapest"
    FL3.departureTime = 17*60
    FL3.arrivalTime = 19.25*60
    FL3.passengers = 140
    # creates fourth flight with some values
    FL4 = Flight.Flight()
    FL4.departureAirport = "Budapest"
    FL4.arrivalAirport = "Barcelona"
    FL4.departureTime = 20*60
    FL4.arrivalTime = 23*60
    FL4.passengers = 97

    # creates the airline
    Xica = Airline.Airline()
    Xica.companyName = "Xica Airline"
    Airline.add_aircraft(Xica, AC1)
    Airline.add_aircraft(Xica, AC2)
    Airline.add_operation(Xica, FL1)
    Airline.add_operation(Xica, FL2)
    Airline.add_operation(Xica, FL3)
    Airline.add_operation(Xica, FL4)

    return Xica

'''# main
print("Phase1: test program starts.")
A = createXicaAirline()

# We call the function to prove that it works properly
Airline.show_airline(A)

# We call the function to prove that it works properly
Airline.plot_flights(A)

# We call the function to prove that it works properly
Airline.assign_operations(A)

# We call the function to prove that it works properly
Airline.plot_assignments(A)

# We call the function to prove that it works properly
Airline.insert_delay(A, "Barcelona", 8*60, 65)

# We call the function to prove that it works properly
Airline.check_operations(A)

print("Phase1: test program ends.")'''


