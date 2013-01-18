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

class gameInfo:

    ## Keeping the below several lines just in case...
    #### Declaration of variables
 
    ## Game segment information

    ## version (string)
    # infomation found in the header
    # examples: 0.10, 0.11, 0.12a
    # will need to truncate from full version information
    # in two formats: versionLong and versionShort
    # versionLong contains the full version information
    # versionShort keeps it at the first 6 characters


    rawData = []
    header = []
    hiscore = []
    stats = []
    misc = []
    notes = []
    inventory = []
    turns_by_place = []
    skills = []
    spells = []
    overview = []
    mutations = []
    monlist = []

    ### Hiscore variables
    ## score (int)
    ## name
    ## title
    ## species (str)
    #
    species = ""

    ## speciesAbbrev
    # 
    speciesAbb = ""

  
    def __init__(self, data):
        self.rawData = data

    ## This function extracts the data from the data element fields.
    ## It will populate data only if the data element field is not empty.
        
    def extractData(self):

        if len(self.header) != 0: self.extractHeader()
        if len(self.hiscore) != 0: self.extractHiscore()
        

    ## header information stored in the following format
    ##  Dungeon Crawl Stone Soup version 0.12-a0-1616-ge3ef79a (tiles) character file.
    def extractHeader(self):
        self.versionLong = self.header[0].split()[5]
        self.versionShort = self.versionLong[0:6]
        # Note: future add - webtile/tile/console version can also be extracted

    ## hiscore information stored in the following format
    ## 51752 Ray the Unseen (level 14, -2/92 HPs)
    ##         Began as a Kobold Berserker on Jan 16, 2013.
    ##         Was the Champion of Trog.
    ##         Killed by divine providence
    ##         ... invoked by an orc priest
    ##          (14 damage)
    ##         ... on Level 1 of the Orcish Mines on Jan 17, 2013.
    ##         The game lasted 01:28:44 (24313 turns).
    def extractHiscore(self):
        self.score = self.hiscore[0].split()[0]

        # name may have spaces in it. need to search until 'the' is found
        lineIndex = 0
        wordIndex = 1
        lineSplit = self.hiscore[lineIndex].split()
        self.name = lineSplit[wordIndex]
        wordIndex += 1
        while lineSplit[wordIndex] != "the":
            self.name += " " + lineSplit[wordIndex]
            lineIndex += 1

        wordIndex += 1
        self.title = lineSplit[wordIndex]
        wordIndex += 1
        while lineSplit[wordIndex] != "(level":
            self.title += " " + lineSplit[wordIndex]
            wordIndex += 1

        lineIndex = 1
        lineSplit = self.hiscore[lineIndex].split()
        wordIndex = 3
        self.species += lineSplit[wordIndex]
        ### todo, some species have two words in their names, need to add
        ## if statements to account for this fact.

        
