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
## InternalID : [AlternativeID : Short Desc : Long Desc]

dAchievementList = {
    0 : [0, "A Winner is You", "Escaped with the Orb"],
    1 : [1, "Maximum Level", "Hit level 27 with at least one character"],
    2 : [2, "Game Complete", "Escaped with the Orb and 15 runes"]

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
