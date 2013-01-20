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

import dictionary

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
    ## subspecies (str) (used only for Draconians)
    ## speciesShort (str)
    ## background
    ## backgroundShort
    ## god
    ## winFlag

    ### stats variables
    ## turnsTaken (int)
    ## timeTakenLong (str)
    ## level (int)
    ## levelLong (float)
    ## numRunes (int)
    

  
    def __init__(self, data):
        self.rawData = data

    ## This function extracts the data from the data element fields.
    ## It will populate data only if the data element field is not empty.
        
    def extractData(self):

        if len(self.header) != 0: self.extractHeader()
        if len(self.hiscore) != 0: self.extractHiscore()
        if len(self.stats) != 0: self.extractStats()
        

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
        self.score = int(self.hiscore[0].split()[0])

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

        # Extract species information
        lineIndex = 1
        lineSplit = self.hiscore[lineIndex].split()
        wordIndex = 3
        self.species = lineSplit[wordIndex]
        wordIndex += 1
        if lineSplit[wordIndex] == "Draconian":
            self.species = "Draconian"
            self.subspecies = lineSplit[wordIndex - 1]
            wordIndex += 1
        elif lineSplit[wordIndex] in ["Elf", "Dwarf", "Orc"]:
            self.species += " " + lineSplit[wordIndex]
            wordIndex += 1
        self.speciesShort = dictionary.dSpecies[self.species]

        # Extract background information
        self.background = lineSplit[wordIndex]
        if lineSplit[wordIndex+1] != "on":
            self.background += " " + lineSplit[wordIndex+1]
        self.backgroundShort = dictionary.dBackground[self.background]

        # Extract god information
        lineIndex += 1
        lineSplit = self.hiscore[lineIndex].split()
        wordIndex = 0
        if lineSplit[wordIndex] != "Was": self.god = ""
        else:
            self.god = self.hiscore[lineIndex][self.hiscore[lineIndex].find("of")+3:-2]
            lineIndex += 1  # Note, line increment done here in case no god exists
            

        # End information can be extracted in this next section
        # This is a future todo after reviewing source to determine exact format
        # in which the end data is displayed.
        # For now, will use this section to set the winFlag
        wordIndex = 0
        if self.hiscore[lineIndex].split()[0] == "Escaped": self.winFlag = True
        else: self.winFlag = False

    ## stats extraction information

    def extractStats(self):
        
        ## Line 0:
        ## Ray the Unseen (Kobold Berserker)                  Turns: 24313, Time: 01:28:45
        lineSplit = self.stats[0].split()
        wordSplit = 0
        self.turnsTaken = int(lineSplit[lineSplit.index("Turns:")+1][:-1])
        self.timeTakenLong = lineSplit[-1]
        
        ## Line 2:
        ## HP  -2/92        AC 16     Str 17      XL: 14   Next: 90%
        lineSplit = self.stats[2].split()
        self.level = int(lineSplit[-3])
        self.levelLong = int(lineSplit[-1][:-1])/100 + self.level

        '''
MP  27/27        EV 25     Int  8      God: Trog [******]
Gold 1668        SH 16     Dex 21      Spells:  0 memorised, 14 levels left

Res.Fire  : + . .   See Invis. : +   D - +7 quick blade {god gift}
Res.Cold  : . . .   Warding    : .   F - +3 leather armour of the Wild Haggis {rEle
Life Prot.: . . .   Conserve   : .   N - +0 buckler
Res.Poison: +       Res.Corr.  : .   (no helmet)
Res.Elec. : +       Clarity    : .   u - +1 cloak {MR}
Sust.Abil.: . .     Spirit.Shd : .   S - +0 pair of gauntlets
Res.Mut.  : .       Stasis     : .   t - +2 pair of boots of Texzo {Str-1 Acc+2 Stl
Res.Rott. : .       Ctrl.Telep.: .   V - amulet "Laeto" {Faith Contam Dex+2 SInv, u
Saprovore : + + .   Flight     : .   l - +2 ring of protection
                                     b - ring of regeneration

@: regenerating, exhausted, studying Armour, very slightly contaminated, slowed,
very slow, incredibly resistant to hostile enchantments, incredibly stealthy
A: disease resistance, carnivore 3, poison resistance, saprovore 2, AC +2, Dex
+2
a: Burn Spellbooks, Berserk, Trog's Hand, Brothers in Arms, Renounce Religion
}: 2/15 runes: barnacled, gossamer
        '''

        ## extracting rune information if it exists.
        lineIndex = 3
        self.numRunes = 0
        while (lineIndex < len(self.stats)) and (self.numRunes == 0):
            if len(self.stats[lineIndex]) < 2: lineIndex += 1
            else:
                if self.stats[lineIndex].split()[0] == "}:":
                    loop = False
                    runeString = self.stats[lineIndex].split()[1]
                    self.numRunes = int(runeString[:runeString.find("/")])
                lineIndex += 1

        
        
        
