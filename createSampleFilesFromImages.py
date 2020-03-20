from functools import partial
import hashlib
from pathlib import Path
import os
from os import listdir
from os.path import isfile, join
import time
from datetime import datetime
import numpy as np
import util

blankHash = "bf619eac0cdf3f68d496ea9344137e8b"



def createSampleFiles(osRemove):

   if osRemove == True :
       osOptionSuffix = '_NoOS'
   else:
       osOptionSuffix = ''

    # sample_rate = 0.3
   sample_rates = {5, 10, 20, 30, 40, 50, 75}
   #sample_rates = {5}
   Emp ='P'
   srcDir = 'E:/M57/Image/' + Emp
   Emp = 'T'
   srcDir = 'G:/M57/Image/' + Emp
   outSampleEmpDir = 'G:/M57/Sample/' + Emp + '/'
   onlyfiles = [f for f in listdir(srcDir) if isfile(join(srcDir, f))]

   onlyImgfiles = [f  for f in onlyfiles if not f.endswith('.txt')]
   for baseSrcfile in sorted(onlyImgfiles) :
       #baseSrcfile = 'c11_12.001'
       baseSrcDir = baseSrcfile.replace('.001', '')
       outDir = Path(outSampleEmpDir) / baseSrcDir
       creatDirIfNotExist(outDir)

       #srcfile = (srcDir / baseSrcfile)
       srcfile = Path(srcDir) / baseSrcfile
       #print(srcfile)

       with open(srcfile, 'rb') as srcFileobj :
           totalSector = int(getSize(srcFileobj) / 512)

           printTimeWithInfoString(baseSrcfile + ' starts.' )

           for intRate in sorted(sample_rates):
               baseOutfile = baseSrcDir + '_Rate_' + str(intRate) + osOptionSuffix + '.csv'
               outfile = outDir / baseOutfile

               sampleCount = int(totalSector * intRate /100)
               printTimeWithInfoString(baseOutfile + ' starts.  totalSector: ' + str(totalSector) + ', sampleCount: ' + str(sampleCount) )
               createOneSampleFileFromImage(srcfile, outfile, totalSector, sampleCount, osRemove)
               printTimeWithInfoString( baseOutfile + ' ends.')


           printTimeWithInfoString(baseSrcfile + ' ends.' )


def isOsSector(hash) :

    return True

def createOneSampleFileFromImage(imgfile, outfile, totalSector, sampleCount, osRemove) :
    sectorSize = 512
    basename = os.path.basename(imgfile).replace('.001', '')

    # inds will have FALSE and TRUE value for each sector
    inds  = np.random.random(totalSector) <= (sampleCount * 1.0 / totalSector)

    #print(outfile)
    with open(outfile, 'w') as md5file:
        with open(imgfile, 'rb') as openfileobject:
            iterCount = -1
            writeCount = 1
            osSectorCount = 0
            for chunk in iter(partial(openfileobject.read, sectorSize), b''):
                iterCount += 1
                if inds[iterCount] :
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

    infoFile = outfile.replace('.csv', '.info.txt')
    with open(infoFile, 'w') as infofile:
        infofile.write("Total sector count : " + str(totalSector))
        infofile.write("Total sample count : " + str(sampleCount))
        infofile.write("Total OS sector    : " + str(osSectorCount))

if __name__ == '__main__':
    Main()