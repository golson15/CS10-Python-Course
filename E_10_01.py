#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 21:34:48 2019

@author: Grace Olson and Jack Chiplin
Episteme 10
"""

#create super class Person
class Person:
    #initialize variables to proper type and values
    def __init__(self, name = "", birthYear = 1970):
        self._name = str(name)
        if not self._name.isdigit():
            self._name = name
        else: 
            raise ValueError
        self._birthYear = str(birthYear)
        if self._birthYear.isdigit():
            self._birthYear = birthYear
        else: 
            raise ValueError
        self._birthYear = int(self._birthYear)
        if self._birthYear < 1900:
            raise ValueError
        if self._birthYear > 2016:
            raise ValueError
            
    def setName(self, name):
        #set name
        self._name = name
        
    def setBirthYear(self, birthYear):
        #set birth year
        self._birthYear = birthYear
        if self._birthYear < 1900:
            raise ValueError
        if self._birthYear > 2016:
            raise ValueError
            
    def getName(self):
        #return name
        return self._name
        
    def getBirthYear(self):
        #return birth year
        return self._birthYear
        
    def __repr__(self):
        #give representation of class
        return "Name: %s, Year of Birth: %d"% (self._name, self._birthYear) 
    

#create sub class Student   
class Student(Person):
    #initialize variables to proper type and values
    def __init__(self, name = "", birthYear =  1970, major = "Computer Science"):
        super().__init__(name, birthYear)   
        self._major = str(major)
        if not self._major.isdigit():
            self._major = major
        else: 
            raise ValueError
            
    def setMajor(self, major):
         #set major
        self._major = major
        
    def getMajor(self, major = "Computer Science"):
        #return major
        return self._major

    def __repr__(self):
        #give representation of class
        return "Name: %s, Year of Birth: %d, Major: %s"% (self._name, self._birthYear, self._major)  
    
    
#create sub class Professor
class Professor(Person):
    #initialize variables to proper type and values
    def __init__(self, name = "", birthYear =  1970, salary = 0):
        super().__init__(name, birthYear)   
        self._salary = str(salary)
        if self._salary.isdigit():
            self._salary = salary
        else: 
            raise ValueError
            
    def setSalary(self, salary):
        #set salary
        self._salary = salary
        
    def getSalary(self, salary = 0):
        #return salary
        return self._salary

    def __repr__(self):
        #give representation of class
        return "Name: %s, Year of Birth: %d, Salary: %d"% (self._name, self._birthYear, self._salary)
        
    