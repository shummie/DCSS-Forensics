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
        if gameInfoObject.id not in self.gameID:
            self.gameList.append(gameInfoObject)
            self.gameID.append(gameInfoObject.id)
        self.updateAchievements()


    def addFile(self, filename):
        # Reads the file and adds the game to the gameList.
        game = forensicsParser.readGameRecord(filename)
        if game.id not in self.gameID:
            self.gameList.append(game)
            self.gameID.append(game.id)
            if forensicsConfig.verbosity >= 3: print (filename, + " appended")
        self.updateAchievements()

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

    # Prints out (or saves in a csv?) the top N scores in the gameCollection
    def topNScores(self, n):
        topScores = []
        topScoresIndex = []
        # Find the top N scoring games first...
        for i in range(0, len(self.gameList)):
            if len(topScores) < n:
                topScores.append(self.gameList[i].score)
                topScoresIndex.append(i)
            else:
                if self.gameList[i].score > min(topScores):
                    topScoresIndex.pop(topScores.index(min(topScores)))
                    topScores.pop(topScores.index(min(topScores)))
                    topScores.append(self.gameList[i].score)
                    topScoresIndex.append(i)

        if forensicsConfig.verbosity >= 2:
            print (topScores)
            print (topScoresIndex)

        # Next, sort the list
        topScoresIndexOrdered = []
        topScoresOrdered = []
        while len(topScores) > 0:
            index = topScores.index(max(topScores))
            topScoresOrdered.append(topScores[index])
            topScoresIndexOrdered.append(topScoresIndex[index])
            topScores.pop(index)
            topScoresIndex.pop(index)

        if forensicsConfig.verbosity >= 2:
            print (topScoresOrdered)
            print (topScoresIndexOrdered)

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
        statTable = []
        for i in range(0, len(forensicsDictionary.dBackgroundShortTableList)):
            dummyList = [0]*len(forensicsDictionary.dSpeciesShortTableList)
            statTable.append(dummyList)
        for game in self.gameList:
            spIndex = forensicsDictionary.dSpeciesTableIndex[game.species]
            bgIndex = forensicsDictionary.dBackgroundTableIndex[game.background]
            if game.level > statTable[spIndex][bgIndex]:
                statTable[spIndex][bgIndex] = game.level
        return statTable			                

    def comboGamesWon(self):
        # Returns a table with the games won of each species/background combo.
        statTable = []
        for i in range(0, len(forensicsDictionary.dBackgroundShortTableList)):
            dummyList = [0]*len(forensicsDictionary.dSpeciesShortTableList)
            statTable.append(dummyList)
        for game in self.gameList:
            if game.winFlag == True:
                spIndex = forensicsDictionary.dSpeciesTableIndex[game.species]
                bgIndex = forensicsDictionary.dBackgroundTableIndex[game.background]
                statTable[spIndex][bgIndex] += 1
        return statTable                       
                    
            
        
        
        


                    
                    

            
