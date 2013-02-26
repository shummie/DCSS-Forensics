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

### DICTIONARY FILE ###

### Species Mapping Dictionary ###

dSpecies = {
    "Human" : "Hu",
    "High Elf" : "HE",
    "Deep Elf" : "DE",
    "Sludge Elf" : "SE",
    "Deep Dwarf" : "DD",
    "Hill Orc" : "HO",
    "Merfolk" : "Mf",
    "Halfling" : "Ha",
    "Kobold" : "Ko",
    "Spriggan" : "Sp",
    "Naga" : "Na",
    "Centaur" : "Ce",
    "Ogre" : "Og",
    "Troll" : "Tr",
    "Minotaur" : "Mi",
    "Tengu" : "Te",
    "Draconian" : "Dr",
    "Demigod" : "Dg",
    "Demonspawn" : "Ds",
    "Mummy" : "Mu",
    "Ghoul" : "Gh",
    "Vampire" : "Vp",
    "Felid" : "Fe",
    "Octopode" : "Op",
    "Hill Dwarf" : "HD",
    "Elf" : "El",
    "Ogre-mage" : "OM",
    "Grey Elf" : "GE",
    "Gnome" : "Gn",
    "Mountain Dwarf" : "MD"
    }

### Background Mapping Dictionary ###

dBackground = {
    "Fighter" : "Fi",
    "Gladiator" : "Gl",
    "Monk" : "Mo",
    "Hunter" : "Hu",
    "Assassin" : "As",
    "Berserker" : "Be",
    "Abyssal Knight" : "AK",
    "Chaos Knight" : "CK",
    "Death Knight" : "DK",
    "Priest" : "Pr",
    "Healer" : "He",
    "Skald" : "Sk",
    "Enchanter" : "En",
    "Transmuter" : "Tm",
    "Arcane Marksman" : "AM",
    "Stalker" : "St",
    "Warper" : "Wr",
    "Wizard" : "Wz",
    "Conjurer" : "Cj",
    "Summoner" : "Su",
    "Necromancer" : "Ne",
    "Fire Elementalist" : "FE",
    "Ice Elementalist" : "IE",
    "Air Elementalist" : "AE",
    "Earth Elementalist" : "EE",
    "Venom Mage" : "VM",
    "Artificer" : "Ar",
    "Wanderer" : "Wn",
    "Paladin" : "Pa",
    "Reaver" : "Re",
    "Thief" : "Th"
    }


## Achievements
## Format is the following:
## InternalID : [AlternativeID : Short Name, Long Name, Short Desc : Long Desc]

dAchievementList = {
    0 : [0, "Win", "Winner", "A Winner is You", "Escaped with the Orb"],
    1 : [1, "Maximum Level", "Maximum Level", "Maximum Level", "Hit level 27 with at least one character"],
    2 : [2, "Game Complete", "Game Complete", "Game Complete", "Escaped with the Orb and 15 runes"],
    3 : [3, "SlowAndSteady1", "Slow and Steady I", "XL 9 in 2 consecutive games", "Reach XL 9 in 2 consecutive games"],
    4 : [4, "SlowAndSteady2", "Slow and Steady II", "Achieve a 2-win streak", "Achieve a 2-win streak"],
    5 : [5, "SlowAndSteady3", "Slow and Steady III", "4-win streak with 4 diff species & backgrounds", "Achieve a 4-win streak with 4 distinct species & backgrounds"],
    6 : [6, "Explorer1", "Explorer I", "Reach Lair:8 before returning to Dungeon", "After entering Lair for the 1st time, reach Lair:8 before returning to the Dungeon"],
    7 : [7, "Explorer2", "Explorer II", "Win a game in where when you enter a branch for the 1st time, you reach the end of the branch before leaving", "Win a game in where when you enter a branch for the 1st time, you reach the end of the branch before leaving"],
    8 : [8, "Explorer3", "Explorer III", "Win a game as in II, except all subbranches must be completed", "Win a game as in II, except all subbranches must be completed before leaving the branch. I.e., all subbranches of Lair must be complete before leaving Lair"],
    9 : [9, "Pious1", "Pious I", "Champion any god", "Champion (******) any god"],
    10 : [10, "Pious2", "Pious II", "Champion 5 different gods", "Champion 5 different gods"],
    11 : [11, "Pious3", "Pious III", "Champion 13 different gods", "Champion 13 different gods"],
    12 : [12, "NaturesAlly1", "Nature's Ally I", "Enter the Crypt", "Enter the Crypt"],
    13 : [13, "NaturesAlly2", "Nature's Ally II", "Get the golden rune", "Get the golden rune"],
    14 : [14, "NaturesAlly3", "Nature's Ally III", "Enter Tomb for the first time after picking up the Orb of Zot and then get the Golden Rune", "Enter Tomb for the first time after picking up the Orb of Zot and then get the Golden Rune"],
    15 : [15, "GelatinousBody1", "Gelatinous Body I", "Reach XL:9 with 5 different species and backgrounds", "Reach XL:9 with 5 different species and backgrounds"],
    16 : [16, "GelatinousBody2", "Gelatinous Body II", "Get a rune with 5 different species and backgrounds", "Get a rune with 5 different species and backgrounds"],
    17 : [17, "GelatinousBody3", "Gelatinous Body II", "Win with 5 different species and backgrounds", "Win with 5 different species and backgrounds"]   
    

    }

