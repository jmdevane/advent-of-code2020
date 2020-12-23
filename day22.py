# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:40:43 2020

ADVENT OF CODE 2020 -- DAY 22

@author: murph
"""

import numpy as np

data = open('c:/Users/murph/Documents/projects/advent of code/input22.txt', 'r')
raw = data.read()
data.close()
master = raw.split('\n\n')
p1 = master[0].split(':')[1].split('\n')[1:]
p2 = master[1].split(':')[1].split('\n')[1:-1]
p1 = list(map(int, p1))
p2 = list(map(int, p2))

rounds = []
r = 0 #starting round number

while (len(p1) > 0) | (len(p2) > 0):
    p1_card = p1.pop(0) #draw top card for each player
    p2_card = p2.pop(0)
    hand = sorted([p1_card, p2_card], reverse=True)
    
    if p1_card > p2_card:
        
        p1 = p1 + hand
        
    else:
        
        p2 = p2 + hand
    
    r +=1
    if (len(p1) == 0) | (len(p2) == 0):
        break
    
end = [p1, p2]    
winner = end[np.argmax(end)]
renniw = winner[::-1]

tally = []
points = 1

for i in renniw:
    
    tally.append(i * points)
    points+=1
    
score = np.sum(tally)
