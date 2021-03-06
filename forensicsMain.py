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

import forensicsGameCollection
import forensicsConfig
import forensicsHTML
import os
import glob
import pickle
import logging




# Note, for now, ALL data and functions utilize the main gameCollection object
# I can alter the below later to deal with multiple databases, but currently
# assumes a single database and will never need to worry about passing a
# gameCollection object as a parameter for any values.


# outputs the CSV file
def outputCSV():
    gameCollection.outputCSVFile(forensicsConfig.CSVOUTFILE)

# Loads the gameCollection object with the morgue files
def readGameData():
    for files in glob.glob("*.txt"):
    # files = morgue-Ray-20121211-213939.txt
        if forensicsConfig.verbosity >= 2:
            print(files)
        gameCollection.addFile(files)
    print("Updating achievements")
    logging.info("Updating achievements")
    gameCollection.updateAchievements()
    print("Achievements updated")
    logging.info("Achievements updated")

# Saves the gameCollection object into filename
def saveGameData(filename):
    output = open(filename, "wb")
    pickle.dump(gameCollection, output)
    output.close()

# returns the gameCollection object
def loadGameData(filename):
    inputfile = open(filename, "rb")
    return pickle.load(inputfile)

logging.basicConfig(filename='dcssforensics.log', filemode = 'w', level=logging.DEBUG)

#try:    
print("Attempting to read config.ini")
logging.info("Attemping to read config.ini")
forensicsConfig.readConfigFile("config.ini")
os.chdir(forensicsConfig.PATH)
gameCollection = forensicsGameCollection.gameCollection()
print("Attempting to read game data")   
logging.info("Attempting to read game data")
readGameData()
print("All game data read.")
logging.info("All game data read.")
forensicsHTML.createHTMLOverview(gameCollection)
print("overview.html created")
logging.info("overview.html created")
forensicsHTML.createHTMLALLScoresTable(gameCollection)
print("allGamesByScore.html created")
logging.info("allGamesByScore.html created")
forensicsHTML.createHTMLALLGamesTableRecent(gameCollection)
print("allGamesByRecent.html created")
logging.info("allGamesByRecent.html created")
forensicsHTML.createGameCollectionDump(gameCollection)
print("allGamesDump.html created")
logging.info("allGamesDump.html created")
forensicsHTML.createAchievementDetailed(gameCollection)
print("acheivementsDetailed.html created")
logging.info("acheivementsDetailed.html created")


#except WindowsError:
    #print("Directory " + forensicsConfig.PATH + " does not exist.")
#except:
    #print("An unknown error has occurred, program halted.")
