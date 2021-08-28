import time
import random
import os

def readLines(fileName):
    fileDir = os.path.dirname(__file__)
    fullPath = os.path.join(fileDir, fileName)
    f = open(fullPath, "r")
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

def getWords(inputSting):
    wordList = inputSting.split()
    return wordList

def calcPercent(userPhrase, correctPhrase):
    userWords = getWords(userPhrase)
    correctWords = getWords(correctPhrase)

    total = 0
    tempCorrectWords = correctWords.copy()
    for word in userWords:
        if word in tempCorrectWords:
            tempCorrectWords.remove(word)
            total += 1
    percentRight = (total/len(correctWords)) * 100
    return percentRight

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
