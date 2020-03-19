import os
import time
from datetime import datetime


def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size


def printTimeWithInfoString(infoString) :
    timeForDisplay = time.strftime("%c")
    print(timeForDisplay + ': ' + infoString)

def creatDirIfNotExist(dirName):
   if not os.path.exists(dirName):
       os.mkdir(dirName)
       print("Directory " , dirName ,  " Created ")
   else:
       print("Directory " , dirName ,  " already exists")