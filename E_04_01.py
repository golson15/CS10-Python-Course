#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 20:35:16 2019

@author: Grace Olson and Jack Chiplin
"""
#Referenced Dr. Patterson's code from help session

# import library for finding random numbers
import random

#initialize a variable for each strategy (either switching or not switching)
strategySwitch = 0
strategyNoSwitch = 0

#Create a simulation for 1,000 runs of the game 
while strategySwitch + strategyNoSwitch < 1000:
    doorCar = random.randint(1,3) #Assign the car to a random door
    doorPick = random.randint(1,3) #Assign the contestant's choice to a random door
    doorReveal = random.randint(1,3) #Assign the door revealed to a random door
    while (doorReveal == doorPick) or (doorReveal == doorCar) : #keep picking a door until it is not the one the contestant picked and not the one with the car behind it
        doorReveal = random.randint(1,3)
    if doorCar != doorPick :
        strategySwitch = strategySwitch + 1 #if the contestant didn't pick the door with the car behind it, they would win if they switched
    else :
        strategyNoSwitch = strategyNoSwitch + 1 #if the contestant did pick the door with the car behind, they would win if they did not switch

print (strategySwitch) 
print (strategyNoSwitch)


