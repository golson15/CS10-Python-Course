# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:49:44 2019

@authors: Megan Davis and Grace Olson
CS-010-01
Episteme 7 - Paired Programing

"""
#E_07_01

def wordCounter(fileName, wordList): #define function
    try:
        for word in wordList:
            word = word.lower() #make words in wordList lowercase
            count = 0 #initialize count
            inputFile = open(fileName, "r") #read file
            line = inputFile.readline()
            while line != "": #read till end of script
                line = line.rstrip() #strip newline character from inputFile
                line = line.lower() #make lines in file lowercase
                wlist = line.split() #split lines into words from inputFile
                for word1 in wlist: #dealing inputFile words
                    word1 = word1.rstrip(".,?!") #removing punctutation
                    if word1 == word: #asking if file wrds match words from wodList
                        count = count + 1 #count when there is a match
                line = inputFile.readline() #make sure it continues the loop
            print (word,":",count) #print words in wordList and their count
    except IOError: #raise an exception
        print ("Error: file not found") #print an error if there is one
        for word in wordList:
            print(word, ":", "0") #print count for wordlist when error
            

    