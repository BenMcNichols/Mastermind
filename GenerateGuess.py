# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:50:55 2021

@author: bmcn6
"""

#generate guess function

secretSequence = ["A","C","B","D"] # not used in code, just for my thinking

turnNumber = 3 #2nd turn

guessHistory = [["A","A","D","B"],["A","C","D","B"],["B","C","D","A"]]

responseHistory = [[1,2],[2,2],[1,3]]

print(turnNumber,guessHistory,responseHistory)
colorList = ["A", "B", "C", "D"]
#First, iterate through possible answers
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
                    print("This is a good guess to make:", guessSequence)
                    break