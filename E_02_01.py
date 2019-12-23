#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:02:03 2019

@author: Grace Olson
"""
#Ask the user to input information about the gas in the tank
gasGallons = float(input("Enter the number of gallons of gas in the tank: "))
fuelEfficiency = float(input("Enter the fuel efficiency in miles per gallon: "))
gasPrice = float(input("Enter the price of gas per gallon: "))

#Use the constant 100 to multiply the gas price by
GAS_MILES = 100

#Print the cost of gas per 100 miles
print("The cost of gas per 100 miles is: ", gasPrice * GAS_MILES, "dollars")

#Print how far the car can go with the gas in the tank
print("The car can go: ", gasGallons * fuelEfficiency, "miles")
