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
import forensicsParser
import os
import glob

## Enter path below to main DCSS directory
# PATH = "C:/Users/shumr/Documents/Ray/stone_soup-tiles-0.11"
PATH = "C:/Users/shumr/Documents/Ray/crawl_tiles-0.12-a0-1616"
OUTFILE = "test.csv"

os.chdir(PATH + "/morgue")

gameCollection = forensicsGameCollection.gameCollection()

# Note, for now, ALL data and functions utilize the main gameCollection object
# I can alter the below later to deal with multiple databases, but currently
# assumes a single database and will never need to worry about passing a
# gameCollection object as a parameter for any values.


# outputs the CSV file
def outputCSV():
    gameCollection.outputCSVFile(OUTFILE)

# Loads the gameCollection object with the morgue files
def loadGameData():
    for files in glob.glob("*.txt"):
    # files = morgue-Ray-20121211-213939.txt
    # DEBUG:: print(files)
        gameCollection.addFile(files)  

# Saves the gameCollection object into filename
def saveGameData(filename):
    output = open(filename, "wb")
    pickle.dump(gameCollection, output)
    output.close()

# returns the gameCollection object
def loadGameData(filename):
    inputfile = open(filename, "rb")
    return pickle.load(inputfile)

    
