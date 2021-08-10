import time

def readNextXLines(fileName):
    f = open(fileName, r)
    lines = f.readLines()
    f.close()
    return lines

