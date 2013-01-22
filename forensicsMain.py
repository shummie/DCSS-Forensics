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

import forensicsParser
import os
import glob

## Enter path below to main DCSS directory
PATH = "C:/Users/shumr/Documents/Ray/stone_soup-tiles-0.11"
OUTFILE = "test.csv"

os.chdir(PATH + "/morgue")

gameCollection = []

for files in glob.glob("*.txt"):
    gameCollection.append(forensicsParser.readGameRecord(files))

outputList = []
listHeaders = ["Name", "Version", "Score", "Title", "Level", "Species", "Background",
               "SP", "BG", "God", "WinFlag", "realTime", "turnsTaken", "numRunes",
               "DLevel", "DLocation", "DPlace"]
outputList.append(listHeaders)
for game in gameCollection: outputList.append(game.outputList())

outputFormat = []
for item in outputList:
    csvList = ""
    for a in item:
        csvList += str(a) + ","
    outputFormat.append(csvList[:-1]+"\n")

f = open(OUTFILE, "w")
for i in range(0, len(outputFormat)):
    f.write(outputFormat[i])
f.close()

print("Successfully completed.")
print(str(len(outputList)-1) + " records exported to \n" + PATH + "/morgue/" + OUTFILE)

    
