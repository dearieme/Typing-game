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
    if line[-1] == "\n":
        line = line[:-1]
    return line

def calcPercent(userPhrase, correctPhrase):
    if len(userPhrase) > len(correctPhrase):
        length = len(correctPhrase)
    else:
        length = len(userPhrase)
    total = 0

    for i in range (length):
        if userPhrase[i] == correctPhrase[i]:
            total += 1
    return (total/len(correctPhrase))*100

def calcWPM(chars, timeTaken):
    mins = timeTaken/60
    words = chars/5
    return words/mins
    
lineToType = getLine()
print("The phrase is '" + lineToType + "'")
time.sleep(3)
startTime = time.time()
userString = input("Go!\n")
endTime = time.time()

print("Time Taken: " + str(round(endTime - startTime, 2)) + " seconds")
print("Percentage Correct:" + str(round(calcPercent(userString, lineToType), 1)) + "%")
print("WPM: " + str(round(calcWPM(len(userString),endTime-startTime), 2)))
if calcPercent(userString, lineToType) < 95:
    print("Fail")
else:
    print("Acceptable Accuracy")