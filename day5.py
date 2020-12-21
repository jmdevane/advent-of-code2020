# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 08:30:04 2020

ADVENT OF CODE 2020 -- DAY 5

@author: murph
"""

import numpy as np

data = open('c:/Users/murph/Documents/projects/advent of code/input5.txt', 'r')
bulk = data.read()
passes = bulk.split('\n')[:-1]
data.close()

ids = []

for p in range(len(passes)):
# p=1 #test one pass
    pass_ = passes[p]
    remaining_rows = np.arange(128)
    remaining_cols = np.arange(8)
    row_codes = pass_[:7]
    col_codes = pass_[7:]
    
    for r in range(len(row_codes)):
        
        half = int(len(remaining_rows) / 2)
        if row_codes[r] == 'F':
            remaining_rows = remaining_rows[:half]
        else:
            remaining_rows = remaining_rows[half:]
        # print(remaining_rows)
       
    for c in range(len(col_codes)):
        
        half = int(len(remaining_cols) / 2)
        if col_codes[c] == 'R':
            remaining_cols = remaining_cols[half:]
        else:
            remaining_cols = remaining_cols[:half]
        # print(remaining_cols)
            
    row = remaining_rows[0]
    col = remaining_cols[0]
    seat_id = row * 8 + col
    ids.append(seat_id)
    print(p)

max_id = max(ids)  
print(max_id)