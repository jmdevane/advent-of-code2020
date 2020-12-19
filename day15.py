# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:56:31 2020

ADVENT OF CODE 2020 -- DAY 15

@author: murph
"""

#PART ONE
import numpy as np
from tqdm import trange

seed = [8,13,1,0,18,9]
annex = [0] * (2020 - len(seed))
composite = seed + annex

for i in trange(6, 2020):
    
    if composite[i-1] in composite[:i-1]:
        
        age = (i - ((len(composite[:i-1]) - 1) - 
                            composite[:i-1][::-1].index(composite[i-1])+ 1))
        
    else:
        
        age = 0
    
    composite[i] = age


#part 2, ripped from reddit

def main():
    input_string = "11,18,0,20,1,7,16"
    #input_string = "0,3,6"
    numbers = {int(i):index 
            for index,i in enumerate(input_string.split(","),start=1)}

    n = len(numbers)+1
    number_to_be_spoken = 0

    while n<3000000:

        if number_to_be_spoken in numbers.keys():
            next_number = n - numbers[number_to_be_spoken]
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = next_number
        else:
            numbers[number_to_be_spoken] = n
            number_to_be_spoken = 0
        n+=1
    print(number_to_be_spoken)