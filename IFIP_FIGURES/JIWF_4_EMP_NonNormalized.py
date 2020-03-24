#!/usr/bin/env python

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

def set_Terry_scatter(ax1):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global terryMarker, charlieMarker, JoMarker, patMarker
    fig = plt.figure()

    # order is important
    ax1.scatter(x_T, y_T, label='Terry', marker=terryMarker, s=markerSize)
    ax1.scatter(x_P, y_P, label='Pat', marker=patMarker, s=markerSize)
    ax1.scatter(x_C, y_C, label='Charlie', marker=charlieMarker, s=markerSize)
    ax1.scatter(x_J, y_J, label='Jo', marker=joMarker, s=markerSize)

def set_Pat_scatter(ax1):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global terryMarker, charlieMarker, JoMarker, patMarker
    fig = plt.figure()

    # order is important
    ax1.scatter(x_P, y_P, label='Pat', marker=patMarker, s=markerSize)
    ax1.scatter(x_C, y_C, label='Charlie', marker=charlieMarker, s=markerSize)
    ax1.scatter(x_J, y_J, label='Jo', marker=joMarker, s=markerSize)
    ax1.scatter(x_T, y_T, label='Terry', marker=terryMarker, s=markerSize)

def set_Jo_scatter(ax1):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global terryMarker, charlieMarker, JoMarker, patMarker
    fig = plt.figure()

        # order is important
    ax1.scatter(x_J, y_J, label='Jo', marker=joMarker, s=markerSize)
    ax1.scatter(x_C, y_C, label='Charlie', marker=charlieMarker, s=markerSize)
    ax1.scatter(x_P, y_P, label='Pat', marker=patMarker, s=markerSize)
    ax1.scatter(x_T, y_T, label='Terry', marker=terryMarker, s=markerSize)


def set_Charlie_scatter(ax1):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T
    global terryMarker, charlieMarker, joMarker, patMarker
    global markerSize
    fig = plt.figure()

    # ax1.tick_params(axis='x', labelsize=2)


    # order is important
    ax1.scatter(x_C, y_C, label='Charlie', marker=charlieMarker, s=markerSize)
    ax1.scatter(x_J, y_J, label='Jo', marker=joMarker, s=markerSize)
    ax1.scatter(x_P, y_P, label='Pat', marker=patMarker, s=markerSize)
    ax1.scatter(x_T, y_T, label='Terry', marker=terryMarker, s=markerSize)

def set_rotation(ax1, angle):
   for label in ax1.xaxis.get_ticklabels():
       label.set_rotation(angle)

def set_tickFontSize(ax1, size):
   for tick in ax1.xaxis.get_major_ticks():
        tick.label.set_fontsize(size)

def drawPicture(TitleString, ax1, xLabelPrint,  yLabelPrint):
    labelFont = {'family': 'sans-serif',
            'color': 'black',
            'weight': 'normal',
            'size': 8,
            }
    titleFont = {'family': 'sans-serif',
             'color': 'black',
             'weight': 'bold',
             'size': 10,
             }

    angle = 44
    set_rotation(ax1, angle)
    set_tickFontSize(ax1, 5)
    ax1.set_title(TitleString,  fontdict=titleFont)
    if xLabelPrint:
        ax1.set_xlabel('Daily Image', fontdict=labelFont)
    if yLabelPrint:
        ax1.set_ylabel('JIWF', fontdict=labelFont)

    legend_properties = {'weight': 'normal'}
    #leg = ax1.get_legend()
    if xLabelPrint and yLabelPrint: # Pat
        ax1.legend(loc='best', prop={"size":8})

    #plt.legend(prop=legend_properties)
    # plt.legend(loc='best')

# =============================================
# draw_Charlie_JIWF()
# ---------------------
def draw_Jo_JIWF(ax, xLabel, yLabel):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Jo JIWF"

    x_C = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-2']
    y_C = [0.580209, 0.607690, 0.471818, 0.519579, 0.495694]
    x_J = ['@11-12', '11-12strt', '11-16', '@11-17', '11-18', '11-19', '11-20new', '11-20old', '@11-23',
           '11-24', '11-30', '12-01', '12-02', '12-03', '12-04', '@12-07', '12-08', '12-09',
           '12-10', '12-11-1', '@12-11-2']
    y_J = [0.510068, 0.466230, 0.508020, 0.530476, 0.530545, 0.533058, 0.470032, 0.590809, 0.508113, 0.589090,
           0.687056, 0.701606, 0.709529, 0.749305, 0.749830, 0.763826, 0.760515, 0.752596, 0.747283, 0.754391, 0.768874]

    x_P = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-2']
    y_P = [0.477766, 0.501286, 0.418116, 0.459298, 0.448496]
    x_T = ['@11-12', '@11-17', '@11-23', '@12-07', '@12-11-2']
    y_T = [0.160137, 0.170565, 0.156133, 0.209922, 0.207862]

    addText(ax, '11-16', 0.8, '(b)')
    set_Jo_scatter(ax)

    drawPicture(titleString, ax, xLabel, yLabel)

