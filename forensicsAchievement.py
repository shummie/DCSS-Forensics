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

    if gameCollection.achievementList[0] == False:
        gameCollection.achievementList[0] = _0_CheckAnyWin(gameCollection)
    if gameCollection.achievementList[1] == False:
        gameCollection.achievementList[1] = _1_CheckAnyLevel27(gameCollection)
    if gameCollection.achievementList[2] == False:
        gameCollection.achievementList[2] = _2_CheckAny15RuneWin(gameCollection)
    if gameCollection.achievementList[3] == False:
        gameCollection.achievementList[3] = _3_SlowAndSteady1(gameCollection)

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
        