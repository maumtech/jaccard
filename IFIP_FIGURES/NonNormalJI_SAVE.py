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
import csv
import numpy as np

from matplotlib import rcParams

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.text as text

fileType = 'eps'

def set_Terry_scatter_and_rotation():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T, x_Dummy, y_Dummy
    global ax1

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1,), (0, 0))

    # order is important
    ax1.scatter(x_T, y_T, label='Terry', marker='s')
    ax1.scatter(x_P, y_P, label='pat', marker='^')
    ax1.scatter(x_C, y_C, label='Charlie', marker='*')
    ax1.scatter(x_J, y_J, label='Jo', marker='+')


    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65)


def set_Pat_scatter_and_rotation():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T, x_Dummy, y_Dummy
    global ax1

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1,), (0, 0))

    # order is important
    ax1.scatter(x_P, y_P, label='pat', marker='^')
    ax1.scatter(x_C, y_C, label='Charlie', marker='*')
    ax1.scatter(x_J, y_J, label='Jo', marker='+')
    ax1.scatter(x_T, y_T, label='Terry', marker='s')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65)

def set_Jo_scatter_and_rotation():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T, x_Dummy, y_Dummy
    global ax1

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1,), (0, 0))

    # order is important
    ax1.scatter(x_J, y_J, label='Jo', marker='+')
    ax1.scatter(x_C, y_C, label='Charlie', marker='*')
    ax1.scatter(x_P, y_P, label='pat', marker='^')
    ax1.scatter(x_T, y_T, label='Terry', marker='s')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65)


def set_Charlie_scatter_and_rotation():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T, x_Dummy, y_Dummy
    global ax1

    fig = plt.figure()
    ax1 = plt.subplot2grid((1, 1,), (0, 0))

    # order is important
    ax1.scatter(x_C, y_C, label='Charlie', marker='*')
    ax1.scatter(x_J, y_J, label='Jo', marker='+')
    ax1.scatter(x_P, y_P, label='pat', marker='^')
    ax1.scatter(x_T, y_T, label='Terry', marker='s')

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(65)

def drawPicture(TitleString):


    plt.title(TitleString)
    plt.xlabel('Daily Image')
    plt.ylabel('JIWF')

    legend_properties = {'weight': 'bold'}


    plt.legend(prop=legend_properties)
    plt.legend()

    plt.subplots_adjust(left=0.1, bottom=0.21, right=0.94, top=0.95, wspace=0.2, hspace=0)

    picFile = WorkingDir + TitleString + fileType
    plt.savefig(picFile, bbox_inches="tight", pad_inches=2, dpi=600)
    plt.show()



# =============================================
# draw_Charlie_JIWF()
# ---------------------
def draw_Jo_JIWF():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global ax1

    titleString = "Jo JIWF"


    x_C = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002']
    y_C = [0.580209, 0.607690, 0.471818, 0.519579, 0.495694]
    x_J = ['@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new', '11-20-old', '@11-23',
           '11-24', '11-30', '12-01', '12-02', '12-03', '12-04', '@12-07', '12-08', '12-09',
           '12-10', '12-11-001', '@12-11-002']
    y_J = [0.510068, 0.466230, 0.508020, 0.530476, 0.530545, 0.533058, 0.470032, 0.590809, 0.508113, 0.589090,
           0.687056, 0.701606, 0.709529, 0.749305, 0.749830, 0.763826, 0.760515, 0.752596, 0.747283, 0.754391, 0.768874]

    x_P = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002']
    y_P = [0.477766, 0.501286, 0.418116, 0.459298, 0.448496]
    x_T = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-002']
    y_T = [0.160137, 0.170565, 0.156133, 0.209922, 0.207862]


    set_Jo_scatter_and_rotation()
    drawPicture(titleString)

# =============================================
# draw_Charlie_JIWF()
# ---------------------
def draw_Charlie_JIWF():
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Charlie JIWF"

    x_C = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24',
           '@11-30', '12-01', '12-02', '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11']
    y_C = [0.632447, 0.582177, 0.670682, 0.701664, 0.712600, 0.756320, 0.763604, 0.773809, 0.778139,
                     0.790539, 0.797142, 0.804689, 0.798197, 0.795916, 0.803630, 0.808965, 0.705377, 0.685749]

    x_J = ['@11-16', '@11-20', '@11-30', '@12-04', '@12-10']
    y_J = [0.486080, 0.523141, 0.538398, 0.533674, 0.489852]
    x_P = ['@11-16', '@11-20', '@11-30', '@12-04']
    y_P = [0.492106, 0.517342, 0.494489, 0.479734]
    x_T = ['@11-16', '@11-20', '@11-30', '@12-04', '@12-10']
    y_T = [0.105441, 0.109627, 0.115682, 0.116129, 0.106600]

    #*x_C_short is collected from x_C to compare gap.

    x_C_short = ['@11-16', '@11-20', '@11-30', '@12-04', '@12-10']
    y_C_short_dataStore = [0.670682, 0.763604,  0.790539,  0.795916,  0.705377]

    set_Charlie_scatter_and_rotation()
    drawPicture(titleString)

