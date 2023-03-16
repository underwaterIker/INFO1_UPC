#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:25:43 2020

@author: cristina
"""

#test code of Phase3
import Airline, Airport

#uploading the data from files
primera = Airline.read_airline("PrimeraAir.txt")
costs = Airport.read_airports("AP.txt")

Airport.read_airport_costs(costs, "APC.txt")    # We have to call this function in order to set the costs of each Airport facilities

#do calculations
primera = Airline.assign_operations(primera)
to_pay = Airline.calculate_day_costs(primera, costs)

#results in screen and in file
print("Total cost for the day operations is "+str(to_pay)+" Euros\n")
if Airline.write_day_plan(primera, "May7.txt"):
    print("See detailed planning in file 'May7th.txt'")