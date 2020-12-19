# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 08:46:49 2020

ADVENT OF CODE 2020 DAY 13

@author: murph
"""
import pandas as pd
import numpy as np

data = open('c:/Users/murph/Documents/projects/advent of code/input13.txt')
raw = data.read()
data.close()
eta = int(raw.split('\n')[0])
all_buses = list((raw.split('\n')[1]).split(','))
running = [int(i) for i in all_buses if i != 'x']
time = eta #start waiting when you've arrived
leaving_now = False #are you leaving at this time

while leaving_now == False:
    
    print(time)    
    buses = np.divide(time, running)
    floor = np.floor(np.divide(time, running))
    bus_here = any(buses == floor) # has one of the buses arrived in this time period?
    if bus_here == True:
        bus_id = running[np.argmax(np.where(buses == floor, 1, 0))]
        leaving_now = True
        print('You waited for: '+str(time - eta),
              '\nYou took bus number: '+str(bus_id),
              '\nResult: ' + str((time - eta) * bus_id)
              )
    else:
        time += 1