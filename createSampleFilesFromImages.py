#  This program  creates sample file by reading .001 files which was created from E01
# by using FTK (refer Research/Progress/DataConversion/DataProcess.txt
#
#
from functools import partial
import hashlib
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import time
from datetime import datetime
import numpy as np
import pandas as pd
import csv
import util as utl

blankHash = "bf619eac0cdf3f68d496ea9344137e8b"

def createSetFromOS_CsvFile():
    global  xpSet, vistaSet

    xpSet = set()
    vistaSet = set()
    xpDir = 'G:/Backup/WinImage/win-XP-Pro/'
    inCSVFile = 'xpPro_md5hash.csv'
    inFullFile = Path(xpDir) / inCSVFile

    with open(inFullFile, 'r') as md5HashFile:
        hashList = csv.reader(md5HashFile, delimiter=',')
        count = 0
        for hash, offset in hashList:
            count += 1
            #aLine = hash[0]
            #print(hash)
            xpSet.add(hash)

    vistaDir ='G:/Backup/WinImage/win-Vista_bz_32/'
    inCSVFile = 'vista_md5hash.csv'
    inFullFile = Path(vistaDir) / inCSVFile
    with open(inFullFile, 'r') as md5HashFile:
        hashList = csv.reader(md5HashFile, delimiter=',')
        count = 0
        for hash, offset in hashList:
            count += 1
            # aLine = hash[0]
            #print(hash)
            vistaSet.add(hash)

    vistaSet.remove(blankHash)
    xpSet.remove(blankHash)
    #print("====== XP SET ==============")
    #for e in xpSet:
    #   print(e + " ")



def createSampleFiles(osRemove):
   global xpSet, vistaSet

   if osRemove == True :
       osOptionSuffix = '_NoOS'
       createSetFromOS_CsvFile()
   else:
       osOptionSuffix = ''

    # sample_rate = 0.3
   sample_rates = {5, 10, 20, 30, 40, 50, 75}
   #sample_rates = {5}

  #
   Emp = 'T'
   srcDir = 'I:/M57/Image/' + Emp  + '/'
   Emp = 'P'
   srcDir = 'I:/M57/Image/' + Emp  + '/'
   Emp = 'J'
   srcDir = 'I:/M57/Image/' + Emp  + '/'
   Emp = 'C'
   srcDir = 'I:/M57/Image/' + Emp  + '/'

   if osRemove == True :
       outSampleEmpDir = 'I:/M57/SampleNoOS/' + Emp + '/'
   else:
       outSampleEmpDir = 'I:/M57/SampleWithOS/' + Emp + '/'
   onlyfiles = [f for f in listdir(srcDir) if isfile(join(srcDir, f))]

   # remove .txt file from the folder
   onlyImgfiles = [f  for f in onlyfiles if not f.endswith('.txt')]
   #onlyImgfiles = [ 'c11_12.001' ]
   for baseSrcfile in sorted(onlyImgfiles) :
       #baseSrcfile = 'c11_12.001'
       baseOutDir = baseSrcfile.replace('.001', '')
       outDir = Path(outSampleEmpDir) / baseOutDir
       utl.creatDirIfNotExist(outDir)

       srcfile = Path(srcDir) / baseSrcfile

       with open(srcfile, 'rb') as srcFileobj :
           totalSector = int(utl.getSize(srcFileobj) / 512)

           utl.printTimeWithInfoString(baseSrcfile + ' starts.' )

           for intRate in sorted(sample_rates):
               baseOutfile = baseOutDir + '_Rate_' + str(intRate) + osOptionSuffix + '.csv'
               outfile = Path(outDir) / baseOutfile

               sampleCount = int(totalSector * intRate /100)
               utl.printTimeWithInfoString(baseOutfile + ' starts.  totalSector: ' + str(totalSector) + ', sampleCount: ' + str(sampleCount) )
               createOneSampleFileFromImage(srcfile, outfile, totalSector, sampleCount, osRemove)
               utl.printTimeWithInfoString( baseOutfile + ' ends.')


           utl.printTimeWithInfoString(baseSrcfile + ' ends.' )



