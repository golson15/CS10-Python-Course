#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Episteme 06_2 Water Percent

Created on Mon Oct 14 12:16:56 2019

@author: Grace Olson and Jack Chiplin
"""

#this was a sad attempt

#make flood damage function
def floodDamage(heights,percent): 
    for x in range(10) : 
        for y in range(10) : 
            if heights [x][y] == percent:
                print("W", end = "") #marking where flooded
            else:
                print(".", end="") #marking where not flooded
            if [y] == [9] :
                print("") 


    
    
    
  



