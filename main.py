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
    
def giveUserLine(lineToType):
    print("The phrase is '" + lineToType + "'")
    time.sleep(3)
    startTime = time.time()
    print("Go!")
    userString = input(lineToType + "\n")
    endTime = time.time()
    timeTaken = endTime - startTime
    return userString, timeTaken

lineToType = getLine()
userString, timeTaken = giveUserLine(lineToType)
percentCorrect = calcPercent(userString, lineToType)
wpm = calcWPM(len(userString), timeTaken)

print("Time Taken: " + str(round(timeTaken, 2)) + " seconds")
print("Percentage Correct:" + str(round(percentCorrect, 1)) + "%")
print("WPM: " + str(round(wpm, 2)))

if percentCorrect == 100:
    print("Perfect")
elif percentCorrect == 0:
    print("Fail")
elif percentCorrect < 50:
    print("Very inacurate")
elif percentCorrect < 75:
    print("Moderately accurate")
elif percentCorrect < 100:
    print("Mostly accurate")
else:
    print("Error in accuracy description section: percentCorrect = " + str(percentCorrect))