# =============================================
# draw_Charlie_JIWF()
# ---------------------
def draw_Charlie_JIWF(ax, xLabel, yLabel):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Charlie JIWF"

    x_C = ['11-12', '11-12strt', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24',
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

    addText(ax, '@11-16', 0.8, '(a)')
    set_Charlie_scatter(ax)
    drawPicture(titleString, ax,  xLabel, yLabel)

def addText(ax, xPos, yPos, textString):
    txt = text.Text(xPos, yPos, textString, ha='left', va='bottom', fontsize=10, axes=ax)
    ax.add_artist(txt)


def drawGapLine(ax):
    x_L = [13, 13]
    y_L = [0.6,  0.8]
    gapLine = Line2D(x_L, y_L, lw=2, color='black', axes=ax)
    gapText = text.Text('@12-04', 0.7, '  <-- Gap', ha='left', va='bottom', fontsize=6, axes=ax)

    ax.add_artist(gapText)
    ax.add_line(gapLine)


def draw_Pat_JIWF_wit_Gap(ax, xLabel, yLabel) :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Pat JIWF"

    x_P = ['11-12', '@11-12strt', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24',
           '11-30', '12-01', '12-02', '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_P = [0.510498, 0.503068, 0.604256, 0.615644, 0.632779, 0.668068, 0.693734, 0.717161,0.756917,
           0.796259, 0.804932, 0.822046, 0.829912, 0.838054, 0.833640, 0.836465, 0.831184, 0.820886, 0.831616]
    x_J = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_J = [0.456029, 0.489852, 0.522277, 0.541147, 0.539731]
    x_C = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_C = [0.540093, 0.591994, 0.565347, 0.572104, 0.562676]
    x_T = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_T = [0.147636, 0.174581, 0.200509, 0.214636, 0.221010]

    addText(ax, '11-16', 0.8, '(c)')
    drawGapLine(ax)
    set_Pat_scatter(ax)
    drawPicture(titleString, ax, xLabel, yLabel)




def draw_Pat_JIWF(ax, xLabel, yLabel) :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Pat JIWF"

    x_P = ['11-12', '@11-12strt', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24',
           '11-30', '12-01', '12-02', '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_P = [0.510498, 0.503068, 0.604256, 0.615644, 0.632779, 0.668068, 0.693734, 0.717161,0.756917,
           0.796259, 0.804932, 0.822046, 0.829912, 0.838054, 0.833640, 0.836465, 0.831184, 0.820886, 0.831616]
    x_J = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_J = [0.456029, 0.489852, 0.522277, 0.541147, 0.539731]
    x_C = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_C = [0.540093, 0.591994, 0.565347, 0.572104, 0.562676]
    x_T = ['@11-12strt', '@11-18', '@11-24', '@12-04', '@12-11']
    y_T = [0.147636, 0.174581, 0.200509, 0.214636, 0.221010]


    set_Pat_scatter(ax)
    drawPicture(titleString, ax, xLabel, yLabel)

def draw_Terry_JIWF(ax, xLabel, yLabel) :
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

    addText(ax, '11-16', 0.8, '(d)')
    set_Terry_scatter(ax)
    drawPicture(titleString, ax, xLabel, yLabel)

#==========================================
def adjustSubPlot():
    plt.subplots_adjust(left=0.125, bottom=0.21, right=0.8, top=0.95, wspace=0.1, hspace=.3)


#==========================================


def setMarkerValues():
    global terryMarker, charlieMarker, joMarker, patMarker
    global markerSize
    markerSize = 4
    charlieMarker = '*'
    terryMarker = 's'
    joMarker = 'd'
    patMarker = '^'



def draw_4_JIWF():
    global WorkingDir
    #fig = plt.figure(figsize=(4, 6))

    plt.style.use('grayscale')
    fig, axes = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=True, figsize=(5, 12))

    adjustSubPlot()
    setMarkerValues()
    xLabel = False
    yLabel = True
    draw_Charlie_JIWF(axes[0][0], xLabel, yLabel)
    xLabel = False
    yLabel = False
    draw_Jo_JIWF(axes[0][1], xLabel, yLabel)
    xLabel = True
    yLabel = True
    #draw_Pat_JIWF(axes[1][0], xLabel, yLabel)
    draw_Pat_JIWF_wit_Gap(axes[1][0], xLabel, yLabel)
    xLabel = True
    yLabel = False
    draw_Terry_JIWF(axes[1][1], xLabel, yLabel)

    TitleString = "JIWF_4_EMP"
    picFile = WorkingDir + TitleString + '.' + fileType
    # plt.savefig(picFile, bbox_inches="tight", pad_inches=2, dpi=600)
    fig.savefig(picFile, bbox_inches="tight", pad_inches=2, dpi=600, orientation='landscape')
    plt.show()



# =====================
#   main()
# ---------------------
def main():
    global ax1

    #print("draw_4_JIWF()")
    draw_4_JIWF()



##############  SET UP AREA ###########
if __name__ == '__main__':
    print("main called")

    WorkingDir = "C:/Research/IFIP/matplotResult/"

    main()

