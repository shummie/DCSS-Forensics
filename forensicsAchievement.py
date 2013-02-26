#   Copyright (C) 2013  Raymond Shum
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.


## This module is the forensicsAchievement module. This module takes a
## gameCollection object and reads the gameInfo data list (gameList) and
## determines which achievements are earned.
## Achievements are stored in the gameCollection object in a list called
## achievementList. The list consists of a series of True/False by ID
## which corresponds to the dictionary dAchievementList InternalID number.

import forensicsDictionary

def forensicsAchievement(gameCollection):

    while len(gameCollection.achievementList) < len(forensicsDictionary.dAchievementList):
        gameCollection.achievementList.append(False)

    if gameCollection.achievementList[0][0] == False:
        gameCollection.achievementList[0] = _0_CheckAnyWin(gameCollection)
    if gameCollection.achievementList[1][0] == False:
        gameCollection.achievementList[1] = _1_CheckAnyLevel27(gameCollection)
    if gameCollection.achievementList[2][0] == False:
        gameCollection.achievementList[2] = _2_CheckAny15RuneWin(gameCollection)
    if gameCollection.achievementList[3][0] == False:
        gameCollection.achievementList[3] = _3_SlowAndSteady1(gameCollection)
    if gameCollection.achievementList[4][0] == False:
        gameCollection.achievementList[4] = _4_SlowAndSteady2(gameCollection)
    if gameCollection.achievementList[5][0] == False:
        gameCollection.achievementList[5] = _5_SlowAndSteady3(gameCollection)
    if gameCollection.achievementList[6][0] == False:
        gameCollection.achievementList[6] = _6_Explorer1(gameCollection)
    if gameCollection.achievementList[7][0] == False:
        gameCollection.achievementList[7] = _7_Explorer2(gameCollection)
    if gameCollection.achievementList[8][0] == False:
        gameCollection.achievementList[8] = _8_Explorer3(gameCollection)
    if gameCollection.achievementList[9][0] == False:
        gameCollection.achievementList[9] = _9_Pious1(gameCollection)
    if gameCollection.achievementList[10][0] == False:
        achievement = _10_11_Pious_2_3(gameCollection)
        gameCollection.achievementList[10] = achievement[0]
        gameCollection.achievementList[11] = achievement[1]
    if gameCollection.achievementList[12][0] == False:
        gameCollection.achievementList[12] = _12_NaturesAlly1(gameCollection)    
    if gameCollection.achievementList[13][0] == False:
        gameCollection.achievementList[13] = _13_NaturesAlly2(gameCollection)
    if gameCollection.achievementList[14][0] == False:
        gameCollection.achievementList[14] = _14_NaturesAlly3(gameCollection)    
    if gameCollection.achievementList[15][0] == False:
        gameCollection.achievementList[15] = _15_GelatinousBody1(gameCollection)
    if gameCollection.achievementList[16][0] == False:
        gameCollection.achievementList[16] = _16_GelatinousBody2(gameCollection)
    if gameCollection.achievementList[17][0] == False:
        gameCollection.achievementList[17] = _17_GelatinousBody3(gameCollection)
    if gameCollection.achievementList[18][0] == False:
        gameCollection.achievementList[18] = _18_LordOfDarkness1(gameCollection)
    if gameCollection.achievementList[19][0] == False:
        gameCollection.achievementList[19] = _19_LordOfDarkness2(gameCollection)  
    if gameCollection.achievementList[20][0] == False:
        gameCollection.achievementList[20] = _20_LordOfDarkness3(gameCollection)
    

def _0_CheckAnyWin(gameCollection):
    # InternalID: 0
    # Has the player won the game?
    for game in gameCollection.gameList:
        if game.winFlag == True: return [True, "Complete!"]
    return [False, ""]

def _1_CheckAnyLevel27(gameCollection):
    # InternalID: 1
    # Has the player reached level 27 in any game?
    maxLevel = 0
    for game in gameCollection.gameList:
        if game.level == 27: return [True, "Complete!"]
        elif game.level > maxLevel: maxLevel = game.level
    return [False, "Max Level: " + str(maxLevel)]

