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



## this function reads the game record and returns a gameinfo object with
## the data fields populated. In theory, this part can be restructured such
## that the gameinfo object data is populated within the gameinfo class.
## For now, I'll keep this part separate.

import forensicsGameInfo
import forensicsConfig
import logging

def readGameRecord(filePath):

    # open/read in the morgue files
    f = open(filePath)
    rawData = f.readlines()
    f.close()

    # Create a gameInfo object
    try:
        gameInfoObject = forensicsGameInfo.gameInfo(rawData)
        gameInfoObject.filename = filePath
        parseGameInfoObject(gameInfoObject)
        return gameInfoObject
    except:
        print("Could not read file: " + filePath + " correctly. Skipping.")
        logging.info("Could not read file: " + filePath + " correctly. Skipping.")
        return None



def parseGameInfoObject(gameInfoObject):

    rawData = gameInfoObject.rawData

    # list declaration. 
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
    kills_by_place = []
    kills = []
            
    lineNum = 0
    while lineNum < len(rawData):
        # read each line to try to identify each section
        sectionID = "blank"
        if rawData[lineNum] != "\n":
            sectionID = sectionParser(rawData[lineNum])
        # Check if no line
        if ((sectionID == "unknown") or (sectionID == "blank")): lineNum += 1
        # Check if header
        elif sectionID == "header":
            headerStart = lineNum
            lineNum += 1
            headerEnd = lineNum
            header = rawData[headerStart:headerEnd]
        # Check if hiscore
        elif sectionID == "hiscore":
            hiscoreStart = lineNum
            while rawData[lineNum] != "\n": lineNum += 1
            hiscoreEnd = lineNum
            hiscore = rawData[hiscoreStart:hiscoreEnd]
        # Check if stats
        elif sectionID == "stats":
            statsStart = lineNum
            breakCheck = 0
            while breakCheck != 4:
                lineNum += 1
                if rawData[lineNum] == "\n": breakCheck += 1
            statsEnd = lineNum
            stats = rawData[statsStart:statsEnd]
        # Check if misc
        elif sectionID == "misc":
            miscStart = lineNum
            # for misc, _sdump_visits is always printed, however,
            # _sdumps_gold is the last line, but may not always show.
            # need to find location info and then see if gold info exists.
            while rawData[lineNum].find("visited") == -1: lineNum += 1
            # Check to see if gold exists
            while rawData[lineNum] != "\n": lineNum += 1
            # 2 options, either we're at the next section or we're at the
            # gold section. Check which and proceed.
            lineNum += 1
            if rawData[lineNum].find("gold pieces") == -1:
                # No gold found
                lineNum -= 1                    
            else:
                # Gold found
                while rawData[lineNum] != "\n": lineNum += 1
            miscEnd = lineNum
            misc = rawData[miscStart:miscEnd]
        # Check if notes
        elif sectionID == "notes":
            notesStart = lineNum
            while (rawData[lineNum] != "\n") and (rawData[lineNum] != "             \n"): lineNum += 1
            notesEnd = lineNum
            notes = rawData[notesStart:notesEnd]
        # Check if inventory
        elif sectionID == "inventory":
            inventoryStart = lineNum
            if rawData[inventoryStart] == "You aren't carrying anything.\n":
                lineNum += 1
            else:
                lineNum += 2
                while rawData[lineNum] != "\n": lineNum += 1
            inventoryEnd = lineNum
            inventory = rawData[inventoryStart:inventoryEnd]
        # Check if turns_by_place
        elif sectionID == "turns_by_place":
            turns_by_placeStart = lineNum-1
            breakCount = 0
            while breakCount != 2:
                if rawData[lineNum] == "               +-------+-------+-------+-------+-------+----------------------\n":
                    breakCount += 1
                lineNum += 1
            turns_by_placeEnd = lineNum
            turns_by_place = rawData[turns_by_placeStart:turns_by_placeEnd]
        # Check if skills
        elif sectionID == "skills":
            skillsStart = lineNum
            while rawData[lineNum] != "\n": lineNum += 1
            skillsEnd = lineNum
            skills = rawData[skillsStart:skillsEnd]
        # Check if spells
        elif sectionID == "spells":
            spellsStart = lineNum
            while ((rawData[lineNum] != "You didn't know any spells.\n") and
                   (rawData[lineNum] != "You knew the following spells:\n")): lineNum += 1
            if rawData[lineNum] == "You didn't know any spells.\n":
                lineNum += 1
            else:
                lineNum += 2
                while rawData[lineNum] != "\n": lineNum += 1
            spellsEnd = lineNum
            spells = rawData[spellsStart:spellsEnd]
        # Check if overview
        elif sectionID == "overview":
            # Overview consists of 5 sections: Branches, Altars, Shops, Portals, and Annotations
            overviewStart = lineNum
            lineNum += 2
            while rawData[lineNum] in ["Branches:\n", "Altars:\n", "Shops:\n", "Portals:\n", "Annotations\n"]:
                while rawData[lineNum] != "\n": lineNum += 1
                lineNum += 1
            lineNum -= 1
            overviewEnd = lineNum
            overview = rawData[overviewStart:overviewEnd]
        # Check if mutations
        elif sectionID == "mutations":
            mutationsStart = lineNum
            lineNum += 2
            while rawData[lineNum] != "\n": lineNum += 1
            mutationsEnd = lineNum
            mutations = rawData[mutationsStart:mutationsEnd]
        # Check if monlist
        elif sectionID == "monlist":
            monlistStart = lineNum
            while rawData[lineNum] != "\n": lineNum += 1
            monlistEnd = lineNum
            monlist = rawData[monlistStart:monlistEnd]
        # Check if kills_by_place
        elif sectionID == "kills_by_place":
            kills_by_placeStart = lineNum-1
            breakCount = 0
            while breakCount != 2:
                if rawData[lineNum] == "               +-------+-------+-------+-------+-------+----------------------\n":
                    breakCount += 1
                lineNum += 1
            kills_by_placeEnd = lineNum
            kills_by_place = rawData[kills_by_placeStart:kills_by_placeEnd]
        # Check if kills
        elif sectionID == "kills":
            killsStart = lineNum
            try:
                while rawData[lineNum].find("Grand Total:") == -1: lineNum += 1
            except:
                try:
                    lineNum = killsStart
                    while rawData[lineNum].find("Monster Nature") == -1: lineNum += 1
                    lineNum -= 2
                except:
                    lineNum = killsStart
                    while rawData[lineNum].find("vanquished.") == -1: lineNum += 1                    
            lineNum += 1
            killsEnd = lineNum
            kills = rawData[killsStart:killsEnd]
        # Check if action_counts
        else:
            # Should never trigger if all components are active
            lineNum += 1
        
    # Now that each section has been separated, need to call the functions
    # in order to create the gameInfo object that stores each game's information.

    gameInfoObject.header = header
    gameInfoObject.hiscore = hiscore
    gameInfoObject.stats = stats
    gameInfoObject.misc = misc
    gameInfoObject.notes = notes
    gameInfoObject.inventory = inventory
    gameInfoObject.turns_by_place = turns_by_place
    gameInfoObject.skills = skills
    gameInfoObject.spells = spells
    gameInfoObject.overview = overview
    gameInfoObject.mutations = mutations
    gameInfoObject.monlist = monlist
    gameInfoObject.kills_by_place = kills_by_place
    gameInfoObject.kills = kills

    gameInfoObject.extractData()
                    
                    
