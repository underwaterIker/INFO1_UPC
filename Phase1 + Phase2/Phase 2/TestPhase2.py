#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:01:54 2020

@author: cristina
"""

import Aircraft, Flight, Airline, Assignment
from TestAirline import createXicaAirline

X = createXicaAirline()
Airline.assign_operations(X)
#X = Airline.assign_operations(createXicaAirline())
Airline.plot_assignments(X)

Airline.insert_delay(X, "Barcelona", 8*60, 60)
if Airline.check_operations(X):
    print("No problem with the delay")
else:
    print("Reasigning flights again")
    X = Airline.assign_operations(X)

Airline.show_airline(X)