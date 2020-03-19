from functools import partial
import hashlib
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import time
from datetime import datetime

def readOneImageAndGenSampleMD5Hash(imgfile, outDir,  rate):
    sectorSize = 512

    basename = os.path.basename(imgfile).replace('.001','_f')

    md5FullFile = Path(outDir) /  basename

    print(md5FullFile)
    with open(md5FullFile, 'w') as md5file:
     with open(imgfile, 'rb') as openfileobject:
        count = 0
        for chunk in iter(partial(openfileobject.read, sectorSize), b''):
            count = count + 1
            hash = hashlib.md5(chunk).hexdigest()
            md5file.write(hash + "," + str(count) +'\n')

        print("total sector count :" + str(count))


def readOneImageAndGenMD5Hash(imgfile, outDir):
    sectorSize = 512

    basename = os.path.basename(imgfile).replace('.001','_f')

    md5FullFile = Path(outDir) /  basename

    print(md5FullFile)
    with open(md5FullFile, 'w') as md5file:
     with open(imgfile, 'rb') as openfileobject:
        count = 0
        for chunk in iter(partial(openfileobject.read, sectorSize), b''):
            count = count + 1
            hash = hashlib.md5(chunk).hexdigest()
            md5file.write(hash + "," + str(count) +'\n')

        print("total sector count :" + str(count))


def readImagesAndGenMD5Hash()  :
    imgDir ='G:/M57/Image/T/' # T is in G: folder
    md5Dir = 'G:/M57/Md5CsvFull/T/'

    onlyfiles = [f for f in listdir(imgDir) if isfile(join(imgDir, f))]
    count =1
    for f in onlyfiles :
        if not f.endswith('txt') :
         if f.find('11_16') != -1 : # found
            imgFullFile = Path(imgDir) / f
            print(imgFullFile)
            #break
            startTimeForDisplay = time.strftime("%c")
            print(f + '.. starts at ' + startTimeForDisplay)
            readOneImageAndGenMD5Hash(imgFullFile, md5Dir)
            endTimeForDisplay = time.strftime("%c")
            print(f + '..   ends at ' + endTimeForDisplay)


if __name__ == '__main__':
    Main()