#!/usr/bin/env python

# This script tests the Python version and hashdb library functions.
# This script creates filenames starting with "temp_" in the local directory.

# ############################################################
# test Python version
# ############################################################
import sys
import datetime
import time
import os
import matplotlib.pyplot as plt
import csv
import numpy as np



#-------------------------------
#ResultFile contents
#-------------------------
#05:42:47 11/25/18 ::: @  CHARLIE
#22:36:23 11/27/18 :::====== Starting... Src:S_jo-11-12.hdb, Target:S_charlie_Random_All.hdb
#22:36:23 11/27/18 ::: TotalSizeHashesOfSource:5752108.0, TotalSizeHashesOfTarget:107901663.0
#22:45:20 11/27/18 ::: Calculated TotalSource:8597971, TotalTarget:152609027
#22:45:20 11/27/18 ::: JI:0.04580146229, Normalized JI:0.377420551568
#22:45:21 11/27/18 :::====== Starting... Src:S_jo-11-12start.hdb, Target:S_charlie_Random_All.hdb
#22:45:21 11/27/18 ::: TotalSizeHashesOfSource:5532015.0, TotalSizeHashesOfTarget:107901663.0
#22:53:09 11/27/18 ::: Calculated TotalSource:8515383, TotalTarget:152609027
#22:53:09 11/27/18 ::: JI:0.0456207038135, Normalized JI:0.355001425384
#    .........

#---------------------------------------------------
# List of chosen dates for imaginary data
#-----------------------------------------
#  charlie: 11-16, 11-20, 11-30, 12-04, 12-10
#  Jo:      11-12, 11-17, 11-23, 12-07, 12-11-002
#  pat:     11-12start, 11-18, 11-24, 12-04, 12-11   
#  Terry:   11-19, 11-23, 12-01, 12-03, 12-07
#----------------------------------------------------


CharlieImaginaryDates = ['11-16', '11-20', '11-30', '12-04', '12-10']
JoImaginaryDates = ['11-12', '11-17', '11-23', '12-07', '12-11-002']
PatImaginaryDates = ['11-12start', '11-18', '11-24', '12-04', '12-11']   
TerryImaginaryDates = ['11-19', '11-23', '12-01', '12-03', '12-07']


def dateInImaginary(date, person):    
  if (person == 'C'):
     dateList = CharlieImaginaryDates     
  elif (person == 'J'):
     dateList = JoImaginaryDates
  elif (person == 'P'):
     dateList = PatImaginaryDates
  elif (person == 'T'):
     dateList = TerryImaginaryDates

  for i_dt in dateList:
     if (date == i_dt):
        return True

  return False

def drawPlotForCharlieHashDataStoreAndStore():
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1,), (0,0))

    x_C = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24',
           '11-30', '12-01',      '12-02',  '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11' ]
    y_C_dataStore = [0.632447,0.582177,0.670682,0.701664,0.712600,0.756320,0.763604,0.773809,0.778139,
                     0.790539,0.797142,0.804689,0.798197,0.795916,0.803630,0.808965,0.705377,0.685749]

    y_C_Store =     [0.308174,0.287929,0.282364,0.348596,0.356321,0.377304,0.333087,0.390406,0.390019,
                     0.346381,0.404548,0.403796,0.409020,0.355813,0.408166,0.417065,0.364515,0.368514]

    ax1.scatter(x_C, y_C_dataStore, label='hash_data_store', marker='*')
    ax1.scatter(x_C, y_C_Store, label='hash_store', marker='+')
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65) 
    
   
   # print(x_C) 
    #plt.scatter(x_C, y_C, label='scatter', color='k', marker='*')


    
    TitleString = "Charlie"
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(TitleString)
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom =0.21, right=0.94, top=0.95, wspace=0.2, hspace=0)

   
    pngFile= WorkingDir + TitleString + 'hash_store.png'
    plt.savefig(pngFile, bbox_inches="tight", pad_inches=2,transparent=True)
    plt.show()


