#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Episteme 06_01 Water Level

Created on Mon Oct 14 19:47:01 2019

@author: Grace Olson and Jack Chiplin
"""

#Make flood map function
def floodMap(terrainMap, waterLevel):
    for x in range(10) : 
        for y in range(10) : 
            if terrainMap [x][y] < waterLevel :
                print("W", end = "") #for where water floods
            else :
                print(".", end="") #for where water doesn't flood
            if [y] == [9] :
                print("") #to break up the lines
  
