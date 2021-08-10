import time
import random

def readLines(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    return lines

def isNewLine(string):
    if string != "\n":
        return True
    else:
        return False

def getLine():
    lines = readLines("thingsToType.txt")
    lines = list(filter(isNewLine, lines))
    line = lines[random.randint(0, len(lines)-1)]
    return line

def calcPercent(userPhrase, correctPhrase):
    return 100

def calcWPM(chars, time):
    return 100

lineToType = getLine()
startTime = time.time()
userString = input(lineToType + "\n")
endTime = time.time()

print("TimeTaken: " + str(endTime - startTime) + " seconds")
print("Percentage Correct:" + str(calcPercent("","")) + "%")
print("WPM: " + str(calcWPM("","")))















        