def _2_CheckAny15RuneWin(gameCollection):
    # InternalID: 2
    # Has the player won the game with 15 runes?
    maxRunes = 0
    for game in gameCollection.gameList:
        if (game.winFlag == True) and (game.numRunes == 15): return [True, "Complete!"]
        elif game.numRunes < maxRunes: maxRunes = game.numRunes
    return [False, "Max Runes: " + str(maxRunes)]

def _3_SlowAndSteady1(gameCollection):
    # Internal ID: 3
    # Check that there are two characters in a row with XL:9
    i = 0
    levelCount = 0
    while (i < len(gameCollection.gameList)) and (levelCount < 2):
        if gameCollection.gameList[i].level >= 9: levelCount += 1
        else: levelCount = 0
    if levelCount < 2: return [False, ""]
    else: return [True, "Complete!"]
        
def _4_SlowAndSteady2(gameCollection):
    # Achieve a 2-win streak
    # Currently no streak detection coded, so this will need to be rewritten
    return [False, "Not yet implemented"]

def _5_SlowAndSteady3(gameCollection):
    # Achieve a 4-win streak with 4 different Species & Classes
    # Currently no streak detection coded, so this will need to be rewritten
    return [False, "Not yet implemented"]

def _6_Explorer1(gameCollection):
    # After entering Lair the first time, reach Lair 8 before returning to the dungeon
    for game in gameCollection.gameList:
        achieveStep = 0
        i = 0
        while (i < len(game.notesList)) and (achieveStep < 2):
            if game.notesList[i][1] == "Lair:1": achieveStep = 1
            if achieveStep == 1:
                if game.notesList[i][1][:2] == "D:": achieveStep = 2
                elif game.notesList[i][1] == "Lair:8": return [True, "Complete!"]
            i += 1
    return [False, ""]

def _7_Explorer2(gameCollection):
    # Win a game in where when you enter a branch for the 1st time, you reach the end of the branch before leaving
    return [False, "Not yet Implemented"]            

def _8_Explorer3(gameCollection):
    # Win a game as in II, except all subbranches must be completed before leaving the branch. I.e., all subbranches of Lair must be complete before leaving Lair
    return [False, "Not yet implemented"]

def _9_Pious1(gameCollection):
    # Champion a god
    maxPiety = 0
    for game in gameCollection.gameList:
        if game.pietyLevel == 6: return [True, "Complete!"]
        elif game.pietyLevel > maxPiety: maxPiety = game.pietyLevel 
    return [False, "Max Piety: " + ("*" * maxPiety)]

def _10_11_Pious_2_3(gameCollection):
    # Champion 5 gods and 13 gods
    champList = []
    for game in gameCollection.gameList:
        if game.pietyLevel == 6:
            if game.god not in champList: champList.append(game.god)
    godString = listToString(champList, ", ")
    if len(champList) >= 13:
        return [[True, "Complete!"], [True, "Complete!"]]
    elif len(champList) >= 5:
        return [[True, "Complete!"], [False, godString]]
    else:
        return [[False, godString], [False, godString]]        
    
def _12_NaturesAlly1(gameCollection):
    # Enter the crypt
    for game in gameCollection.gameList:
        for i in game.notesList:
            if i[1] == "Crypt:1": return [True, "Complete!"]
    return [False, ""]

def _13_NaturesAlly2(gameCollection):
    # Collect the golden rune of Zot
    for game in gameCollection.gameList:
        if "golden" in game.runeList: return [True, "Complete!"]
    return [False, ""]

def _14_NaturesAlly3(gameCollection):
    # Enter Tomb for the first time after picking up the Orb of Zot and then get the Golden Rune
    for game in gameCollection.gameList:
        if "golden" in game.runeList:
            enterTombTurn = 0
            getOrbTurn = 0
            line = 0
            while (line < len(game.notesList)) and ((getOrbTurn == 0) or (enterTombTurn == 0)):
                if game.notesList[2] == "Entered Level 1 of the Tomb of the Ancients": enterTombTurn = game.notesList[line][0]
                elif game.notesList[2] == "Got the Orb of Zot": getOrbTurn = game.notesList[line][0]
                line += 1
            if (getOrbTurn < enterTombTurn) and (getOrbTurn != 0): return [True, "Complete!"]
    return [False, ""]

