#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Episteme 09_02

Created on Fri Nov  8 15:35:18 2019

@author: Grace Olson
"""


class ComboLock :
    def __init__(self, secret1, secret2, secret3) :
        #initialize all instance variables
        #make an emppty list for direction
        self._direction = []
        #set dial to zero
        self._dial = 0
        #create the correct combo using the secret numbers in a list
        self._secretCombo = [secret1, secret2, secret3]
        #create an empty list for the inputed combo
        self._comboList = []
        
    def reset(self) : 
        #set dial to zero
        self._dial = 0 
        
    def turnLeft(self, ticks) : 
        #add an L to the direction list to make sure the user goes Right, Left, Right
        self._direction.append("L")
        #set the dial to the absolute value of dial plus ticks
        self._dial = abs(self._dial + ticks)
        #add where the dial ends up to the combo list to check later
        self._comboList.append(self._dial)
           
    def turnRight(self, ticks) :
        #add an R to the direction list to make sure the user goes Right, Left, Right
        self._direction.append("R")
        #set the dial to the absolute value of dial plus ticks minus 40
        self._dial = abs(self._dial + ticks - 40)
        #add where the dial ends up to the combo list to check later
        self._comboList.append(self._dial)
        
    #Returns True or False
    def open(self) :
        #check if the direction list is equal to Right, Left, Right
        #check if the combo list is equal to the correct combo with the secret numbers
        return self._direction == ["R", "L", "R"] and self._comboList == self._secretCombo