## Table Index Format

dSpeciesTableIndex = {
    "Human" : 0,
    "High Elf" : 1,
    "Deep Elf" : 2,
    "Sludge Elf" : 3,
    "Deep Dwarf" : 4,
    "Hill Orc" : 5,
    "Merfolk" : 6,
    "Halfling" : 7,
    "Kobold" : 8,
    "Spriggan" : 9,
    "Naga" : 10,
    "Centaur" : 11,
    "Ogre" : 12,
    "Troll" : 13,
    "Minotaur" : 14,
    "Tengu" : 15,
    "Draconian" : 16,
    "Demigod" : 17,
    "Demonspawn" : 18,
    "Mummy" : 19,
    "Ghoul" : 20,
    "Vampire" : 21,
    "Felid" : 22,
    "Octopode" : 23,
    "Hill Dwarf" : 24,
    "Elf" : 25,
    "Ogre-mage" : 26,
    "Grey Elf" : 27,
    "Gnome" : 28,
    "Mountain Dwarf" : 29
    }

dSpeciesShortTableList = ["Hu", "HE", "DE", "SE", "DD", "HO", "Mf", "Ha", "Ko",
                          "Sp", "Na", "Ce", "Og", "Tr", "Mi", "Te", "Dr", "Dg",
                          "Ds", "Mu", "Gh", "Vp", "Fe", "Op", "HD", "El", "OM",
                          "GE", "Gn", "MD"]


dBackgroundTableIndex = {
    "Fighter" : 0,
    "Gladiator" : 1,
    "Monk" : 2,
    "Hunter" : 3,
    "Assassin" : 4,
    "Berserker" : 5,
    "Abyssal Knight" : 6,
    "Chaos Knight" : 7,
    "Death Knight" : 8,
    "Priest" : 9,
    "Healer" : 10,
    "Skald" : 11,
    "Enchanter" : 12,
    "Transmuter" : 13,
    "Arcane Marksman" : 14,
    "Stalker" : 15,
    "Warper" : 16,
    "Wizard" : 17,
    "Conjurer" : 18,
    "Summoner" : 19,
    "Necromancer" : 20,
    "Fire Elementalist" : 21,
    "Ice Elementalist" : 22,
    "Air Elementalist" : 23,
    "Earth Elementalist" : 24,
    "Venom Mage" : 25,
    "Artificer" : 26,
    "Wanderer" : 27,
    "Paladin" : 28,
    "Reaver" : 29,
    "Thief" : 30
    }

dBackgroundShortTableList = ["Fi", "Gl", "Mo", "Hu", "As", "Be", "AK", "CK",
                             "DK", "Pr", "He", "Sk", "En", "Tm", "AM", "St",
                             "Wr", "Wz", "Cj", "Su", "Ne", "FE", "IE", "AE",
                             "EE", "VM", "Ar", "Wn", "Pa", "Re", "Th"]