def draw_Pat_JIWF() :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Pat JIWF"

    x_P = ['11-12', '@11-12strt', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24',
           '11-30', '12-01', '12-02', '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_P = [0.510498, 0.503068, 0.604256, 0.615644, 0.632779, 0.668068, 0.693734, 0.717161,0.756917,
           0.796259, 0.804932, 0.822046, 0.829912, 0.838054, 0.833640, 0.836465, 0.831184, 0.820886, 0.831616]
    x_J = ['@11-12start', '@11-18', '@11-24', '@12-04', '@12-11']
    y_J = [0.456029, 0.489852, 0.522277, 0.541147, 0.539731]
    x_C = ['@11-12start', '@11-18', '@11-24', '@12-04', '@12-11']
    y_C = [0.540093, 0.591994, 0.565347, 0.572104, 0.562676]
    x_T = ['@11-12start', '@11-18', '@11-24', '@12-04', '@12-11']
    y_T = [0.147636, 0.174581, 0.200509, 0.214636, 0.221010]


    set_Pat_scatter_and_rotation()
    drawPicture(titleString)

def draw_Terry_JIWF() :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Terry JIWF"

    x_T = ['11-12', '11-12strt', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24',
           '11-30', '@12-01', '12-02', '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11']
    y_T = [0.406384918, 0.353164019, 0.424189535, 0.423801134, 0.409321505, 0.475386497, 0.499422645,0.557956231,
           0.584171094, 0.610956533, 0.641366434, 0.616914049, 0.653736433, 0.665332686, 0.678743448, 0.665909419,
           0.660516767, 0.663782581, 0.659092027]
    x_C = ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07']
    y_C = [0.260631, 0.273086, 0.403832, 0.413554, 0.391545]
    x_J = ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07']
    y_J = [0.256593, 0.308625, 0.341324, 0.349416, 0.331429]
    x_P = ['@11-19', '@11-23', '@12-01', '@12-03', '@12-07']
    y_P = [0.230738, 0.313590, 0.309866, 0.323403, 0.304127]

    set_Terry_scatter_and_rotation()
    drawPicture(titleString)
#==========================================
# draw non-normalized Jaccard Index for 4
#==========================================
def draw_4_JIWF():
    draw_Charlie_JIWF()
    draw_Jo_JIWF()
    draw_Pat_JIWF()
    draw_Terry_JIWF()

def testSubplot():
    '''
    x = np.linspace(0, 1, 100)
    y = 2 * x + 1
    plt.plot(x, y, '-r', label='y=2x+1')
    plt.title('Graph of y=2x+1')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.legend(loc='upper left')
    plt.show()

    '''
    x_C =['a','b','c', 'd']
    y_C = [0.2, 0.6, 0.4, 0.35]






    fig, axes = plt.subplots(nrows=2, ncols=1)
    plt.subplots_adjust(left=0.1, bottom=0.21, right=0.94, top=0.95, wspace=0.2, hspace=0.5)
    #l, b, w, h =  axes[0].get_position().bounds

    #*CB.ax.set_position([ll, b + 0.1 * h, ww, h * 0.8])

   # axes[0].set_position([l,b*0.8,w,h*0.8], 'both')
    f1 = plt.plot(ax=axes[0], label='s1')
   # l1 = axes[0].axhline(0.5, color='black', ls='--')

    axes[0].scatter(x_C, y_C, label='Charlie', marker='*')
    TitleString = {'Charlie', 'JIWF'}
    axes[0].set_title(TitleString)

    axes[0].set_xlabel('Daily Image')
    axes[0].set_ylabel('JIWF')


    #l1.set_label('l1')

    axes[0].legend(loc='best')

    x_L = ['c', 'c']
    y_L= [0.4, 0.55]
    line = Line2D(x_L, y_L, lw=2, color='black', axes=axes[0])



    uni_char = u"✹"
    t = text.Text('c', 0.5, '  <==  Gap', ha='left', va='bottom', axes=axes[0])

    axes[0].add_artist(t)

    axes[0].add_line(line)



    ####
    x_C = ['a', 'b', 'c', 'd']
    y_C = [0.6, 0.3, 0.2, 0.5]

    f2 = plt.plot(ax=axes[1], label='s2')


    axes[1].scatter(x_C, y_C, label='Pat', marker='+')


    axes[1].legend(loc='best')

    TitleString = 'Pat'
    axes[1].set_title(TitleString)

    axes[1].set_xlabel('Daily Image')
    axes[1].set_ylabel('JIWF')

    l, b, w, h = axes[1].get_position().bounds

    # *CB.ax.set_position([ll, b + 0.1 * h, ww, h * 0.8])

   # axes[1].set_position([l, b * 0.8, w, h * 0.8], 'both')
    plt.show()

# =====================
#   main()
# ---------------------
def main():
    global ax1

    testSubplot()

    #print("draw_4_JIWF()")
    #draw_4_JIWF()



##############  SET UP AREA ###########
if __name__ == '__main__':
    print("main called")

    WorkingDir = "C:/Research/IFIP/matplotResult/"

    main()