def setCharlieData():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    
    x_C = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24',
           '@11-30', '12-01',      '12-02',  '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11' ]
    y_C_dataStore = [0.632447,0.582177,0.670682,0.701664,0.712600,0.756320,0.763604,0.773809,0.778139,
                     0.790539,0.797142,0.804689,0.798197,0.795916,0.803630,0.808965,0.705377,0.685749]

    x_J = ['@11-16', '@11-20', '@11-30', '@12-04', '@12-10' ]  
    y_J_dataStore = [0.486080,0.523141,0.538398,0.533674,0.489852]
    
    x_P = ['@11-16', '@11-20', '@11-30', '@12-04' ]  
    y_P_dataStore = [0.492106,0.517342,0.494489,0.479734]
    
    x_T = ['@11-16', '@11-20', '@11-30', '@12-04', '@12-10' ]  
    y_T_dataStore = [0.105441,0.109627,0.115682,0.116129,0.106600]

   
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    
def setJoData():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    global ax1
    
    x_C = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002']
    y_C_dataStore = [0.580209,0.607690,0.471818,0.519579,0.495694]

    x_J = ['@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new','11-20-old', '@11-23',
           '11-24', '11-30', '12-01', '12-02', '12-03', '12-04','@12-07', '12-08', '12-09',
           '12-10', '12-11-001',  '@12-11-002',  'fav-usb-12-11',  'work-usb-12-11' ]  
    y_J_dataStore = [0.510068,0.466230,0.508020,0.530476,0.530545,0.533058,0.470032,0.590809,0.508113,0.589090,0.687056,
                     0.701606,0.709529,0.749305,0.749830,0.763826,0.760515,0.752596,0.747283,0.754391,0.768874,0.042184,0.000717]

    x_P = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002'] 
    y_P_dataStore = [0.477766,0.501286,0.418116,0.459298,0.448496]

    
    x_T = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002']  
    y_T_dataStore = [0.160137,0.170565,0.156133,0.209922,0.207862]
    
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')  
    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    
def setPatData():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    global ax1
    
    x_P = ['11-12', '@11-12start', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24',
           '11-30', '12-01',      '12-02',  '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11' ]
    y_P_dataStore = [0.510498,0.503068,0.604256,0.615644,0.632779,0.668068,0.693734,0.717161,
           0.756917,0.796259,0.804932,0.822046,0.829912,0.838054,0.833640,0.836465,0.831184,0.820886,0.831616]


    x_J = ['@11-12start', '@11-18',  '@11-24', '@12-04', '@12-11' ]  
    y_J_dataStore = [0.456029,0.489852,0.522277,0.541147,0.539731]

    
    x_C = ['@11-12start', '@11-18',  '@11-24', '@12-04', '@12-11' ]  
    y_C_dataStore = [0.540093,0.591994,0.565347,0.572104,0.562676]

    
    x_T = ['@11-12start', '@11-18',  '@11-24', '@12-04', '@12-11' ]  
    y_T_dataStore = [0.147636,0.174581,0.200509,0.214636,0.221010]


    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')  
    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    
def setTerryData():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    
    x_T = ['11-12', '11-12start', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24',
           '11-30', '@12-01',     '12-02', '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11' ]
    y_T_dataStore = [0.406384918,0.353164019,0.424189535,0.423801134,0.409321505,0.475386497,0.499422645,0.557956231,0.584171094,
                     0.610956533,0.641366434,0.616914049,0.653736433,0.665332686,0.678743448,0.665909419,0.660516767,0.663782581,0.659092027]

    x_C =  ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07' ]  
    y_C_dataStore = [0.260631,0.273086,0.403832,0.413554,0.391545]
    
    x_J = ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07' ]  
    y_J_dataStore = [0.256593,0.308625,0.341324,0.349416,0.331429]

    
    x_P = ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07' ] 
    y_P_dataStore = [0.230738,0.313590,0.309866,0.323403,0.304127]

    
   

    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')  
    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
   
#=====================
# drawManualPlot()
#---------------------
def drawManualPlot(person):
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    global ax1
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1,), (0,0))

    if (person == 'C'):
       setCharlieData()
       TitleString = "Charlie"
    elif (person == 'J'):
       setJoData()
       TitleString = "Jo"
    elif (person == 'P'):
       setPatData()
       TitleString = "Pat"
    elif (person == 'T'):
       setTerryData()
       TitleString = "Terry"

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65) 

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(TitleString)
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom =0.21, right=0.94, top=0.95, wspace=0.2, hspace=0)

   
    pngFile= WorkingDir + TitleString + '_crossCompare.png'
    plt.savefig(pngFile, bbox_inches="tight", pad_inches=2,transparent=True)
    plt.show()


    
#=====================
#   main()
#---------------------
def Main():

   #drawPlotForCharlieHashDataStoreAndStore()   
   drawManualPlot('C')
   drawManualPlot('J')
   drawManualPlot('P')
   drawManualPlot('T')
    
    
##############  SET UP AREA ########### 
if __name__ == '__main__':
    
    print ("main called")
    WorkingDir = "C:/Research/IFIP/matplotResult/"
    
    Main()
    
