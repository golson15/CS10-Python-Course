#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:13:45 2019

@author: Grace Olson
"""


#Point tracker
score = 0

#Title
print("------------------")
print(" Housing Priority")
print("------------------")

YEAR_1 = 1
YEAR_2 = 2
YEAR_3 = 3
YEAR_4 = 4

INCREASE_WEIGHT = 2

#Assigning points based on how many units have been completed thus far
units = int(input("How many units have you completed?: "))

if units >= 92:    #senior
    score += YEAR_4 * INCREASE_WEIGHT
elif units >= 59:  #junior
    score += YEAR_3 * INCREASE_WEIGHT       
elif units >= 26:  #sophomore
    score += YEAR_2 * INCREASE_WEIGHT
elif units >= 0:  #freshman
    score += YEAR_1 * INCREASE_WEIGHT

#Assigning additional points
#If taking more than four classes then add one point
number_of_units = int(input("How many units are you planning to take this semester?: "))
if int(number_of_units) > 18:
    score += 1
    
#If GPA is over 3.5, then add one point (maybe the GPA value could be changed...?)
gpa = float(input("What is your current GPA?: "))
if float(gpa) >= 3.5:
    score += 1

#If the student earned a scholarship then add one point
scholarship = input("Did you earn a scholarship? (Yes/No): ")

if str(scholarship) == "Yes":
    score += 1
elif str(scholarship) == "No":
    score += 0 
    
#If the student is an athlete, then +1
athlete = input("Are you an athlete? (Yes/No): ")

if str(athlete) == "Yes":
    score += 1
elif str(athlete) == "No":
    score += 0

#If the student has a physical/mental disability then add one
disability = input("Do you have a physical or mental disability? (Yes/No): ")

if str(disability) == "Yes":
    score += 1
elif str(disability) == "No":
    score += 0

#For any violations of community guidelines subtract 1
violation_of_guidelines = input("Have you ever violated the Community Life Statement and/or the dorm hall guidelines?(Yes/No): ")

if str(violation_of_guidelines) == "Yes":
    score -= 1
elif str(violation_of_guidelines) == "No":
    score += 0

#For any chapel probation subtract 1
chapel_probation = input("In the last semester were you ever on chapel probation? (Yes/No): ")

if str(chapel_probation) == "Yes":
    score -= 1
elif str(chapel_probation) == "No":
    score += 0
    
#For any academic probation subtract 1
academic_probation = input("In the last semester were you ever on academic probation? (Yes/No): ")

if str(academic_probation) == "Yes":
    score -= 1
elif str(academic_probation) == "No":
    score += 0  




#Printing the user's housing score
print("----------------------------------------------------------------------------------")
print("Your housing priority score is", score)



