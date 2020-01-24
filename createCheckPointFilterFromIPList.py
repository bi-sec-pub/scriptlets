# by: bi-sec 2020
# Read a file with a list with one IP per line and create a CheckPoint SmartConsole Filter
# with < 500 characters per line an write them to a file
#
# Useful to create a manual filter for example for C&C-IP-List like
# https://feodotracker.abuse.ch/downloads/ipblocklist.txt
import os

# Change to your needs
inFile = "input-ip-list.txt"
outFile = "cp-Filter.txt"
filterFillText = " OR dst:"
newLineCharacter = "\r"

#Temp-Vars
inLine = ""
outLine = ""
fLine = ""
writeFile = open(outFile, "w")  # recreate file
writeFile.close()

if os.path.isfile(inFile):
    with open(inFile, 'r') as file:
        fLine = file.readline()
        fLine = fLine.replace("\r\n", "")
        fLine = fLine.replace("\r", "")
        fLine = fLine.replace("\n", "")
        inLine = fLine
        while fLine:
            fLine = file.readline()
            fLine = fLine.replace("\r\n", "")
            fLine = fLine.replace("\r", "")
            fLine = fLine.replace("\n", "")
            if len(inLine) + len(fLine) + len(filterFillText) > 500:
                writeFile = open(outFile, "a")
                writeFile.write(inLine)
                writeFile.write(newLineCharacter)
                writeFile.close()
                inLine = fLine
            else:  # Just add to Line and
                inLine = inLine + filterFillText + fLine
