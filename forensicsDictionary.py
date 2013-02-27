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

### Branches List ###

lOverviewBranchList = ["Dungeon", "Temple", "Orc", "Elf", "Lair", "Swamp", "Snake", "Slime", "Vaults", "Blade", "Crypt", "Tomb", "Dis", "Geh", "Coc", "Tar", "Zot", "Hive"]


## Achievements
## Format is the following:
## InternalID : [AlternativeID : Short Name, Long Name, Short Desc : Long Desc]

dAchievementList = {
    990 : [990, "Win", "Winner", "A Winner is You", "Escaped with the Orb"],
    991 : [991, "Maximum Level", "Maximum Level", "Maximum Level", "Hit level 27 with at least one character"],
    992 : [992, "Game Complete", "Game Complete", "Game Complete", "Escaped with the Orb and 15 runes"],
    0 : [0, "SlowAndSteady1", "Slow and Steady I", "XL 9 in 2 consecutive games", "Reach XL 9 in 2 consecutive games"],
    1 : [1, "SlowAndSteady2", "Slow and Steady II", "Achieve a 2-win streak", "Achieve a 2-win streak"],
    2 : [2, "SlowAndSteady3", "Slow and Steady III", "4-win streak with 4 diff species & backgrounds", "Achieve a 4-win streak with 4 distinct species & backgrounds"],
    3 : [3, "Explorer1", "Explorer I", "Reach Lair:8 before returning to Dungeon", "After entering Lair for the 1st time, reach Lair:8 before returning to the Dungeon"],
    4 : [4, "Explorer2", "Explorer II", "Win a game in where when you enter a branch for the 1st time, you reach the end of the branch before leaving", "Win a game in where when you enter a branch for the 1st time, you reach the end of the branch before leaving"],
    5 : [5, "Explorer3", "Explorer III", "Win a game as in II, except all subbranches must be completed", "Win a game as in II, except all subbranches must be completed before leaving the branch. I.e., all subbranches of Lair must be complete before leaving Lair"],
    6 : [6, "Pious1", "Pious I", "Champion any god", "Champion (******) any god"],
    7 : [7, "Pious2", "Pious II", "Champion 5 different gods", "Champion 5 different gods"],
    8 : [8, "Pious3", "Pious III", "Champion 13 different gods", "Champion 13 different gods"],
    9 : [9, "NaturesAlly1", "Nature's Ally I", "Enter the Crypt", "Enter the Crypt"],
    10 : [10, "NaturesAlly2", "Nature's Ally II", "Get the golden rune", "Get the golden rune"],
    11 : [11, "NaturesAlly3", "Nature's Ally III", "Enter Tomb for the first time after picking up the Orb of Zot and then get the Golden Rune", "Enter Tomb for the first time after picking up the Orb of Zot and then get the Golden Rune"],
    12 : [12, "GelatinousBody1", "Gelatinous Body I", "Reach XL:9 with 5 different species and backgrounds", "Reach XL:9 with 5 different species and backgrounds"],
    13 : [13, "GelatinousBody2", "Gelatinous Body II", "Get a rune with 5 different species and backgrounds", "Get a rune with 5 different species and backgrounds"],
    14 : [14, "GelatinousBody3", "Gelatinous Body III", "Win with 5 different species and backgrounds", "Win with 5 different species and backgrounds"],   
    15 : [15, "LordOfDarkness1", "Lord of Darkness I", "Enter the Vestibule of Hell without having entered the Lair", "Enter the Vestibule of Hell without having entered the Lair"],
    16 : [16, "LordOfDarkness2", "Lord of Darkness II", "Win a game without having entered the Lair", "Win a game without having entered the Lair"],
    17 : [17, "LordOfDarkness3", "Lord of Darkness III", "Win a game without having entered the Temple, Orcish Mines, Lair, or Vaults", "Win a game without having entered the Temple, Orcish Mines, Lair, or Vaults"],
    18 : [18, "AbyssalTourist1", "Abyssal Tourist I", "Survive the abyss without having worshipped Lugonu in that game", "Survive the abyss without having worshipped Lugonu in that game"],
    19 : [19, "AbyssalTourist2", "Abyssal Tourist II", "Find the abyssal rune and escape the Abyss without following Lugonu in that game", "Find the abyssal rune and escape the Abyss without following Lugonu in that game"],
    20 : [20, "AbyssalTourist3", "Abyssal Tourist III", "Find the abyssal rune and escape the Abyss before XL 13 and without following Lugonu in that game", "Find the abyssal rune and escape the Abyss before XL 13 and without following Lugonu in that game"],
    21 : [21, "Conqueror1", "Conqueror I", "Reach XL 13", "Reach XL 13"],
    22 : [22, "Conqueror2", "Conqueror II", "Win a game", "Win a game"],
    23 : [23, "Conqueror3", "Conqueror III", "Win a game in under 50000 turns", "Win a game in under 50000 turns"],
    24 : [24, "Lorekeeper1", "Lorekeeper I", "Enter a branch that contains a rune.", "Enter a branch that contains a rune."],
    25 : [25, "Lorekeeper2", "Lorekeeper II", "Find 5 distinct runes.", "Find 5 distinct runes."],
    26 : [26, "Lorekeeper3", "Lorekeeper III", "Find 17 distinct runes.", "Find 17 distinct runes."],
    27 : [27, "VowOfCourage1", "Vow of Courage I", "Get a rune before entering D:14 (or below) in that game.", "Get a rune before entering D:14 (or below) in that game."],
    28 : [28, "VowOfCourage2", "Vow of Courage II", "Get two runes before entering D:14 (or below) in that game.", "Get two runes before entering D:14 (or below) in that game."],
    29 : [29, "VowOfCourage3", "Vow of Courage III", "Get four runes before entering D:14 (or below) in that game.", "Get four runes before entering D:14 (or below) in that game."],
    30 : [30, "RuthlessEfficiency1", "Ruthless Efficiency I", "Kill any two uniques within two turns of each other.", "Kill any two uniques within two turns of each other."],
    31 : [31, "RuthlessEfficiency2", "Ruthless Efficiency II", "Kill two medium or deep uniques within one turn of each other.", "Kill two medium or deep uniques within one turn of each other."],
    32 : [32, "RuthlessEfficiency3", "Ruthless Efficiency III", " Kill two deep uniques on the same turn.", "Kill two deep uniques on the same turn."],
    33 : [33, "DescentIntoMadness1", "Descent into Madness I", "Enter a ziggurat.", "Enter a ziggurat."],
    34 : [34, "DescentIntoMadness2", "Descent into Madness II", "Reach the 14th floor of a ziggurat.", "Reach the 14th floor of a ziggurat."],
    35 : [35, "DescentIntoMadness3", "Descent into Madness III", "Leave a ziggurat from its lowest floor.", "Leave a ziggurat from its lowest floor."],
    36 : [36, "AngelOfJustice1", "Angel of Justice I", "Enter either Pandemonium or any branch of Hell.", "Enter either Pandemonium or any branch of Hell."],
    37 : [37, "AngelOfJustice2", "Angel of Justice II", "Kill at least one unique pan lord and at least one unique hell lord.", "Kill at least one unique pan lord and at least one unique hell lord."],
    38 : [38, "AngelOfJustice3", "Angel of Justice III", "Kill all four unique pan lords and all four unique hell lords.", "Kill all four unique pan lords and all four unique hell lords."], 
    39 : [39, "Harvest1", "Harvest I", "Kill 25 distinct uniques", "Kill 25 distinct uniques"],
    40 : [40, "Harvest2", "Harvest II", "Kill 45 distinct uniques", "Kill 45 distinct uniques"],
    41 : [41, "Harvest3", "Harvest III", "Kill 65 distinct uniques", "Kill 65 distinct uniques"],
    
    
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


## Unique List (Note: Updated as of v0.11)

# Uniques who do not normally generate before depth 18.
lDeepUniques = ["Antaeus", "Asmodeus", "Boris", "Cerebov", "Dispater", "Dissolution", "Ereshkigal", "Frederick", "Geryon", "Gloorx Vloq", "Ignacio", "Ilsuiw", "Jory", 
                "Khufu", "Lom Lobon", "Mara", "Margery", "Mennas", "Mnoleg", "Murray", "the Enchantress", "the Lernaean hydra", "the Serpent of Hell", "the royal jelly",
                "Tiamat", "Xtahua"]

# Uniques who do not normally generate before depth 11 and are not on the previous list.
lMediumUniques = ["Agnes", "Aizul", "Arachne", "Azrael", "Donald", "Frances", "Kirke", "Louise", "Maud", "Nergalle", "Nessos", "Nikola", "Norris", "Polyphemus", 
                  "Roxanne", "Rupert", "Saint Roka", "Snorg", "Wiglaf"]

# Uniques who are not on the previous lists.
lShallowUniques = ["Blork", "Crazy Yiuf", "Dowan", "Duvessa", "Edmund", "Erica", "Erolcha", "Eustachio", "Fannar", "Gastronok", "Grum", "Grinder", "Harold", "Ijyb", 
                   "Jessica", "Joseph", "Josephine", "Maurice", "Menkaure", "Pikel", "Prince Ribbit", "Psyche", "Purgy", "Sigmund", "Sonja", "Terence", "Urug"]

# All uniques
lUniques = lDeepUniques + lMediumUniques + lShallowUniques
