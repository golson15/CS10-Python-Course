#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:06:46 2019

@author: Grace Olson
"""


inputCountry = input(print("Please enter a country (\"q\" to quit): "))


lifedata = {} 
while inputCountry != "q":
    inFileLife = open("life.txt" , "r")
    line = inFileLife.readline()
    while line != "":
        splitline = line.split()
        

if inputCountry in dict:
    print (dict[inputCountry])


print(lifedata)    
    
    
'''
while inputCountry != "q":  
    if inputCountry in lifedata:
        print("Life Expectancy is" , lifedata[inputCountry], "years at birth")


inFileGini = open("gini.txt" , "r")
Gini = inFileGini.readline()

'''
'''
psuedocode:

read life expectancy for a country
read input of country
use country as key
print value

'''
'''
d = {}
with open("life.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[key] = float(val)


lifeExpectancy = inFileLife.readline()

newDict = {}
with open('testFile.txt', 'r') as f:
        for line in f:
            splitLine = line.split()
            newDict[int(splitLine[0])]
'''










            