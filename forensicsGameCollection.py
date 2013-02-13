#   Dungeon Crawl Stone Soup Forensics
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

## This class is the gameCollection object
## This object stores all the read morgue files from the readGameRecord function
## of the parser file and stores the returned gameInfo object as a collection
## or list of game records. This object will then perform various statistics
## and return a string, file, or other formatted output based upon the
## collection of games within the collection.

## Of particular note, we will write this object so that it saves the game info
## such that game records will not need to be read each time. May not be
## necessary since reading ~ 300 game files still takes under a second. But
## allows the morgue directory to be cleaned up.

## Note, that this will only capture the snapshot of gameInfo at the time the
## morgue files are read, so this is NOT a failsafe substitute for the morgue
## files themselves.

import forensicsParser
import forensicsAchievement
import forensicsConfig
import forensicsDictionary

class gameCollection:

    def __init__(self):
        self.gameList = []
        self.gameID = []
        self.achievementList = [False]*3

    def addGame(self, gameInfoObject):
        # Check if this game exists in the database, if not, add it.
        # Don't believe this is currently used, so please use w/ caution. Will not be updating...
        if gameInfoObject.id not in self.gameID:
            self.gameList.append(gameInfoObject)
            self.gameID.append(gameInfoObject.id)
        self.updateAchievements()
        self.gameList.sort(key = lambda x: x.datetime)

    def addFile(self, filename):
        # Reads the file and adds the game to the gameList.
        game = forensicsParser.readGameRecord(filename)
        if game != None:
            if game.id not in self.gameID:
                self.gameList.append(game)
                self.gameID.append(game.id)
                if forensicsConfig.verbosity >= 3: print (filename, + " appended")
        self.updateAchievements()
        self.gameList.sort(key = lambda x: x.datetime)

    def outputCSVFile(self, OUTFILE):
        # Saves a CSV file with the name OUTFILE in the standard directory
        outputFormat = []
        listHeaders = ["ID", "Name", "Version", "Score", "Title", "Level", "Species", "Background",
                       "SP", "BG", "God", "WinFlag", "realTime", "turnsTaken", "numRunes",
                       "DLevel", "DLocation", "DPlace"]
        csvLine = ""
        for i in listHeaders:
            csvLine += str(i) + ","
        outputFormat.append(csvLine[:-1]+"\n")
        
        for game in self.gameList:
            csvLine = ""
            gameRecord = game.outputList()
            for i in gameRecord:
                csvLine += str(i) + ","
            outputFormat.append(csvLine[:-1]+"\n")

        f = open(OUTFILE, "w")
        for i in range(0, len(outputFormat)):
            f.write(outputFormat[i])
        f.close()

        print("Successfully completed.")
        print(str(len(self.gameList)) + " records exported to " + OUTFILE)
            
    def topNScores(self, n):
        # Returns a list of the top N scoring games.
        scoreSortedGameList = sorted(self.gameList, key = lambda x: x.score, reverse = True)
        return scoreSortedGameList[0:n]

    def updateAchievements(self):
        # runs the achievement module
        forensicsAchievement.forensicsAchievement(self)

    def completedAchievements(self):
        # Prints out the list of completed achievements
        print ("Completed Achievements:")
        for i in range(0, len(self.achievementList)):
            if self.achievementList[i] == True:
                print ("  " + forensicsDictionary.dAchievementList[i][1] +
                       " : " + forensicsDictionary.dAchievementList[i][2])
        
    def comboMaxLevel(self):
        # Returns a table with the max level of each species/background combo.
        statTable = self.blankStatTable()
        for game in self.gameList:
            spIndex = forensicsDictionary.dSpeciesTableIndex[game.species]+1
            bgIndex = forensicsDictionary.dBackgroundTableIndex[game.background]+1
            if game.level > statTable[spIndex][bgIndex]:
                statTable[spIndex][bgIndex] = game.level

        for i in range(1, len(statTable)-2):
            maxVal = 0
            for j in range(1, len(statTable[i])-2):
                if statTable[i][j] > maxVal: maxVal = statTable[i][j]
            statTable[i][-2] = maxVal

        for j in range(1, len(statTable[0])-2):
            maxVal = 0
            for i in range(1, len(statTable)-2):
                if statTable[i][j] > maxVal: maxVal = statTable[i][j]
            statTable[-2][j] = maxVal

        for i in range(1, len(statTable)-1):
            for j in range(1, len(statTable[0])-1):
                if statTable[i][j] == 0: statTable[i][j] = ""
            
        return statTable			                

    def comboGamesWon(self):
        # Returns a table with the games won of each species/background combo.
        statTable = self.blankStatTable()
        for game in self.gameList:
            if game.winFlag == True:
                spIndex = forensicsDictionary.dSpeciesTableIndex[game.species]+1
                bgIndex = forensicsDictionary.dBackgroundTableIndex[game.background]+1
                statTable[spIndex][bgIndex] += 1

        for i in range(1, len(statTable)-2):
            sumVal = 0
            for j in range(1, len(statTable[i])-2):
                sumVal += statTable[i][j]
            statTable[i][-2] = sumVal

        for j in range(1, len(statTable[0])-2):
            sumVal = 0
            for i in range(1, len(statTable)-2):
                sumVal += statTable[i][j]
            statTable[-2][j] = sumVal

        for i in range(1, len(statTable)-1):
            for j in range(1, len(statTable[0])-1):
                if statTable[i][j] == 0: statTable[i][j] = ""
                
        return statTable                       

    def comboGamesPlayed(self):
        # Returns a table with the games played for each sp/bg combo
        statTable = self.blankStatTable()
        for game in self.gameList:
            spIndex = forensicsDictionary.dSpeciesTableIndex[game.species]+1
            bgIndex = forensicsDictionary.dBackgroundTableIndex[game.background]+1
            statTable[spIndex][bgIndex] += 1

        for i in range(1, len(statTable)-2):
            sumVal = 0
            for j in range(1, len(statTable[i])-2):
                sumVal += statTable[i][j]
            statTable[i][-2] = sumVal

        for j in range(1, len(statTable[0])-2):
            sumVal = 0
            for i in range(1, len(statTable)-2):
                sumVal += statTable[i][j]
            statTable[-2][j] = sumVal

        for i in range(1, len(statTable)-1):
            for j in range(1, len(statTable[0])-1):
                if statTable[i][j] == 0: statTable[i][j] = ""
                
        return statTable             
            
    def blankStatTable(self):
        # Creates a blank statTable with headers
        headerRow = [""]
        headerRow.extend(forensicsDictionary.dBackgroundShortTableList)
        headerRow.extend([""])
        headerRow.extend([""])
        statTable = []
        statTable.append(headerRow)
        for i in range(0, len(forensicsDictionary.dSpeciesShortTableList)):
            dummyList = [0]*(len(forensicsDictionary.dBackgroundShortTableList)+1)
            dummyList[0] = forensicsDictionary.dSpeciesShortTableList[i]
            dummyList.extend([0])
            dummyList.extend([forensicsDictionary.dSpeciesShortTableList[i]])
            statTable.append(dummyList)

        totalRow = [""]
        totalRow.extend([0]*len(forensicsDictionary.dBackgroundShortTableList))
        totalRow.extend([""])
        totalRow.extend([""])
        statTable.append(totalRow)
        statTable.append(headerRow)
        return statTable

    def overallStatsList(self):
        # returns a list of stats in the following order:
        # [0] Total Score, [1] # Games, [2] # Wins, [3] % Win, [4] Best XL,
        # [5] Best Score, [6] Avg Score,
        # [7] Favorite Species, [8] Favorite Background, [9] Favorite Combo

        from collections import Counter

        statList = [0, 0, 0, "", 0, 0, 0, "", "", ""]
        spList = []
        bgList = []
        comboList = []
            
        for game in self.gameList:
            statList[0] += game.score
            statList[1] += 1
            statList[2] += (1 if game.winFlag == True else 0)
            if statList[4] != 27:
                statList[4] = max(statList[4], game.levelLong)
            statList[5] = max(statList[5], game.score)
            spList.append(game.species)
            bgList.append(game.background)
            comboList.append(game.species + " " + game.background)

        statList[3] = str(round(statList[2]/statList[1]*100, 2))+"%"
        statList[6] = "{:,}".format(int(round(statList[0]/statList[1], 0)))
        statList[0] = "{:,}".format(statList[0])
        statList[1] = "{:,}".format(statList[1])
        statList[2] = "{:,}".format(statList[2])
        statList[5] = "{:,}".format(statList[5])

        # Find the most common species/bg/combo
        speciesCounter = Counter(spList)
        spTuple = speciesCounter.most_common()
        maxSpeciesCount = spTuple[0][1]
        i = 0
        while spTuple[i][1] == maxSpeciesCount:
            if len(statList[7]) > 0: statList[7] += ", "
            statList[7] += spTuple[i][0]
            i += 1

        backgroundCounter = Counter(bgList)
        bgTuple = backgroundCounter.most_common()
        maxBackgroundCount = bgTuple[0][1]
        i = 0
        while bgTuple[i][1] == maxBackgroundCount:
            if len(statList[8]) > 0: statList[8] += ", "
            statList[8] += bgTuple[i][0]
            i += 1
        
        comboCounter = Counter(comboList)
        comboTuple = comboCounter.most_common()
        maxComboCount = comboTuple[0][1]
        i = 0
        while comboTuple[i][1] == maxComboCount:
            if len(statList[9]) > 0: statList[9] += ", "
            statList[9] += comboTuple[i][0]
            i += 1

        return statList
        
    def allGamesWonList(self):
        # Returns a list of gameInfo objects which have a winFlag of True
        # Will sort the list (oldest game with index 0) based on the date/time
        gameWinList = []
        for game in self.gameList:
            if game.winFlag == True: gameWinList.append(game)
        gameWinList.sort(key = lambda x: x.datetime)
        return gameWinList
            
    def recentNGames(self, n):
        # Returns a list of the most recent N games.
        scoreSortedGameList = sorted(self.gameList, key = lambda x: x.datetime, reverse = True)
        return scoreSortedGameList[0:n]            
            
        
        


                    
                    

            
