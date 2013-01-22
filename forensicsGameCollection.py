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

class gameCollection:

    def __init__(self):
        self.gameList = []
        self.gameID = []

    def addGame(self, gameInfoObject):
        # First, check if this game exists in the database.
        # Currently, no way to uniquely identify a game record.
        # One idea uses the default naming convention of the record, but
        # will this always be the case?

        # Assumes that the game record is unique:...
        self.gameList.append(gameInfoObject)

    def addFile(self, filename):
        # Reads the file and adds the game to the gameList.
        
        game = forensicsParser.readGameRecord(filename)
        if game.id not in self.gameID:
            self.gameList.append(game)
            self.gameID.append(game.id)
        

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

            

    


        
