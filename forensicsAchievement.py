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
    godString = ""
    for a in champList: godString += a + ", "
    godString = godString[:-2]
    if len(champList) >= 13:
        return [[True, "Complete!"], [True, "Complete!"]]
    elif len(champList) >= 5:
        return [[True, "Complete!"], [False, godString]]
    else:
        return [[False, godString], [False, godString]]        
    
    