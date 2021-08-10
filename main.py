import time
import random

def readLines(fileName):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    return lines

def isNewLine(string):
    if string == "\n":
        return True
    else:
        return False

lines = readLines("thingsToType.txt")
#filter newline function
line = lines[random.randint(0, len(lines))]

print(lines)
print(line)
