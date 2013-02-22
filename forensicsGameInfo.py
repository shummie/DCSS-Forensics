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

import forensicsDictionary
import datetime

class gameInfo:

    ## Keeping the below several lines just in case...
    #### Declaration of variables
 
    ## Game segment information

    ## version (string)
    # infomation found in the header
    # examples: 0.10, 0.11, 0.12a0
    # will need to truncate from full version information
    # in two formats: versionLong and versionShort
    # versionLong contains the full version information
    # versionShort keeps it at the first 7 characters


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

    ## Filename is used to extract the date/time info, assuming the standard
    ## naming convention is used.
    filename = ""

    ## ID variables
    ## date (str)
    ## time (str)
    ## id (str)
    ## datetime (datetime object)

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
    ## runeList (list of str)
    ## pietyLevel (int)

    ### misc variables
    ## dungeonLevel (int)
    ## dungeonLocation (str)
    ## dungeonPlace (str)
    ## branchesVisited (int)
    ## levelsVisited (int)
    ## panVisits (int)
    ## panLevelVisits (int)
    ## abyssVisits (int)
    ## bazaarVisits (int)
    ## zigVisits (int)
    ## zigLevelVisits (int)
    ## zigCompleted (int)
    ## zigDeepest (int)
    ## goldCollected (int)
    ## goldSpent (int)
    ## goldDonated (int)
    ## goldMisc (int)
    
    ### kills variables
    ## numCreaturesVanquished (int)
    
    ### notes variables
    ## notesList (list [Turn, Location, Note])

  
    def __init__(self, data):
        self.rawData = data
        
        ## Initialization of variables
        
        ## Misc Var
        self.levelsVisited = 0
        self.branchesVisited = 0
        self.panVisits = 0
        self.panLevelVisits = 0
        self.abyssVisits = 0
        self.bazaarVisits = 0
        self.zigCompleted = 0
        self.zigDeepest = 0
        self.zigLevelVisits = 0
        self.zigVisits = 0
        self.goldCollected = 0
        self.goldSpent = 0
        self.goldDonted = 0
        self.goldMisc = 0

        ## Kills var        
        self.numCreaturesVanquished = 0
        
        ## stats var
        self.turnsTaken = 0
        self.pietyLevel = 0
        self.numRunes = 0
        self.runeList = []
        self.level = 0
        
        ## notes var
        self.notesList = []
        

    ## This function extracts the data from the data element fields.
    ## It will populate data only if the data element field is not empty.
        
    def extractData(self):
        
        if self.filename != "": self.extractID()
        if len(self.header) != 0: self.extractHeader()
        if len(self.hiscore) != 0: self.extractHiscore()
        if len(self.stats) != 0: self.extractStats()
        if len(self.misc) != 0: self.extractMisc()
        if len(self.kills) != 0: self.extractKills()
        if len(self.notes) != 0: self.extractNotes()

    def extractID(self):
        # morgue-Ray-20130122-083257.txt
        datetimeList = self.filename.split("-")
        if len(datetimeList) == 4:        
            self.date = datetimeList[2]
            self.time = datetimeList[3][:-4]
            self.id = self.date + self.time
            self.datetime = datetime.datetime(int(self.date[:4]), int(self.date[4:6]), int(self.date[6:]), int(self.time[:2]), int(self.time[2:4]), int(self.time[4:]))

        else:
            self.date = ""
            self.time = ""
            # Still import, but establish a unique time identifier
            self.id = datetime.datetime.now().isoformat(' ')
            self.datetime = datetime.datetime.now()

    ## header information stored in the following format
    ##  Dungeon Crawl Stone Soup version 0.12-a0-1616-ge3ef79a (tiles) character file.
    def extractHeader(self):
        self.versionLong = self.header[0].split()[5]
        self.versionShort = self.versionLong[0:7]
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
        self.speciesShort = forensicsDictionary.dSpecies[self.species]

        # Extract background information
        self.background = lineSplit[wordIndex]
        if lineSplit[wordIndex+1] != "on":
            self.background += " " + lineSplit[wordIndex+1]
        self.backgroundShort = forensicsDictionary.dBackground[self.background]

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
        self.end = ""

        # The below is probably VERY SLOW. Need to find a better way to
        # optimize this.
        while ((len(self.hiscore[lineIndex].strip()) != 0) and
               (self.hiscore[lineIndex].find("... on ") == -1) and
               (self.hiscore[lineIndex].find("... in ") == -1) and
               (self.hiscore[lineIndex].find("The game lasted") == -1)):
        
            self.end += self.hiscore[lineIndex].strip()
            # Keeping the below debug line for now... should probably convert
            # to a verbosity trigger...
            # print (self.hiscore[lineIndex])
            lineIndex += 1
        self.end = self.end.replace("...", "")
        if self.end[self.end.find("(")-1] != " ": self.end = self.end.replace("(", " (")

        ## Collect all end information and place in one line. The formatting for this
        ## varies quite a bit depending on how the player died/quit.
        
        if self.end.split()[0] == "Escaped":
            self.winFlag = True
            # I originally put the below so that when you win, it just shows:
            # Escaped w/ the rune and X orbs! (removing the date at the end)
            # Instead, I'll keep it and have the date removed if needed
            # at another section.
            # self.end = self.end[0:self.end.find("runes")+5] + "!"
        else: self.winFlag = False

    ## stats extraction information

    def extractStats(self):
        
        ## Line 0:
        ## Ray the Unseen (Kobold Berserker)                  Turns: 24313, Time: 01:28:45
        lineSplit = self.stats[0].split()
        self.turnsTaken = int(lineSplit[lineSplit.index("Turns:")+1][:-1])
        self.timeTakenLong = lineSplit[-1]
        
        ## Line 2:
        ## HP  -2/92        AC 16     Str 17      XL: 14   Next: 90%
        ## HP 224/224 (225) AC 55     Str 16      XL: 27
        lineSplit = self.stats[2].split()
        if self.stats[2][-2] == "%":            
            self.level = int(lineSplit[-3])
            self.levelLong = int(lineSplit[-1][:-1])/100 + self.level
        else:
            self.level = int(lineSplit[-1])
            self.levelLong = self.level + 0.0
            


        
        ## Line 3:
        ## MP  27/27        EV 25     Int  8      God: Trog [******]
        ## MP   0/0         EV 10     Int  4      God: 
        lineIndex = 3
        self.pietyLevel = self.stats[lineIndex].split()[-1].count("*")
        
        '''

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

        '''        
        
        ## Future change? Can rewrite this section to parse the runeList info and just have numRunes = len(runeList)
        ## also, can just read to the end of the section instead of assuming it is only 2 lines long at max.
        ## extracting rune information if it exists.       
        
        ## }: 2/15 runes: barnacled, gossamer
        ## }: 15/15 runes: decaying, serpentine, slimy, silver, golden, iron, obsidian,
        ## icy, bone, abyssal, demonic, glowing, magical, fiery, dark
        
        self.numRunes = 0
        while (lineIndex < len(self.stats)) and (self.numRunes == 0):
            if len(self.stats[lineIndex]) < 2: lineIndex += 1
            else:
                if self.stats[lineIndex].split()[0] == "}:":
                    runeString = self.stats[lineIndex]
                    numRuneString = self.stats[lineIndex].split()[1]
                    self.numRunes = int(numRuneString[:numRuneString.find("/")])
                lineIndex += 1
                
        ## extracting runes collected
        if self.numRunes > 0: 
            if lineIndex < len(self.stats):
                runeString += self.stats[lineIndex]
            
            # Rune string shouldn't exceed 2 lines... I think?
            runeString = runeString.replace(",", " ")
            self.runeList = runeString.split()[3:]
            
    ## extract misc information
                
    def extractMisc(self):

        ## Line 0: You were on level 1 of the Orcish Mines.
        lineIndex = 0
        lineSplit = self.misc[lineIndex].split()
        if lineSplit[1] == "escaped.":
            self.dungeonLevel = 0
            if self.winFlag == True: self.dungeonLocation = "Won"
            else: self.dungeonLocation = "Dungeon" # Occurs when exit w/o Orb
        elif lineSplit[-1] == "Abyss.":
            self.dungeonLevel = 0
            self.dungeonLocation = "Abyss"
        elif lineSplit[-1] == "Blades.":
            self.dungeonLevel = 0
            self.dungeonLocation = "Blades"
        elif lineSplit[-1] == "Cocytus.":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = "Cocytus"
        elif lineSplit[-1] == "Gehenna.":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = "Gehenna"
        elif lineSplit[-1] == "Tartarus.":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = "Tartarus"
        # I don't have a morgue file with Dis yet...
        elif lineSplit[-1] == "Dis.":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = "Dis"
        # Do we need to add exceptions for Hell & Pandemonium?
        elif lineSplit[-1] == "ziggurat.":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = "Ziggurat"
        elif lineSplit[2] == "on":
            self.dungeonLevel = int(lineSplit[lineSplit.index("level")+1])
            self.dungeonLocation = self.misc[lineIndex][self.misc[lineIndex].find("the")+4:-2]
        elif lineSplit[2] == "in":
            self.dungeonLevel = 0
            self.dungeonLocation = self.misc[lineIndex][self.misc[lineIndex].find("a"):-2]
        else:
            self.dungeonLevel = -1
            self.dungeonLocation = "ERROR"
        if self.dungeonLevel == 0: self.dungeonPlace = self.dungeonLocation
        else: self.dungeonPlace = self.dungeonLocation + ":" + str(self.dungeonLevel)
            
        '''
You worshipped Trog.
Trog was exalted by your worship.
You were very full.
        '''
        # You visited 3 branches of the dungeon, and saw 23 of its levels.
        while self.misc[lineIndex].find("You visited") == -1: lineIndex += 1
            # Note, this still assumes dead characters. 
        self.branchesVisited = int(self.misc[lineIndex].split()[2])
        self.levelsVisited = int(self.misc[lineIndex].split()[-4])
        if lineIndex < (len(self.misc) - 1) : lineIndex += 1
        
        ## You visited Pandemonium 2 times, and saw 27 of its levels.
        if self.misc[lineIndex].find("Pandemonium") != -1:
            self.panVisits = int(self.misc[lineIndex].split()[3])
            self.panLevelVisits = int(self.misc[lineIndex].split()[7])
            if lineIndex < (len(self.misc) - 1) : lineIndex += 1
            
        ## You visited the Abyss 1 time.
        if self.misc[lineIndex].find("Abyss") != -1:
            self.abyssVisits = int(self.misc[lineIndex].split()[4])
            if lineIndex < (len(self.misc) - 1) : lineIndex += 1
        
        ## You visited 1 bazaar.
        if self.misc[lineIndex].find("bazaar") != -1:
            self.bazaarVisits = int(self.misc[lineIndex].split()[2])
            if lineIndex < (len(self.misc) - 1) : lineIndex += 1
        
        ## You completed 1 Ziggurat, and saw 27 of its levels.
        ## You completed 2 Ziggurats, and saw 54 of their levels.
        ## You visited 1 Ziggurat, and saw 14 of its levels.
        ## You visited 2 Ziggurats, and saw 32 of its levels (deepest: 22).
        ## You visited 2 Ziggurats (completing 1), and saw 51 of their levels.
        if self.misc[lineIndex].find("Ziggurat") != -1:
            lineSplit = self.misc[lineIndex].split()
            self.zigVisits = int(lineSplit[2])
            if lineSplit[1] == "completed": self.zigCompleted = self.zigVisits
            elif lineSplit[4] == "(completing": self.zigCompleted = int(lineSplit[5][:-2])
            self.zigLevelVisits = int(lineSplit[lineSplit.index("saw")+1])
            if lineSplit[-2] == "(deepest:": self.zigDeepest = int(lineSplit[-1][:-2])
            elif self.zigCompleted > 0: self.zigDeepest = 27
            else: self.zigDeepest = self.zigLevelVisits
            if lineIndex < (len(self.misc) - 1) : lineIndex += 1
            
        ## You also visited: Labyrinth, Sewer, Ossuary, Bailey and Volcano.

        ## You collected 3205 gold pieces.
        ## You spent 493 gold pieces at shops.
        self.goldCollected = 0
        self.goldSpent = 0
        self.goldDonated = 0
        self.goldMisc = 0
        while (lineIndex < len(self.misc)) and (self.misc[lineIndex].find("You collected") == -1): lineIndex += 1      
        while lineIndex < len(self.misc):
            lineSplit = self.misc[lineIndex].split()
            if lineSplit[1] == "collected": self.goldCollected = int(self.misc[lineIndex].split()[2])
            elif lineSplit[1] == "spent": self.goldSpent = int(self.misc[lineIndex].split()[2])
            elif lineSplit[1] == "donated": self.goldDonated = int(self.misc[lineIndex].split()[2])
            elif lineSplit[1] == "used": self.goldMisc = int(self.misc[lineIndex].split()[2])
            lineIndex += 1
        
        
        #if lineIndex != len(self.misc) - 1:  
        #    lineIndex += 1
        #    self.goldSpent = int(self.misc[lineIndex].split()[2])
            
    def extractKills(self):
        if self.kills[-1].find("Grand Total:") != -1:
            self.numCreaturesVanquished = int(self.kills[-1].split()[2])
        else:
            self.numCreaturesVanquished = int(self.kills[-1].split()[0])
        
        
    def extractNotes(self):
        self.notesList = self.notes[3:]
        for i in range(len(self.notesList)):
            self.notesList[i] = self.notesList[i].split("|")
            for j in range(len(self.notesList[i])):
                self.notesList[i][j] = self.notesList[i][j].strip()
            self.notesList[i][0] = int(self.notesList[i][0])
            #self.notesList[i][2] = self.notesList[i][2].replace("\n", "") 
         
            
        
        
    # outputs select variables into a list, useful for debugging purposes.
    def outputList(self):
        # outList = []
        outList = [self.id, self.name, self.versionShort, self.score, self.title,
                   self.levelLong, self.species, self.background, self.speciesShort,
                   self.backgroundShort, self.god, self.winFlag, self.timeTakenLong,
                   self.turnsTaken, self.numRunes, self.dungeonLevel, self.dungeonLocation,
                   self.dungeonPlace]
        return outList
        
