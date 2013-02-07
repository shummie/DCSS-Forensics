title = "DCSS Forensics Output File"

def createHTML(gc):

    f = open("test.html", "w")

    writeHtmlStart(f)
    writeHeaderStart(f)
    f.write("<body>\n")

    f.write('<hr>\n')
    f.write('<h3>Winning Characters</h3>')
    winTable = gc.comboGamesWon()
    writeComboTable(f, winTable)

    f.write('<hr>\n')
    f.write('<h3>Max Combo Level</h3>')
    comboLevelTable = gc.comboMaxLevel()
    writeComboTable(f, comboLevelTable)    

    f.write("</body>\n")
    f.write("</html>")

    f.close()


def writeHtmlStart(f):
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")

def writeHeaderStart(f):
    f.write("<head>\n")
    f.write("<title>" + title + "</title>\n")
    f.write('<link rel="stylesheet" type="text/css" href="style.css">\n')
    f.write("</head>\n")

def writeComboTable(f, table):
    # Assume the table has a header row and descriptor column
    f.write('<table class = "stat-table bordered">\n')

    # Print the header row
    header = table[0]
    f.write("<tr>")
    for item in header:
        f.write("<th>"+item+"</th>")
    f.write("</tr>\n")

    # Print the remaining rows
    for i in range(1, len(table)):
        f.write("<tr>")
        f.write("<th>"+table[i][0]+"</th>")
        
        f.write('<td class = "wins">'+str(table[i][1])+'</td>')
        for j in range(2, len(table[i])):
            f.write('<td>'+str(table[i][j])+'</td>')
        f.write("</tr>\n")

    f.write("</table>\n")
    
    
        
    

    
