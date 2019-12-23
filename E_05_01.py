#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 18:23:13 2019

Income Analysis- Episteme 05

@author: Grace Olson and Jack Chiplin
"""

#import data 
import csv

#define and add 14 arguments to the decideOver50K function that correspond with the Census categories
def decideOver50K(age, workClass, fnlWgt, education, educationNum, maritalStatus, occupation, relationship, race, sex, capitalGain, capitalLoss, hoursPerWeek, nativeCountry) :
    predictOver = False #initialize predictOver to be False
    points = 0 #initialize points to be zero
#predict whether over 50K based on age
    if (age > 40): 
        points += 1
    if (age < 25):
        points -= 1
#predict whether over 50K based on work class
    if (workClass == ("State-gov")):
        points -= 1
    if (workClass == ("Self-emp-not-inc")):
        points -= 1
    if (workClass == ("Self-emp-inc")):
        points += 1
#predict whether over 50K based on education
    if (education == ("Doctorate")):
        points += 3
    if (education == ("Masters")):
        points += 3
    if (education == ("Some-college")):
        points += 1
    if (education == ("Bachelors")):
        points += 2
    if (education == ("Prof-school")):
        points += 1
    if (education == ("HS-grad")):
        points -= 1
    if (education == ("11th")):
        points -= 1
    if (education == ("10th")):
        points -= 1
    if (education == ("9th")):
        points -= 1
#predict whether over 50K based on education number
    if (educationNum > 14):
        points += 2
    if (educationNum < 11):
        points -= 1
#predict whether over 50K based on marital status
    if (maritalStatus == ("Married-civ-spouse")):
        points += 2
    if (maritalStatus == ("Never-married")):
        points -= 1
#predict whether over 50K based on occupation
    if (occupation == ("Exec-managerial")):
        points += 3
    if (occupation == ("Tech-support")):
        points += 2
    if (occupation == ("Handlers-cleaners")):
        points -= 1
    if (occupation == ("Farming-fishing")):
        points -= 1
    if (occupation == ("Transport-moving")):
        points -= 1
    if (occupation == ("Machine-op-inspct")):
        points -= 1
    if (occupation == ("Sales")):
        points += 1
    if (occupation == ("Prof-specialty")):
        points += 1
#predict whether over 50K based on relationship
    if (relationship == ("Husband")):
        points += 1
    if (relationship == ("Wife")):
        points += 1
    if (relationship == ("Own-child")):
        points -= 1
#predict whether over 50K based on race
    if (race == ("White")):
        points += 1
#predict whether over 50K based on sex
    if (sex == ("Male")):
        points += 1
#predict whether over 50K based on capital gain
    if (capitalGain > 0):
        points += 1
#predict whether over 50K based on capital loss
    if (capitalLoss > 0):
        points += 1
#predict whether over 50K based on hours per week
    if (hoursPerWeek < 20):
        points -= 3
    if (hoursPerWeek > 70):
        points -= 1
#predict whether over 50K based on native country
    if (nativeCountry == ("Mexico")):
        points -= 1
    if (nativeCountry == ("Jamaica")):
        points -= 1
    if (nativeCountry == ("South")):
        points -= 1
        
#See whether each test case passes the point threshhold required
    if (points > 6):
        predictOver = True
    elif (points <= 6):
        predictOver = False
#return the predictOver variable for each test case as True or False
    return predictOver


#Here are the test functions
def test1():
    predictOver = decideOver50K(48,"Private",285570,"HS-grad",9,"Married-civ-spouse","Adm-clerical","Husband","White","Male",0,0,40,"United-States")
    if(not predictOver):
        print("Test case 1 is <=50K: Pass")
    else:
        print("Test case 1 is <=50K: Fail")

def test2():
    predictOver = decideOver50K(61,"Private",89686,"HS-grad",9,"Married-civ-spouse","Sales","Husband","White","Male",0,0,48,"United-States")
    if(not predictOver):
        print("Test case 2 is <=50K: Pass")
    else:
        print("Test case 2 is <=50K: Fail")

def test3():
    predictOver = decideOver50K(31,"Private",440129,"HS-grad",9,"Married-civ-spouse","Craft-repair","Husband","White","Male",0,0,40,"United-States")
    if(not predictOver):
        print("Test case 3 is <=50K: Pass")
    else:
        print("Test case 3 is <=50K: Fail")

def test4():
    predictOver = decideOver50K(25,"Private",350977,"HS-grad",9,"Never-married","Other-service","Own-child","White","Female",0,0,40,"United-States")
    if(not predictOver):
        print("Test case 4 is <=50K: Pass")
    else:
        print("Test case 4 is <=50K: Fail")

def test5():
    predictOver = decideOver50K(48,"Local-gov",349230,"Masters",14,"Divorced","Other-service","Not-in-family","White","Male",0,0,40,"United-States")
    if(not predictOver):
        print("Test case 5 is <=50K: Pass")
    else:
        print("Test case 5 is <=50K: Fail")

def test6():
    predictOver = decideOver50K(35,"Self-emp-inc",182148,"Bachelors",13,"Married-civ-spouse","Exec-managerial","Husband","White","Male",0,0,60,"United-States")
    if( predictOver):
        print("Test case 6 is >50K: Pass")
    else:
        print("Test case 6 is >50K: Fail")

def test7():
    predictOver = decideOver50K(47,"Private",51835,"Prof-school",15,"Married-civ-spouse","Prof-specialty","Wife","White","Female",0,1902,60,"Honduras")
    if( predictOver):
        print("Test case 7 is >50K: Pass")
    else:
        print("Test case 7 is >50K: Fail")
        
def test8():
    predictOver = decideOver50K(50,"Federal-gov",251585,"Bachelors",13,"Divorced","Exec-managerial","Not-in-family","White","Male",0,0,55,"United-States")
    if( predictOver):
        print("Test case 8 is >50K: Pass")
    else:
        print("Test case 8 is >50K: Fail")
        
def test9():
    predictOver = decideOver50K(43,"Private",237993,"Some-college",10,"Married-civ-spouse","Tech-support","Husband","White","Male",0,0,40,"United-States")
    if( predictOver):
        print("Test case 9 is >50K: Pass")
    else:
        print("Test case 9 is >50K: Fail")

def test10():
    predictOver = decideOver50K(38,"Private",278924,"Bachelors",13,"Married-civ-spouse","Exec-managerial","Husband","White","Male",0,1887,50,"United-States")
    if( predictOver):
        print("Test case 10 is >50K: Pass")
    else:
        print("Test case 10 is >50K: Fail")

#This loads an additional 32562 tests and evaluates decideOver50K
def bigTest():
    correct=0
    incorrect = 0
    with open('data.csv',newline='') as csvfile:
        dataReader = csv.reader(csvfile, delimiter=',',quotechar="'")
        for row in dataReader:
            for i in range(len(row)):
                data = row[i].strip()
                data = data.strip(".")
                row[i]=data
#            print(row)
            predictOver = decideOver50K(int(row[0]),row[1],int(row[2]),row[3],int(row[4]),row[5],row[6],row[7],row[8],row[9],int(row[10]),int(row[11]),int(row[12]),row[13])
            if row[14] == ">50K":
                if predictOver:
                    correct = correct + 1
                else:
                    incorrect = incorrect +1
            else:
                if predictOver:
                    incorrect = incorrect + 1
                else:
                    correct = correct +1
    print("On the 32,562 tests you got %d/%d = %.1f%% correct" %(correct,(correct+incorrect),100.0*correct/(correct+incorrect)))

#This loads an additional 16,283 tests and evaluates decideOver50K
#It is commented out until Prof. Patterson is ready to grade
def hiddenTest():
    print("Hidden test not run")
#    correct=0
#    incorrect = 0
#    with open('test.csv',newline='') as csvfile:
#        dataReader = csv.reader(csvfile, delimiter=',',quotechar="'")
#        for row in dataReader:
#            for i in range(len(row)):
#                data = row[i].strip()
#                data = data.strip(".")
#                row[i]=data
#            predictOver = decideOver50K(int(row[0]),row[1],int(row[2]),row[3],int(row[4]),row[5],row[6],row[7],row[8],row[9],int(row[10]),int(row[11]),int(row[12]),row[13])
#            if row[14] == ">50K":
#                if predictOver:
#                    correct = correct + 1
#                else:
#                    incorrect = incorrect +1
#            else:
#                if predictOver:
#                    incorrect = incorrect + 1
#                else:
#                    correct = correct +1
#    print("On the 16,283 tests you got %d/%d = %.1f%% correct" %(correct,(correct+incorrect),100.0*correct/(correct+incorrect)))


def main():
#Here are ten tests
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    bigTest()
    hiddenTest()
    
    
        
main()

'''
Analysis Comments:

We have learned that the U.S income distribution has most people earning less 
than 50k a year. Only around 8 thousand people out of the 32,000 that the sample
includes made over 50k. The biggest factors in this seem to be level of education,
occupation, age, and how many hours worked each week. 

People are much more likely to be under the 50k mark if they worked either less
than 20 or more than 70 hours per week, if they are an Own-child, their occupation
is Handlers-cleaners, Farming-fishing, Transport-moving, or Machine-Op-inspector, 
if they were never married, if they have an education number less than 11, if 
they graduated high school only or had less education than high school, if their
state-employed-not-inc, or state-gov, or if they are less than 25. 

On the other hand, those that have increased their likelihood of making over 50k 
are those who are married, over 40, self-employed-inc, graduated with a doctorate,
bachelors, masters, some-college or prof-school, if their education number is higher
than 14, if they work as exec-managerial, tech-support, sales, or prof-specialty, 
if they are White or Male, or if they have any capital gain or loss.

'''





