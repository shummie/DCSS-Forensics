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

## Configuration File

import configparser
import os

## Enter path below to main DCSS directory
# PATH = "C:/Users/shumr/Documents/Ray/stone_soup-tiles-0.11"
# PATH = "C:/Users/shumr/Documents/Ray/crawl_tiles-0.12-a0-1684/morgue"
PATH = os.getcwd()


## Output file for the csv dump
#CSVOUTFILE = "test.csv"
CSVOUTFILE = ""

# Verbosity
# 1 = standard output
# 2 = general debugging output
# 3 = verbose
# 5 = FULL verbosity

#verbosity = 1
verbosity = 0


## HTML FILE OUTPUT VARIABLES
#NUM_RECENT_GAMES = 15
#NUM_TOP_SCORES = 15
NUM_RECENT_GAMES = 2
NUM_TOP_SCORES = 2
HTML_OUTFILE_PATH = os.getcwd()
CURRENT_WORKING_PATH = os.getcwd()


def readConfigFile(filename):
    try:
        config = configparser.ConfigParser()
        config.read(filename)
        
        ## Read VARIABLES data
        global PATH
        global CSVOUTFILE
        global verbosity
        PATH = config['VARIABLES']['PATH']
        CSVOUTFILE = config['VARIABLES']['CSVOUTFILE']
        verbosity = int(config['VARIABLES']['VERBOSITY'])
        
        ## Read HTMLOUTPUT data
        global NUM_RECENT_GAMES
        global NUM_TOP_SCORES
        global HTML_OUTFILE_PATH
        NUM_RECENT_GAMES = int(config['HTMLOUTPUT']['NUM_RECENT_GAMES'])
        NUM_TOP_SCORES = int(config['HTMLOUTPUT']['NUM_TOP_SCORES'])
        HTML_OUTFILE_PATH = config['HTMLOUTPUT']['HTML_OUTFILE_PATH']
    except:
        print("Error reading config.ini file. Using default values.")
    
    
    
    
    
