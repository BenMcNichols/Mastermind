# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:08:54 2021

@author: bmcn6
"""

import time
import random


# New Game Setup
def newGame():
    print("ENTER 4-PEG SEQUENCE")
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
    print(turnNumber,guessHistory,responseHistory)
    colorList = ["A", "B", "C", "D", "E", "F"]
    #First, iterate through possible answers
    viableGuesses = [] # list of viable guesses
    for position1 in colorList:
        for position2 in colorList:
            for position3 in colorList:
                for position4 in colorList:
                    guessSequence = [position1, position2, position3, position4]
                    if guessSequence in guessHistory:
                        continue
                    guessResponseHistory = [] # list to mimic response history
                    #print(guessSequence)
                    for cluePair in range(turnNumber):
                        blackTestList = [] #if peg would be black, add peg index to list
                        whiteTestList = [] # if peg would be white, add peg to list (Not index?)
                        #print("Begin Black Checking")
                        for peg in range(len(guessSequence)):
                            #print("Peg = ",peg)
                            if guessSequence[peg]==guessHistory[cluePair][peg]:
                                
                                #print(guessSequence[peg],guessHistory[cluePair][peg])
                                #print("BlackDing")
                                blackTestList.append(peg) 
                                
                        #print("Conclusion: Black", len(blackTestList))
                        
                        #remove black pegs from guess & historical list
                        TempHistList = guessHistory[cluePair][:] # temp list to remove values from
                        TempGuessList = guessSequence[:] # temp list to remove values from
                        for blackpeg in blackTestList[::-1]:
                            del TempHistList[blackpeg]
                            del TempGuessList[blackpeg]
                        #print("Remaining Guess List",TempGuessList)
                        
                        #print("Begin White Checking")
                        WhiteTempHistList = TempHistList[:]
                        matchHistList = []
                        matchGuessList = []
                        for i in range(len(TempHistList)):
                            for j in range(len(TempGuessList)):
                                #print("i,J=",i,j)
                                if TempHistList[i] == TempGuessList[j]:
                                    if i not in matchHistList and j not in matchGuessList:
                                        whiteTestList.append(TempHistList[i])
                                    matchHistList.append(i)
                                    matchGuessList.append(j)
                                    
                        #print("### Analysis Complete ###")
                        #print("Black Peg Count:",len(blackTestList))
                        #print("White Peg Count:",len(whiteTestList))
                        guessResponseHistory.append([len(blackTestList),len(whiteTestList)])    
                    #print(guessResponseHistory)
                    # is the guess viable when compared to previous answers?
                    if guessResponseHistory == responseHistory:
                        #print("This is a good guess to make:", guessSequence)
                        viableGuesses.append(guessSequence)
                        #removed break statement here - think it was causing issues
    
    #print the final viable guess list:
    print("Guess Options:",viableGuesses)
    return(viableGuesses)
                    

# Check if the guess matches the existing chips
def checkGuess():
    return
    
''''Actual program starts here'''

secretSequence = newGame()

guessHistory = []

responseHistory = []

turnNumber = 0 #Turn 1

for turnNumber in range(8):
    print("Turn #", turnNumber+1)
    viableGuesses = generateGuess(turnNumber,guessHistory,responseHistory)
    
    print("Number of options = ",len(viableGuesses))
    if len(viableGuesses)>0:
        #if there are any options left:
            #pick a random option from the list and set it as your guess
        myGuess = viableGuesses[random.randint(0,len(viableGuesses)-1)]
        print("        My Guess Is:", myGuess)
        guessHistory.append(myGuess)
        print("(Secret Sequence is:", secretSequence)
        print("Number of Black:")
        blackPegCount = int(input())
        print("Number of White Pegs")
        whitePegCount = int(input())
        responseHistory.append([blackPegCount,whitePegCount])
        
        #Win Condition
        if blackPegCount == 4:
            print("I Won in ",turnNumber+1,"Turns!")
            break
        
    else:
        print("I give up! You win!")
        break
        


        
    
    