## This function is utilized by the readGameRecord function
## parameter is a single line of raw data
## returns a section heading if line is the first line of that section

def sectionParser(line):

    sectionType = "unknown"  # stays unknown unless identified

    # Check if header
    if line.find("character file.") != -1:
        sectionType = "header"
    # Check if hiscore
    # Future notes: hiscore.cc - hiscore_line
    elif line.find("(level") != -1:
        sectionType = "hiscore"
    # Check if stats
    # Source notes: output.cc - dump_overview_screen
    elif line.find("Time:") != -1:
        sectionType = "stats"
    # Check if misc
    # Source notes: lots of info here, using the location dump to identify
    # the beginning of this dump header. code below found in place.cc
    elif ((line == "You escaped.\n") or (line.find("You were on") == 0)
          or (line.find("You were in") == 0)):
        sectionType = "misc"
    # Check if notes
    elif line == "Notes\n":
        sectionType = "notes"
    # Check if inventory
    elif (line == "Inventory:\n") or (line == "You aren't carrying anything.\n"):
        sectionType = "inventory"
    # Check if turns_by_place
    elif line.find("A = Turns spent") != -1:
        sectionType = "turns_by_place"
    # Check if skills
    elif line == "   Skills:\n":
        sectionType = "skills"
    # Check if spells
    elif ((line == "You had one spell level left.\n") or
          (line == "You couldn't memorise any spells.\n") or
          (line.find("spell levels left.") != -1)):
        sectionType = "spells"
    # Check if overview
    # Source notes: dgn-overview.cc - overview_description_string
    elif line == "Dungeon Overview and Level Annotations\n":
        sectionType = "overview"
    # Check if mutations
    # Source notes: mutation.cc - describe_mutations
    elif line == "Innate Abilities, Weirdness & Mutations\n":
        sectionType = "mutations"
    # Check if messages
    elif line == "Message History\n":
        sectionType = "messages"
    # Check if screenshot
    # Source notes: view.cc - screenshot
    # NO clue how to parse this section...
    #
    # Check if monlist
    # Source notes: output.cc - mpr_monster_list
    elif ((line == "There were no monsters in sight!\n") or
          (line.find("You could see") != -1)):
        sectionType = "monlist"
    # Check if kills_by_place
    elif line.find("A = Kills in") != -1:
        sectionType = "kills_by_place"
    # Check if kills
    # Source notes: kills.cc - kill_info
    elif line == "Vanquished Creatures\n":
        sectionType = "kills"
    # Check if action_counts
    elif line.find("Action") == 0:
        sectionType = "action_counts"

    if forensicsConfig.verbosity >= 5:
        print ("line = " + line)
        print ("sectionType = " + sectionType)

    return sectionType

        
        
    
