import os
import numpy as np
import pandas as pd
from pathlib import Path
import random
import time
from os import listdir
from os.path import isfile, join

blankHash = "bf619eac0cdf3f68d496ea9344137e8b"

def getRandomList(dict_in, sample_rate):

    totalNumberOfSamples = int(sample_rate * len(dict_in))

    random_values = []
    count = 0
    while  (count < totalNumberOfSamples ) :
       key = random.choice(list(dict_in.keys()))
       if dict_in[key]['hash'] == blankHash :
           continue
       count = count + 1
       random_values.append(dict_in[key])


    # print("=== Random values ==")
    # print(', '.join(map(str, random_values)))
    # {'hash': '29df003c144587b95c75d4c9fc00dcdf', 'offset': 88},
    # {'hash': '5abf420d0700e423776e1e3a60ff0543', 'offset': 91},


    return random_values

def creatDirIfNotExist(dirName):
   if not os.path.exists(dirName):
       os.mkdir(dirName)
       print("Directory " , dirName ,  " Created ")
   else:
       print("Directory " , dirName ,  " already exists")


def createOneSampleFileFromCSV(srcfile, outfile, sample_rate):

   # Load spreadsheet
   colNames = ['hash', 'offset']
   src = pd.read_csv(srcfile, names=colNames, header=None, delimiter=',')

   #print(src)
   src_dict = src.to_dict('index')
   #print(src_dict)

   # print(src_dict)
   # {0: {'hash': '87f7904a84dbde02cd8c69f3d043683d', 'offset': 1},
   #  1: {'hash': 'bf619eac0cdf3f68d496ea9344137e8b', 'offset': 2}
   #   .....

   randomList = getRandomList(src_dict, sample_rate)

   f = open(outfile, 'w')
   for e in randomList:
      f.write(e['hash'] + ',  ' + str(e['offset']) + '\n')
   f.close()
   # Begin for debug
   #for e in randomList:
   #    print(e['hash'] + " " + str(e['offset']))
   # End for debug

def createSampleFilesFromCSV():
    # sample_rate = 0.3
   sample_rates = {5, 10, 20, 30, 40, 50, 75}
   sample_rates = {5}
   srcDir = 'G:/M57/Md5CsvFull/C'
   outSampleEmpDir = 'G:/M57/Sample/C/'
   onlyfiles = [f for f in listdir(srcDir) if isfile(join(srcDir, f))]
   count = 1
   for baseSrcfile in onlyfiles:
       baseSrcfile = 'c11_20_f.csv'
       baseSrcDir = baseSrcfile.replace('.csv', '')
       outDir = Path(outSampleEmpDir) / baseSrcDir
       creatDirIfNotExist(outDir)

       #srcfile = (srcDir / baseSrcfile)
       srcfile = Path(srcDir) / baseSrcfile
       print(srcfile)

       startTimeForDisplay = time.strftime("%c")
       print(baseSrcfile + '.. starts at ' + startTimeForDisplay)

       for intRate in sorted(sample_rates):
           baseOutfile = baseSrcDir + '_Rate_' + str(intRate) + '.csv'
           #print(baseOutfile)
           outfile = outDir / baseOutfile
           #print(outfile)
           sampleRate = intRate /100
           startTimeForSampleFile = time.strftime("%c")
           print('    ' + baseOutfile + '.. starts at ' + startTimeForSampleFile)
           createOneSampleFile(srcfile, outfile, sampleRate)
           endTimeForSampleFile = time.strftime("%c")
           print('    ' + baseOutfile + '..  ends  at ' + endTimeForSampleFile)

       endTimeForDisplay = time.strftime("%c")
       print(baseSrcfile + '..   ends at ' + endTimeForDisplay)
       if (count ==1) :
           break

if __name__ == '__main__':
    Main()