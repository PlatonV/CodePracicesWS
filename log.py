from datetime import datetime

outputFile = open('log.txt', 'w')

def info(message):
    outputFile.write("[INFO] " + str(datetime.now()) + ": " + message + "\n")

def error(message):
    outputFile.write("[ERROR] " + str(datetime.now()) + ": " + message + "\n")