def listToString(listVar, delimiter):
    # Creates a string from a list using the delimiter as the separator.
    # Note, delimiter of "," produces a,b,c,d. while ", ", produces a, b, c, d
    retString = ""
    for i in listVar:
        retString += i + delimiter
    return retString[:-len(delimiter)]
    
def _15_GelatinousBody1(gameCollection):
    # Reach XL:9 with 5 different species and backgrounds
    spList = []
    bgList = []
    for game in gameCollection.gameList:
        if game.level >= 9:
            if game.species not in spList: spList.append(game.species)
            if game.background not in bgList: bgList.append(game.background)
            if (len(spList) >= 5) and (len(bgList) >= 5): return [True, "Complete!"]
    return [False, listToString(spList, ", ")+"\n"+listToString(bgList, ", ")]

def _16_GelatinousBody2(gameCollection):
    # Get a rune with at least 5 distinct species and backgrounds
    spList = []
    bgList = []
    for game in gameCollection.gameList:
        if game.numRunes > 0:
            if game.species not in spList: spList.append(game.species)
            if game.background not in bgList: bgList.append(game.background)
            if (len(spList) >= 5) and (len(bgList) >= 5): return [True, "Complete!"]
    return [False, listToString(spList, ", ")+"<br>"+listToString(bgList, ", ")]

def _17_GelatinousBody3(gameCollection):
    # Win with at least 5 distinct species and backgrounds
    spList = []
    bgList = []
    for game in gameCollection.gameList:
        if game.winFlag == True:
            if game.species not in spList: spList.append(game.species)
            if game.background not in bgList: bgList.append(game.background)
            if (len(spList) >= 5) and (len(bgList) >= 5): return [True, "Complete!"]
    return [False, listToString(spList, ", ")+"<br>"+listToString(bgList, ", ")]

def _18_LordOfDarkness1(gameCollection):
    # Enter the Vestibule of Hell without having entered the Lair
    for game in gameCollection.gameList:
        enterLairTurn = 0
        enterHellTurn = 0
        line = 0
        while (line < len(game.notesList)) and ((enterLairTurn == 0) or (enterHellTurn == 0)):
            if game.notesList[2] == "Entered Level 1 of the Lair of Beasts": enterLairTurn = game.notesList[line][0]
            elif game.notesList[2] == "Entered the Vestibule of Hell": enterHellTurn = game.notesList[line][0]
            line += 1
        if (enterHellTurn < enterLairTurn) and (enterHellTurn != 0): return [True, "Complete!"]
    return [False, ""]

def _19_LordOfDarkness2(gameCollection):
    # Win a game without having entered the Lair
    for game in gameCollection.gameList:
        if game.winFlag == True:
            # In case the entrance to Lair was never found.
            if "Lair" not in game.branchesDict: return [True, "Complete"]
            else:
                if game.branchesDict["Lair"][0] == 0: return [True, "Complete"]
    return [False, ""]

def _20_LordOfDarkness3(gameCollection):
    # Win a game without having entered the Temple, Orcish Mines, Lair, or Vaults
    falseString = ""
    bestRun = 19
    for game in gameCollection.gameList:
        temple = 1
        orc = 4
        lair = 8
        vaults = 5
                
        if game.winFlag == True:
            if "Temple" not in game.branchesDict: temple = 0
            else: temple = game.branchesDict["Temple"][0]
            if "Orc" not in game.branchesDict: orc = 0
            else: orc = game.branchesDict["Orc"][0]
            if "Lair" not in game.branchesDict: lair = 0
            else: lair = game.branchesDict["Lair"][0]
            if "Vaults" not in game.branchesDict: vaults = 0
            else: vaults = game.branchesDict["Vaults"][0]
            if (temple + orc + lair + vaults) == 0: return [True, "Complete!"]
            elif (temple + orc + lair + vaults) < bestRun:
                falseList = []
                if temple == 0: falseList.append("Temple")
                if orc == 0: falseList.append("Orc")
                if lair == 0: falseList.append("Lair")
                if vaults == 0: falseList.append("Vaults")
                falseString = listToString(falseList, ", ")
                bestRun = temple + orc + lair + vaults
        return [False, falseString]
                
            
            
    