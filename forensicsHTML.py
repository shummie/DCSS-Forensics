title = "DCSS Forensics Output File"

def createHTML(gc):

    f = open("test.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f)
    f.write("<body>\n")

    # Outputs summary stats
    f.write('<h3>Overall Stats</h3>')
    statList = gc.overallStatsList()
    writeOverallStats(f, statList)

    # output list of games won
    f.write('<h3>Wins</h3>')
    winList = gc.allGamesWonList()
    writeGamesWonList(f, winList)

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


def writeHtmlStart(f):
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

def writeHeaderStart(f):
    f.write("<head>\n")
    f.write("<title>" + title + "</title>\n")

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
    lastrow = table[-1]
    f.write("<tr>")
    for item in header:
        f.write("<th>"+item+"</th>")
    f.write("</tr>\n")

    f.write("</table>\n")
    
    
def writeOverallStats(f, statList):

    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th>Total Score</th><th>Games</th><th>Wins</th><th>Win%</th><th>Best XL</th><th>Best Score</th><th>Average Score</th><th>Favorite Species</th><th>Favorite Background</th><th>Favorite Combo</th></tr>\n')
    f.write('<tr>')
    for item in statList:
        f.write('<td>'+str(item)+'</td>')
    f.write('</tr>')
    f.write('</table>\n')    

def writeGamesWonList(f, winList):
    # Note, winList is a list of gameInfo objects. The list should be sorted by
    # date already. Need to iterate through the list and output the details.

    f.write('<table class = "overall-stats bordered">\n')
    f.write('<tr><th></th><th>Score</th><th>Character</th><th>End</th><th>Turns</th><th>Duration</th><th>God</th><th>Runes</th><th>Time</th><th>Version</th></tr>\n')
    gameCount = 1
    for game in winList:
        f.write('<tr>')
        f.write('<td>'+str(gameCount)+'</td>')
        f.write('<td>'+str(game.score)+'</td>')
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
