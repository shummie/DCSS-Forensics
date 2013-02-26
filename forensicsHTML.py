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

## This file contains all the code required to output various statistics into an .HTML file

import forensicsConfig
import forensicsDictionary
import os


def createHTMLOverview(gc):
    # This function creates an HTML file with various statistics produced
    
    os.chdir(forensicsConfig.HTML_OUTFILE_PATH)

    f = open("overview.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f, "DCSS Forensics Output File")
    f.write("<body>\n")

    # Outputs summary stats
    f.write('<h3>Overall Stats</h3>')
    statList = gc.overallStatsList()
    writeOverallStats(f, statList)

    # output list of games won
    f.write('<h3>Wins</h3>')
    winList = gc.allGamesWonList()
    writeGamesWonList(f, winList)
    
    # output list of recent 10 games
    f.write('<h3>Recent Games</h3>')
    recentGameList = gc.recentNGames(forensicsConfig.NUM_RECENT_GAMES)
    writeRecentGamesList(f, recentGameList)
    
    # output list of top 10 scores
    f.write('<h3>Top Scores</h3>')
    topScoreList = gc.topNScores(forensicsConfig.NUM_TOP_SCORES)
    writeTopScoreList(f, topScoreList)

    # Outputs the combo Tables
    f.write('<hr>\n')
    f.write('<h3>Winning Characters</h3>')
    winTable = gc.comboGamesWon()
    writeComboTable(f, winTable, winTable)

    f.write('<hr>\n')
    f.write('<h3>Games Played</h3>')
    comboGamesPlayedTable = gc.comboGamesPlayed()
    writeComboTable(f, comboGamesPlayedTable, winTable)    

    f.write('<hr>\n')
    f.write('<h3>Max Combo Level</h3>')
    comboLevelTable = gc.comboMaxLevel()
    writeComboTable(f, comboLevelTable, winTable)    

    f.write("</body>\n")
    f.write("</html>")

    f.close()



def createHTMLALLScoresTable(gc):
    
    os.chdir(forensicsConfig.HTML_OUTFILE_PATH)

    f = open("allScores.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f, "DCSS Forensics - All Games by Score")
    f.write("<body>\n")
    
    f.write("<h3>All Games sorted by Score</h3><hr>")
    gameList = gc.topNScores(len(gc.gameList))
    writeTopScoreList(f, gameList)
    
    f.write("</body>\n")
    f.write("</html>")

    f.close()
    
def createHTMLALLGamesTableRecent(gc):
    # outputs all games ordered by the most recent game first
    os.chdir(forensicsConfig.HTML_OUTFILE_PATH)

    f = open("allGamesByRecent.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f, "DCSS Forensics - All Games ordered by time")
    f.write("<body>\n")
    
    f.write("<h3>All Games sorted by Most Recent</h3><hr>")
    gameList = gc.recentNGames(len(gc.gameList))
    writeALLGamesTableRecent(f, gameList)
    
    f.write("</body>\n")
    f.write("</html>")

    f.close()

def createGameCollectionDump(gc):
    # outputs all games ordered in the same order as the gameCollection object
    os.chdir(forensicsConfig.HTML_OUTFILE_PATH)

    f = open("allGamesDump.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f, "DCSS Forensics - All Games - Total information dump")
    f.write("<body>\n")
    
    f.write("<h3>All Games Information</h3><hr>")
    gameList = gc.gameList
    writeGameCollectionDump(f, gameList)
    
    f.write("</body>\n")
    f.write("</html>")

    f.close()
    
def createAchievementDetailed(gc):
    # Outputs the achievement (detailed) data into an html file. Note this is a highly customizable section.
    
    os.chdir(forensicsConfig.HTML_OUTFILE_PATH)
    
    f = open("achievementsDetailed.html", "w")
    
    writeHtmlStart(f)
    writeHeaderStart(f, "DCSS Forensics - Achievements: Detailed")
    f.write("<body>\n")
    
    f.write("<h3>0.11 Tournament God Banners</h3><hr>")
    aNumList = [3, 4, 5, 6, 7, 8, 9, 10, 11]
    writeDetailedAchievements(f, gc.achievementList, aNumList, 6)
    
    f.write('</body>\n')
    f.write('</html>\n')
    
    f.close()
    

def writeHtmlStart(f):
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

def writeHeaderStart(f, title):
    f.write("<head>\n")
    f.write("<title>" + title + "</title>\n")

    writeStyleSheet(f, forensicsConfig.CURRENT_WORKING_PATH + "/style.css")
    # Note, will either need to embed style sheet into the html file or
    # figure out how to keep this separate since it references the sheet
    # from the active directory.
    f.write('<link rel="stylesheet" type="text/css" href="style.css">\n')
    f.write("</head>\n")

def writeComboTable(f, table, winTable):
    # Assume the table has a header row and descriptor column
    f.write('<table class = "stat-table bordered">\n')

    # Print the header row
    header = table[0]
    f.write("<tr>")
    for item in header:
        f.write("<th>"+item+"</th>")
    f.write("</tr>\n")

    # Print the remaining rows
    for i in range(1, len(table)-2):
        f.write("<tr>")

        # First column: Use Header formatting
        f.write("<th>"+table[i][0]+"</th>")

        f.write(('<td class = "stat-win">' if winTable[i][1] != "" else '<td>')
                +str(table[i][1])+'</td>')
        for j in range(2, len(table[i])-2):
            f.write(('<td class="stat-win">' if winTable[i][j] != "" else '<td>')
                    +str(table[i][j])+'</td>')

        # second to last column (Grand Total Column): Use GT formatting
        j += 1
        f.write('<td class = "stat-total' + (' stat-win">' if winTable[i][j] != "" else '">')
                +str(table[i][j])+'</td>')

        # Last column: Use Header formatting
        j += 1
        f.write("<th>"+table[i][j]+"</th>")

        # End row
        f.write("</tr>\n")

    # Second to last row: Grand Total Row
    i += 1
    f.write("<tr>")
    f.write("<th>"+table[i][0]+"</th>")
    for j in range(1, len(table[i])-2):
        f.write('<td class = "stat-total' + (' stat-win">' if winTable[i][j] != "" else '">')
                +str(table[i][j])+'</td>')

    # Last two columns use header formatting
    j += 1
    f.write("<th>"+table[i][j]+"</th>")
    j += 1
    f.write("<th>"+table[i][j]+"</th>")
    f.write("</tr>\n")

    # Last row uses header formatting
    # lastrow = table[-1] (Can remove, accidentally used header instead, but it *should* contain the same info
    f.write("<tr>")
    for item in header:
        f.write("<th>"+item+"</th>")
    f.write("</tr>\n")

    f.write("</table>\n")
    
    
def writeOverallStats(f, statList):

    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th>Total Score</th><th>Games</th><th>Wins</th><th>Win%</th><th>Best XL</th><th>Best Score</th><th>Average Score</th><th>Favorite Species</th><th>Favorite Background</th><th>Favorite Combo</th></tr>\n')
    f.write('<tr>')
    for i in range(0, 10):
        f.write('<td>'+str(statList[i])+'</td>')
    f.write('</tr>')
    f.write('</table>\n')    
    f.write('<p>\n')
    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th>Total Turns Taken</th><th>Runes Collected</th><th>Levels Visited</th><th>Creatures Vanquished</th><th>Gold Collected</th><th>Gold Spent</th></tr>\n')
    f.write('<tr>')
    for i in range(10, 16):
        f.write('<td>'+str(statList[i])+'</td>')
    f.write('</tr>')
    f.write('</table>\n')

def writeGamesWonList(f, winList):
    # Note, winList is a list of gameInfo objects. The list should be sorted by
    # date already. Need to iterate through the list and output the details.

    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Score</th><th>Character</th><th>End</th><th>Turns</th><th>Duration</th><th>God</th><th>Runes</th><th>Time</th><th>Version</th></tr>\n')
    gameCount = 1
    for game in winList:
        f.write('<tr class="even win">') if (gameCount % 2 == 0) else f.write('<tr class="odd win">') 
        f.write('<td>'+str(gameCount)+'</td>')
        f.write('<td>'+("{:,}".format((game.score)))+'</td>')
        f.write('<td>'+game.speciesShort+game.backgroundShort+'</td>')
        f.write('<td>'+game.end+'</td>')
        f.write('<td>'+str(game.turnsTaken)+'</td>')
        f.write('<td>'+game.timeTakenLong+'</td>')
        f.write('<td>'+game.god+'</td>')
        f.write('<td>'+str(game.numRunes)+'</td>')
        f.write('<td>'+game.datetime.isoformat(' ')+'</td>')
        f.write('<td>'+game.versionShort+'</td>')
        f.write('</tr>\n')
        gameCount += 1
    f.write('</table>\n')

def writeRecentGamesList(f, gameList):
    # gameList is a list of gameInfo objects. The list should be sorted by date. Need to iterate through and output details
    # Header fields are as follows:
    # Blank/Score / Character / God / Title / Place / End / XL / Turns / Duration / Runes / Date / Version
    
    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Score</th><th>Character</th><th>God</th><th>Title</th><th>Place</th><th>End</th><th>XL</th><th>Turns</th><th>Duration</th><th>Runes</th><th>Date</th><th>Version</th></tr>')
    gameCount = 1
    for game in gameList:
        trClassTag = ("even" if (gameCount % 2 == 0) else "odd")
        trClassTag += (" win" if game.winFlag == True else "")
        f.write('<tr class="' + trClassTag + '">')
        f.write("<td></td>")
        f.write('<td>'+("{:,}".format((game.score)))+'</td>')
        f.write('<td>'+game.speciesShort+game.backgroundShort+'</td>')
        f.write('<td>'+game.god+'</td>')
        f.write('<td>'+game.title+'</td>')
        f.write('<td>'+game.dungeonPlace+'</td>')
        f.write('<td>'+game.end+'</td>')
        f.write('<td>'+str(game.level)+'</td>')
        f.write('<td>'+("{:,}".format((game.turnsTaken)))+'</td>')
        f.write('<td>'+game.timeTakenLong+'</td>')
        f.write('<td>'+str(game.numRunes)+'</td>')
        f.write('<td>'+game.datetime.isoformat(' ')+'</td>')
        f.write('<td>'+game.versionShort+'</td>')
        gameCount += 1
    f.write('</table>\n')
    
def writeTopScoreList(f, gameList):
    # gameList is a list of gameInfo objects. The list should be sorted by date. Need to iterate through and output details
    # Header fields are as follows:
    # Rank / Score / Character / God / Title / Place / End / XL / Turns / Duration / Runes / Date / Version
    
    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Score</th><th>Character</th><th>God</th><th>Title</th><th>Place</th><th>End</th><th>XL</th><th>Turns</th><th>Duration</th><th>Runes</th><th>Date</th><th>Version</th></tr>')
    gameCount = 1
    for game in gameList:
        trClassTag = ("even" if (gameCount % 2 == 0) else "odd")
        trClassTag += (" win" if game.winFlag == True else "")
        f.write('<tr class="' + trClassTag + '">')
        f.write('<td>'+str(gameCount)+'</td>')
        f.write('<td>'+("{:,}".format((game.score)))+'</td>')
        f.write('<td>'+game.speciesShort+game.backgroundShort+'</td>')
        f.write('<td>'+game.god+'</td>')
        f.write('<td>'+game.title+'</td>')
        f.write('<td>'+game.dungeonPlace+'</td>')
        f.write('<td>'+game.end+'</td>')
        f.write('<td>'+str(game.level)+'</td>')
        f.write('<td>'+("{:,}".format((game.turnsTaken)))+'</td>')
        f.write('<td>'+game.timeTakenLong+'</td>')
        f.write('<td>'+str(game.numRunes)+'</td>')
        f.write('<td>'+game.datetime.isoformat(' ')+'</td>')
        f.write('<td>'+game.versionShort+'</td>')
        gameCount += 1
    f.write('</table>\n')
    
def writeALLGamesTableRecent(f, gameList):
    # gameList is a list of gameInfo objects. The list should be sorted by date. Need to iterate through and output details
    # Header fields are as follows:
    # Rank / Score / Character / God / Title / Place / End / XL / Turns / Duration / Runes / Date / Version
    
    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Score</th><th>Character</th><th>God</th><th>Title</th><th>Place</th><th>End</th><th>XL</th><th>Turns</th><th>Duration</th><th>Runes</th><th>Date</th><th>Version</th></tr>')
    gameCount = 1
    totalGames = len(gameList)
    for game in gameList:
        trClassTag = ("even" if (gameCount % 2 == 0) else "odd")
        trClassTag += (" win" if game.winFlag == True else "")
        f.write('<tr class="' + trClassTag + '">')
        f.write('<td>'+str(totalGames-gameCount+1)+'</td>')
        f.write('<td>'+("{:,}".format((game.score)))+'</td>')
        f.write('<td>'+game.speciesShort+game.backgroundShort+'</td>')
        f.write('<td>'+game.god+'</td>')
        f.write('<td>'+game.title+'</td>')
        f.write('<td>'+game.dungeonPlace+'</td>')
        f.write('<td>'+game.end+'</td>')
        f.write('<td>'+str(game.level)+'</td>')
        f.write('<td>'+("{:,}".format((game.turnsTaken)))+'</td>')
        f.write('<td>'+game.timeTakenLong+'</td>')
        f.write('<td>'+str(game.numRunes)+'</td>')
        f.write('<td>'+game.datetime.isoformat(' ')+'</td>')
        f.write('<td>'+game.versionShort+'</td>')
        gameCount += 1
    f.write('</table>\n')
    
def writeGameCollectionDump(f, gameList):
    # This is used to dump out the entire content of gameList.
    # May or may not be up to date. Will output into an HTML file so that all the info is there on a game by game basis
    # Can be modified to dump into a .csv file in the future, but for now, this is intended to make sure all the info for games
    # is captured appropriately.

    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Filename</th><th>Score</th><th>Character</th><th>God</th><th>Title</th><th>Place</th><th>End</th><th>XL</th><th>XL Long</th><th>Turns</th><th>Duration</th><th>Runes</th><th>Date</th><th>Version</th><th>Version-Long</th>' +
            '<th>ID</th><th>WinFlag</th><th>Branches Visited</th><th>Levels Visited</th><th>Pan Visits</th><th>Pan Level Visits</th><th>Abyss Trips</th><th>Bazaar Visits</th><th>Zig Visits</th><th>Zigs Completed</th><th>Zig Levels Visited</th><th>Deepest Zig Level</th>' + 
            '<th>Gold Collected</th><th>Gold Spent</th><th>Gold Donated</th><th>Gold for Misc</th><th>Creatures Vanquished</th></tr>')
    gameCount = 1
    for game in gameList:
        trClassTag = ("even" if (gameCount % 2 == 0) else "odd")
        trClassTag += (" win" if game.winFlag == True else "")
        f.write('<tr class="' + trClassTag + '">')
        f.write('<td>'+str(gameCount)+'</td>')
        f.write('<td>'+game.filename+'</td>')
        f.write('<td>'+("{:,}".format((game.score)))+'</td>')
        f.write('<td>'+game.speciesShort+game.backgroundShort+'</td>')
        f.write('<td>'+game.god+'</td>')
        f.write('<td>'+game.title+'</td>')
        f.write('<td>'+game.dungeonPlace+'</td>')
        f.write('<td>'+game.end+'</td>')
        f.write('<td>'+str(game.level)+'</td>')
        f.write('<td>'+str(game.levelLong)+'</td>')        
        f.write('<td>'+("{:,}".format((game.turnsTaken)))+'</td>')
        f.write('<td>'+game.timeTakenLong+'</td>')
        f.write('<td>'+str(game.numRunes)+'</td>')
        f.write('<td>'+game.datetime.isoformat(' ')+'</td>')
        f.write('<td>'+game.versionShort+'</td>')
        f.write('<td>'+game.versionLong+'</td>')
        f.write('<td>'+game.id+'</td>')
        f.write('<td>'+str(game.winFlag)+'</td>')
        f.write('<td>'+str(game.branchesVisited)+'</td>')
        f.write('<td>'+str(game.levelsVisited)+'</td>')
        f.write('<td>'+str(game.panVisits)+'</td>')
        f.write('<td>'+str(game.panLevelVisits)+'</td>')
        f.write('<td>'+str(game.abyssVisits)+'</td>')
        f.write('<td>'+str(game.bazaarVisits)+'</td>')
        f.write('<td>'+str(game.zigVisits)+'</td>')
        f.write('<td>'+str(game.zigCompleted)+'</td>')
        f.write('<td>'+str(game.zigLevelVisits)+'</td>')
        f.write('<td>'+str(game.zigDeepest)+'</td>')
        f.write('<td>'+str(game.goldCollected)+'</td>')
        f.write('<td>'+str(game.goldSpent)+'</td>')
        f.write('<td>'+str(game.goldDonated)+'</td>')
        f.write('<td>'+str(game.goldMisc)+'</td>')
        f.write('<td>'+str(game.numCreaturesVanquished)+'</td>')

        
        gameCount += 1
    f.write('</table>\n')    


def writeDetailedAchievements(f, aList, aNumList, numCol):
    # Outputs the detailed Achievement data from an gameCollecetion's achievementList (aList) and produces it in to # of columns
    f.write('<table class = "bordered achievements">\n')
    index = 0
    header = '<tr>'
    desc = '<tr>'
    progress = '<tr class = "progress">'
    
    
    while index < len(aNumList):
        if aList[aNumList[index]][0] == True: 
            header += '<th class = "done"'
            desc += '<td class = "done"'
            progress += '<td class = "done"'
        else:
            header += '<th'
            desc += '<td'
            progress += '<td'
        if index < numCol:
            header += ' width = 10%'
        header += '>' + forensicsDictionary.dAchievementList[aNumList[index]][2] + '</th>'
        desc += '>' + forensicsDictionary.dAchievementList[aNumList[index]][4] + '</td>'
        progress += '>' + aList[aNumList[index]][1] + '</td>'
        
        index += 1
        if (index % numCol == 0) or (index == len(aNumList)):
            header += '</tr>\n'
            desc += '</tr>\n'
            progress += '</tr>\n'
            f.write(header + desc + progress)
            header = '<tr>'
            desc = '<tr>'
            progress = '<tr class = "progress">'
        
            if index != len(aNumList):
                f.write('<tr><td colspan='+str(numCol)+'></td><tr>')
        
    f.write('</table>')
             
          
    
def writeStyleSheet(f, styleFile):
    # attempts to write the stylesheet internally. This way the stylesheet is not required in order for the sheet to be formatted
    # properly, but will utilize the external sheet if it exists.
    
    f_style = open(styleFile, "r")
    stylesheet = f_style.read()
    f.write(stylesheet)
    
