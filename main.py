import time
import random
import os
import numpy

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

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]

def calcPercent(userPhrase, correctPhrase):
    distance = levenshteinDistanceDP(userPhrase, correctPhrase)
    if len(userPhrase) >= len(correctPhrase):
        length = len(userPhrase)
    else:
        length = len(correctPhrase)
    percentage = (1 - distance/length) * 100
    return percentage

def calcWPM(chars, timeTaken):
    mins = timeTaken/60
    words = chars/5
    return words/mins

def giveUserLine(lineToType):
    print("The phrase is '" + lineToType + "'")
    input("Press enter to start")
    startTime = time.time()
    userString = input(lineToType + "\n")
    endTime = time.time()
    timeTaken = endTime - startTime
    return userString, timeTaken

def main():
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

if __name__ == "__main__":
    main()
