import csv
import os

Dir ='G:\Backup\WinImage\win-Vista_bz_32'
inFile='vista_md5hash.txt'
outFile='vista_md5hash.csv'

#Dir ='G:\Backup\WinImage\win-XP-Pro'
#inFile='xpPro_md5hash.txt'
#outFile='xpPro_md5hash.csv'


inFullFile = os.path.join(Dir, inFile)
outFullFile = os.path.join(Dir, outFile)
with open(inFullFile, newline = '') as md5HashFile:
    with open(outFullFile, 'w') as csvFile:
        hashList = csv.reader(md5HashFile, delimiter=' ')
        count = 0
        for hash in hashList:
            count +=1
            aLine = hash[0] + ',' + str(count) +'\n'
            #print(aLine)
            csvFile.write(aLine)
            #if (count > 10):
            #    break