def isOsSector(testHash) :
    global xpSet, vistaSet

    result = False
    if testHash in xpSet:
        return True

    if testHash in vistaSet:
        return True
    return False

def do_something(b, cnt) :
    if (cnt % 1000000) == 0 :
        print (str(cnt) + '\n')

def junkTest() :
    sectorSize = 512
    filename =Path('I:/M57/Image/C/c11_12.001')

    cnt = 0
    with open(filename, 'rb') as f:
        while True:
            b = f.read(sectorSize)
            cnt += 1
            do_something(b, cnt)  # <- be prepared to handle a last chunk of size 0
            #    if the file length *is* a multiple of 50
            #    (incl. 0 byte-length file!)
            #    and be prepared to handle a last chunk of length < 50
            #    if the file length *is not* a multiple of 50
            if len(b) < 50:
                break
def junkTest1() :
    imgfile ='E:/M57/Image/C/c11_12.001'
    outImage = "E:/M57/Image/C/ctest.001"

    sectorSize = 512
    basename = os.path.basename(imgfile).replace('.001', '')

    maxChunk = 150

    with open(imgfile, 'rb') as openfileobject:
      with open("F:/BackUp/ctest.001", 'wb') as outFile:
            iterCount = -1
            writeCount = 1
            osSectorCount = 0
            for chunk in iter(partial(openfileobject.read, sectorSize), b''):
                outFile.write(chunk)
                writeCount += 1
                if (writeCount > maxChunk) :
                    break

    infoFile = outImage.replace('.001', '.info.txt')
    with open(infoFile, 'w') as infofile:
        infofile.write("Total maxChunk count : " + str(maxChunk))




def createOneSampleFileFromImage(imgfile, outfile, totalSector, sampleCount, osRemove) :
    sectorSize = 512
    osSectorCount = 0
    basename = os.path.basename(imgfile).replace('.001', '')
    # inds will have FALSE and TRUE value for each sector
    inds  = np.random.random(totalSector) <= (sampleCount * 1.0 / totalSector)

    timeStart = time.strftime("%c")
    with open(outfile, 'w') as md5file:
        with open(imgfile, 'rb') as openfileobject:
            iterCount = -1
            writeCount = 1

            #reader = partial(openfileobject.read1, sectorSize)
            #file_iterator = iter(reader, bytes())

            for chunk in iter(partial(openfileobject.read, sectorSize), b''):
                iterCount += 1
                if inds[iterCount] : # check if this index(iterCount) is in the random list
                   hash = hashlib.md5(chunk).hexdigest()
                   if osRemove == True and isOsSector(hash) :
                       osSectorCount += 1
                       continue
                   if (hash == blankHash) :
                      continue
                   else:
                      md5file.write(hash + "," + str(iterCount) + '\n')
                      writeCount += 1
                      if (writeCount > sampleCount) :
                         break


    infofile = Path(outfile).stem + '.info.txt'

    infoFileFull = Path(outfile).parent / infofile

    timeEnd = time.strftime("%c")
    with open(infoFileFull, 'w') as infoF:
        infoF.write(infofile)
        infoF.write('\n' + timeStart + ': start')
        infoF.write('\n' + timeEnd + ': end')
        infoF.write('\nTotal sector count : ' + str(totalSector))
        infoF.write('\nTotal sample count : ' + str(sampleCount))
        if osRemove :
           infoF.write('\nTotal OS sector    : ' + str(osSectorCount))
        else:
           infoF.write('\nOS sector is not removed.')
    if osRemove :
        filename = Path('I:\M57\SampleNoOS\masterInfoNoOS.txt')
    else :
        filename = Path('I:\M57\SampleWithOS\masterInfoWithOS.txt')
    with open(filename, 'a+') as minfoF:
        file = Path(outfile).stem
        minfoF.write(file + ','+str(totalSector)+','+str(sampleCount)+','+str(osSectorCount)+','+timeStart+','+timeEnd+'\n')

def Main():
    #junkTest()


     removeOS = True  # if True, os sector will be removed from sample files also
                       # otherwise only blankHash will be removed.

     #removeOS = False
     createSampleFiles(removeOS)


if __name__ == '__main__':
    Main()