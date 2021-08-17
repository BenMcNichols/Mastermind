# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:08:54 2021

@author: bmcn6
"""

import time


# New Game Setup
def newGame():
    print("ENTER SEQUENCE")
    print("COLORS: A,B,C,D,E,F")
    secretSequence = []
    for i in range(4):
        print("Enter Peg #",i+1,":")
        peg = input()
        secretSequence.append(peg)
    print("Secret Sequence =",secretSequence)
    time.sleep(2)
    return secretSequence

# Generaete a new guess which meets the rules
def generateGuess(turnNumber,guessHistory, responseHistory):
    guessResponseHistory = [] # list to mimic response history
    for cluePair in range(turnNumber):
        blackTestList = [] #if peg would be black, add peg index to list
        whiteTestList = [] # if peg would be white, add peg to list (Not index?)
        print("Begin Black Checking")
        for peg in range(len(guessSequence)):
            print("Peg = ",peg)
            if guessSequence[peg]==guessHistory[cluePair][peg]:
                
                print(guessSequence[peg],guessHistory[cluePair][peg])
                print("BlackDing")
                blackTestList.append(peg) 
                
        print("Conclusion: Black", len(blackTestList))
        
        #remove black pegs from guess & historical list
        TempHistList = guessHistory[cluePair][:] # temp list to remove values from
        TempGuessList = guessSequence[:] # temp list to remove values from
        for blackpeg in blackTestList[::-1]:
            del TempHistList[blackpeg]
            del TempGuessList[blackpeg]
        print("Remaining Guess List",TempGuessList)
        
        print("Begin White Checking")
        WhiteTempHistList = TempHistList[:]
        matchHistList = []
        matchGuessList = []
        for i in range(len(TempHistList)):
            for j in range(len(TempGuessList)):
                print("i,J=",i,j)
                if TempHistList[i] == TempGuessList[j]:
                    if i not in matchHistList and j not in matchGuessList:
                        whiteTestList.append(TempHistList[i])
                    matchHistList.append(i)
                    matchGuessList.append(j)
                    
        print("### Analysis Complete ###")
        print("Black Peg Count:",len(blackTestList))
        print("White Peg Count:",len(whiteTestList))
        guessResponseHistory.append([len(blackTestList),len(whiteTestList)])    
    
    # is the guess viable when compared to previous answers?
    if guessResponseHistory == responseHistory:
        print("This is a good guess to make:", guessSequence)
        return True
            
                
            
        
    
    #Then, check if answer matches previous responses

# Check if the guess matches the 
def checkGuess():
    return
    
''''Actual program starts here'''

secretSequence = ["A","C","B","D"] #newGame()

guessHistory = [["A","B","C","D"]]
responseHistory = [[2,2]]

for turnNumber in range(8):
    print("Turn #", turnNumber+1)
    generateGuess(turnNumber,guessHistory,responseHistory)
    