import numpy as np
import pandas as pd
import ntpath
import time
from datetime import datetime
from time import gmtime, strftime
import util
import os
#import createSampleFiles as sf
import createSampleFilesFromImages as sf

def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')


def test1():
    header(" sample ")
    filename = 'sample.txt'
    df = pd.read_csv(filename)
    print(df)

    print(df.index)
    print(df.columns)
    print(df.values)
    print(df.describe)


def MinMaxFind(n1, n2):
    if (n1 < n2):
        return n1, n2
    else:
        return n2, n1


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

jaccard = {}

#trgtList = {'G:/M57/SlimMd5/T/s_t11_16'}

def getJaccardIndexBetweenTwo(srcfile, trgtFile):
    start = datetime.now()  # for calc
    startTimeForDisplay = time.strftime("%c")  # for display
    # Load spreadsheet
    colNames = ['hash', 'offset']
    src = pd.read_csv(srcfile, names=colNames, header=None, delim_whitespace=True)
    trgt = pd.read_csv(trgtFile, names=colNames, header=None, delim_whitespace=True)
    # df = pd.concat([src, trgt], names=['h1', 'h2'], axis=1)

    # print(src)

    # print (src['hash'])
    df2 = pd.concat([src['hash'], trgt['hash']], axis=1)

    df2.columns = ['h1', 'h2']
    # print(df2.columns)
    # print(df2)
    # print(df2['h1'].count())
    h1grp = df2.groupby(['h1']).groups
    sumGrp1 = df2['h1'].count()
    print(" Group 1 done.")
    h2grp = df2.groupby(['h2']).groups
    sumGrp2 = df2['h2'].count()
    print(" Group 2 done.")
    dict1 = {}
    dict2 = {}
    print("Total 1: " + str(sumGrp1) + ", Total 2: " + str(sumGrp2))

    for key in h1grp:
        # print("{}: {}".format(key, len(h1grp[key])))
        dict1[key] = [len(h1grp[key]) / sumGrp1]
    # print("==  Dict 1")
    # print(dict1)
    for key in h2grp:
        # print("{}: {}".format(key, len(h2grp[key])))
        dict2[key] = [len(h2grp[key])]  # give the count of each hash

        if key in dict1:
            # print("{} :: {}".format(key, len(dict1[key])))
            dict1[key].append(len(h2grp[key]) / sumGrp2)
        else:
            dict1[key] = [len(h2grp[key]) / sumGrp2]

    # At this, some will have only one element in the list of dict1.
    # These are hash value which were not common.
    # but dict1 will have all the keys from both : source and target.


    minSum = 0
    maxSum = 0
    for key in dict1:
        if len(dict1[key]) == 1:
            # print("{}: {}".format(key, dict1[key]))
            dict1[key].append(0)

        min, max = MinMaxFind(dict1[key][0], dict1[key][1])
        minSum = minSum + min
        maxSum = maxSum + max

        # print("min =" + str(min) + ", max =" + str(max))

    jaccardIndex = minSum / maxSum
    jaccardkey = (path_leaf(srcfile), path_leaf(trgtFile))
    print("Jaccard Index  " + str(jaccardkey) + " : " + str(jaccardIndex))

    end = datetime.now()
    duration = end - start
    duration_in_s = duration.total_seconds()
    hours = divmod(duration_in_s, 3600)[0]
    minutes = divmod(duration_in_s, 60)[0]
    seconds = divmod(duration_in_s, 60)[1]
    # strftime("%Y-%m-%d %H:%M:%S", gmtime())

    jaccard[jaccardkey] = [jaccardIndex]

    jaccard[jaccardkey].append(startTimeForDisplay)
    jaccard[jaccardkey].append((" process time:(mm, ss) ", minutes, seconds))

def dumpJaccardIndex():
    for key in jaccard:
         print("{} :: {}".format(key, jaccard[key]))

srcfile = 'c:/Temp/JaccardData/source.csv'
trgtList = {'c:/Temp/JaccardData/target1.csv',
            'c:/Temp/JaccardData/target2.csv',
            'c:/temp/JaccardData/target3.csv',
            'c:/temp/JaccardData/target4.csv',
            'c:/temp/JaccardData/target5.csv',
            'c:/temp/JaccardData/target6.csv',
            'c:/temp/JaccardData/target7.csv'}

def Main():
    file = 'c:/temp/Data/example.xlsx'


    #srcfile = 'G:/M57/SlimMd5/P/s_p12_02'


    for trgtFile in sorted(trgtList):
        getJaccardIndexBetweenTwo(srcfile, trgtFile)
      # end of loop

    dumpJaccardIndex()


        # print("==  Dict 2")
        # print(dict2)
        # print("==  Dict 1 again == ")
        # print(dict1)
        # print(df2['h1'])
        # print(df2['h2'])
        # print(df2)

    '''
        idx = df.index
        clm = df.columns
        dataVal = df.values
        print(idx)
        print(clm)
        print(dataVal)
    '''
        # xl = pd.read_excel(file, header=None)
        # Print the sheet names
        # print(xl.sheet_names)
        # print(csv)
        # print(csvConcat)

def testCode():
 iterlen = 100
 sample_size = 20
 inds = np.random.random(iterlen) <= (sample_size * 1.0 / iterlen)
 r = np.random.random(iterlen)
 print(r)
 print(inds)

if __name__ == '__main__':
    #Main()
    import readImage
    #file ='E:/M57/Image/C/c11_12.001'
    #readImage.readImagesAndGenMD5Hash(file)
    #readImage.readImagesAndGenMD5Hash()

    #sf.createSampleFiles()

    removeOS = 'True' # if True, os sector will be removed from sample files also
                      # otherwise only blankHash will be removed.

    sf.createSampleFiles(removeOS)