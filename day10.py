# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:08:05 2020

ADVENT OF CODE 2020: Day 10

@author: murph
"""
import numpy as np

"""Part 1"""
data = open('c:/Users/murph/Documents/projects/advent of code/input10.txt', 'r')
bulk = data.read()
split = bulk.split('\n')
data.close()

x = np.array(list(map(int, split[:-1])))
device = max(x) + 3
x = np.append(x, device)
chain = []
mins = []

current = 0
#goes in loop for each step in chain
for i in range(len(x)):
    diff = x - current
        
    eligible = np.where(np.logical_and(diff>=1, diff<=3))[0] #index values of eligible adapters
    eligible_values = diff[eligible] #pull eligible differences
    min_diff = min(eligible_values) #minimum difference
    mins.append(min_diff) #add minimum difference to list for final calc
    index_min = eligible[np.argmin(eligible_values)] #index value of min diff
    chain.append(x[index_min]) #use index_min to select the correct adapter from the master list, append to chain
    current = x[index_min]

ones = len([i for i in mins if i == 1])
threes = len([i for i in mins if i == 3])
score = ones * threes

"""Part 2"""
