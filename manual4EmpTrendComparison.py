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


   
#=============================================
# drawManualPlotForNormalized()
#---------------------
def drawManualPlotForNomalized():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    global ax1
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1,), (0,0))



    x_C = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24', '11-30',
           '12-01', '12-02', '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11']
    
    y_C = [0.47226140731, 0.4223413257, 0.503406981546, 0.546694415323, 0.569657820051, 0.626371550564, 0.626517574556, 0.638745551718, 0.647707557242, 0.644962411615,
           0.655268281899, 0.658436722593, 0.643846052709, 0.630111848389, 0.637966643286,  0.634,  0.629178228792, 0.535650607859, 0.535800310221]
     #'12-08' is inserted by interpolation


    x_J = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19','11-23', '11-24', '11-30',
           '12-01', '12-02', '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11-001']
    y_J = [0.360448641188, 0.340995707189, 0.37671072589, 0.376302823793, 0.395131125392, 0.395916610751,  0.388765891902, 0.465606548303,
           0.559227928252, 0.563934968181, 0.572423123995, 0.583597254437, 0.574024789344, 0.554712322212, 0.564093131333, 0.538854867619, 0.526265387399, 0.513837654204
]
 # removed '11-20-new', '11-20-old'  '12-11-002'
    x_P = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24', '11-30',
           '12-01', '12-02', '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11']
    y_P = [
0.368208458546, 0.348987090186, 0.468831302521, 0.476082765217, 0.49547737661, 0.551574196848, 0.578530708412, 0.614924372735, 0.657410169231, 0.683750600664,
0.679268108726, 0.697988573101, 0.696230551213, 0.691317267342, 0.675420377796, 0.651725235313, 0.650334388957, 0.63359968743, 0.631238613422
]


    x_T = [
'11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24', '11-30',
'12-01', '12-02', '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11-001']
    y_T = [
0.273859142866, 0.249071705883, 0.286550316572, 0.28299247045, 0.276143776549, 0.310806996514, 0.342008539799, 0.376096350346, 0.403466302521, 0.463962362116,
0.464326570283, 0.468183489089, 0.473603678679, 0.477291732092, 0.488679853353, 0.496992359566, 0.492537620639, 0.492321549245, 0.484517352939
]

   
     

    TitleString = "Comparison"

    ax1.plot(x_C, y_C, label='Charlie')
    ax1.plot(x_J, y_J, label='Jo')
    ax1.plot(x_P, y_P, label='Pat')
    ax1.plot(x_T, y_T, label='Terry')

  
    '''
    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')  
    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
    '''
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65) 

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(TitleString)
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom =0.21, right=0.94, top=0.95, wspace=0.2, hspace=0)

   
    pngFile= WorkingDir + TitleString + '_4_Emp_Non_Normalized.png'
    plt.savefig(pngFile, bbox_inches="tight", pad_inches=2,transparent=True)
    plt.show()


#=============================================
# drawManualPlotForNonNormalized()
#---------------------
def drawManualPlotForNonNomalized():
    global x_C, y_C_dataStore, x_J, y_J_dataStore, x_P, y_P_dataStore, x_T, y_T_dataStore
    global ax1
    
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1,), (0,0))

    

    x_C = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24',
           '11-30', '12-01', '12-02',  '12-03', '12-04', '12-07', '12-08', '12-09',  '12-10', '12-11' ]
    y_C_dataStore = [0.632447,0.582177,0.670682,0.701664,0.712600,0.756320,0.763604,0.773809,0.778139,
                     0.790539,0.797142,0.804689,0.798197,0.795916,0.803630, 0.8055    , 0.808965,    0.705377,0.685749]

    #12-08 is accerted. 0.8055 is averaging 0.803630(12-07) and  0.808965 (12-09)
 
    x_J = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-23',
           '11-24', '11-30', '12-01', '12-02', '12-03', '12-04','12-07', '12-08', '12-09',
           '12-10'  ]
    # REMOVED  '11-20-new','11-20-old' '12-11-001',  '12-11-002'
    y_J_dataStore = [0.510068,0.466230,0.508020,0.530476,0.530545,0.533058,0.508113,0.589090,0.687056,
                     0.701606,0.709529,0.749305,0.749830,0.763826,0.760515,0.752596,0.747283]
    
    x_P = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24',
           '11-30', '12-01',      '12-02',  '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11' ]
    y_P_dataStore = [0.510498,0.503068,0.604256,0.615644,0.632779,0.668068,0.693734,0.717161,
           0.756917,0.796259,0.804932,0.822046,0.829912,0.838054,0.833640,0.836465,0.831184,0.820886,0.831616]


    x_T = ['11-12', '11-12start', '11-16', '11-17', '11-18', '11-19', '11-20', '11-23', '11-24',
           '11-30', '12-01', '12-02', '12-03', '12-04', '12-07', '12-08', '12-09', '12-10', '12-11' ]
    y_T_dataStore = [0.406384918,0.353164019,0.424189535,0.423801134,0.409321505,0.475386497,0.499422645,0.557956231,0.584171094,
                     0.610956533,0.641366434,0.616914049,0.653736433,0.665332686,0.678743448,0.665909419,0.660516767,0.663782581,0.659092027]

     

    TitleString = "Comparison"

    ax1.plot(x_C, y_C_dataStore, label='Charlie')
    ax1.plot(x_J, y_J_dataStore, label='Jo')
    ax1.plot(x_P, y_P_dataStore, label='Pat')
    ax1.plot(x_T, y_T_dataStore, label='Terry')

  
    '''
    ax1.scatter(x_T, y_T_dataStore, label='Terry', marker='s')
    ax1.scatter(x_J, y_J_dataStore, label='Jo', marker='+')  
    ax1.scatter(x_C, y_C_dataStore, label='Charlie', marker='*')  
    ax1.scatter(x_P, y_P_dataStore, label='pat', marker='^')
    '''
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65) 

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(TitleString)
    plt.legend()
    plt.subplots_adjust(left=0.1, bottom =0.21, right=0.94, top=0.95, wspace=0.2, hspace=0)

   
    pngFile= WorkingDir + TitleString + '_4_Emp_Non_Normalized.png'
    plt.savefig(pngFile, bbox_inches="tight", pad_inches=2,transparent=True)
    plt.show()


    
#=====================
#   main()
#---------------------
def Main():

     
   drawManualPlotForNomalized()

   drawManualPlotForNonNomalized
   
    
    
##############  SET UP AREA ########### 
if __name__ == '__main__':
    
    print ("main called")
   
   
    WorkingDir = "C:/Research/Results_Jan_2019/" 
    
    
    Main()
    
