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
        ax1.set_ylabel('JINF', fontdict=labelFont)

    legend_properties = {'weight': 'normal'}
    #leg = ax1.get_legend()
    if xLabelPrint and not yLabelPrint: # Terry
        ax1.legend(loc=2, prop={"size":8})

    #plt.legend(prop=legend_properties)
    # plt.legend(loc='best')

# =============================================
# draw_Charlie_JINF()
# ---------------------
def draw_Jo_JINF(ax, xLabel, yLabel):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Jo JINF"

    x_C = [
        '@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new',
        '11-20-old', '@11-23', '11-24',  '11-30', '12-01', '12-02', '12-03',
        '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001', '@12-11-002'
        ]
    y_C = [
        0.377420551568, 0.355001425384, 0.380498302742, 0.396542196859, 0.407381034588, 0.392766138673, 0.289233500825,
        0.383980503281, 0.307230605987, 0.332402190805, 0.320339747761, 0.316860711744, 0.318173688958, 0.299922663701,
        0.293299190978, 0.28080955675, 0.284292717933, 0.277388123169, 0.257880246572, 0.241105755804, 0.24037328667 ]

    x_J = ['@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new',
           '11-20-old', '@11-23', '11-24', '11-30',  '12-01', '12-02', '12-03',
           '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001', '@12-11-002' ]
    y_J = [ 0.360448641188, 0.340995707189, 0.37671072589, 0.376302823793, 0.395131125392, 0.395916610751, 0.347103198095,
        0.442366335853, 0.388765891902, 0.465606548303, 0.559227928252, 0.563934968181, 0.572423123995, 0.583597254437,
        0.574024789344, 0.554712322212, 0.564093131333, 0.538854867619, 0.526265387399, 0.513837654204, 0.510519148928,
       ]

    x_P = ['@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new', '11-20-old', '@11-23', '11-24', '11-30',
     '12-01', '12-02', '12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001', '@12-11-002' ]
    y_P = [0.301848150022, 0.286662148204, 0.314523589646, 0.318482817639, 0.321017158017, 0.320771362019, 0.253961036822,
     0.332375229263, 0.279710096461, 0.258491537261, 0.283873317944, 0.279360323974, 0.277768592553, 0.288497692785,
     0.274557543538, 0.27490944592, 0.27915262863, 0.273940615099, 0.263210559817, 0.245792549552, 0.244828364498 ]


    x_T = ['@11-12', '11-12start', '11-16', '@11-17', '11-18', '11-19', '11-20-new', '11-20-old', '@11-23', '11-24', '11-30',
     '12-01', '12-02', '12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001', '@12-11-002']
    y_T = [0.0969110350295, 0.0912665761341, 0.0966991673189, 0.0981208016607, 0.0960556597907, 0.0969399819426,
     0.0941607361611, 0.108856090325, 0.0953450084393, 0.093071108937, 0.10625804589, 0.107582507789, 0.108211867199,
     0.106580903011, 0.107397111318, 0.109327062021, 0.109950438177, 0.10817538707, 0.108876366437, 0.104325464205,
     0.103893966597 ]

    addText(ax, '11-16', 0.8, '(b)')
    set_Jo_scatter(ax)

    drawPicture(titleString, ax, xLabel, yLabel)

# =============================================
# draw_Charlie_JINF()
# ---------------------
def draw_Charlie_JINF(ax, xLabel, yLabel):
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Charlie JINF"

    x_C = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24', '@11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11']
    y_C = [0.47226140731, 0.4223413257, 0.503406981546, 0.546694415323, 0.569657820051, 0.626371550564, 0.626517574556,
     0.638745551718, 0.647707557242, 0.644962411615, 0.655268281899, 0.658436722593, 0.643846052709, 0.630111848389,
     0.637966643286, 0.629178228792, 0.535650607859, 0.535800310221 ]

    x_J = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24', '@11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11']
    y_J = [
        0.320026496421, 0.301498097557, 0.324581308602, 0.324223787908, 0.330219130962, 0.356970338142, 0.350400424618,
        0.330756078179, 0.334281243839, 0.330995807984, 0.328696376248, 0.332890402874, 0.325836383748, 0.317184823958,
        0.311680884329, 0.315436999039, 0.306833972545, 0.306413706382 ]

    x_P = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24', '@11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11']
    y_P = [
        0.295186597757, 0.27858813884, 0.311661832984, 0.309590759607, 0.310045230538, 0.308490538781, 0.312008905418,
        0.300414680184, 0.292461953639, 0.286864835253, 0.284707841241, 0.285763320922, 0.297751084142, 0.288360601951,
        0.291170619062, 0.288147138039, 0.272635737444, 0.272288778052 ]

    x_T = ['11-12', '11-12start', '@11-16', '11-17', '11-18', '11-19', '@11-20', '11-23', '11-24', '@11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-09', '@12-10', '12-11']
    y_T = [0.0971023975725, 0.0904907630431, 0.0967026564689, 0.0985701677388, 0.0985766282048, 0.0987966829297,
     0.0974303083147, 0.0967085795676, 0.0965332462033, 0.0992846552623, 0.0996868240577, 0.100648113183,
     0.098957412428, 0.0978965749416, 0.099273317005, 0.0993886341748, 0.0964809264373, 0.0964179718493]



    addText(ax, '@11-16', 0.8, '(a)')
    set_Charlie_scatter(ax)
    drawPicture(titleString, ax,  xLabel, yLabel)

def addText(ax, xPos, yPos, textString):
    txt = text.Text(xPos, yPos, textString, ha='left', va='bottom', fontsize=10, axes=ax)
    ax.add_artist(txt)


def drawGapLine(ax):
    x_L = [13, 13]
    y_L = [0.32,  0.65]
    gapLine = Line2D(x_L, y_L, lw=2, color='black', axes=ax)
    gapText = text.Text('@12-04', 0.5, '  <-- Gap', ha='left', va='bottom', fontsize=6, axes=ax)

    ax.add_artist(gapText)
    ax.add_line(gapLine)


def draw_Pat_JINF_wit_Gap(ax, xLabel, yLabel) :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Pat JINF"

    x_C = ['11-12', '@11-12start', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24', '11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_C = [ 0.361459074845, 0.340038943977, 0.359525474472, 0.371681893876, 0.374078750556, 0.356492438739, 0.337970421221,
        0.316712925409, 0.303714556974, 0.285383364395, 0.280052361225, 0.286632854388, 0.28127533172, 0.27950167768,
        0.265175079071, 0.25886620041, 0.267956611253, 0.253918037352, 0.253835839023 ]

    x_J = ['11-12', '@11-12start', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24', '11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_J = [ 0.320892337663, 0.303745180336, 0.320966400752, 0.320808352516, 0.324577576273, 0.349744047238, 0.337686484883,
        0.313722296333, 0.301957642205, 0.291487752757, 0.285140439031, 0.29487657237, 0.289806801346, 0.28776149701,
        0.273240834554, 0.268423700951, 0.280026155673, 0.271408828562, 0.271399058476 ]

    x_P = ['11-12', '@11-12start', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24', '11-30', '12-01',
           '12-02', '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_P = [0.368208458546, 0.348987090186, 0.468831302521, 0.476082765217, 0.49547737661, 0.551574196848, 0.578530708412,
           0.614924372735, 0.657410169231, 0.683750600664, 0.679268108726, 0.697988573101, 0.696230551213, 0.691317267342,
           0.675420377796, 0.651725235313, 0.650334388957, 0.63359968743, 0.631238613422]

    x_T = ['11-12', '@11-12start', '11-16', '11-17', '@11-18', '11-19', '11-20', '11-23', '@11-24', '11-30', '12-01', '12-02',
     '12-03', '@12-04', '12-07', '12-08', '12-09', '12-10', '@12-11']
    y_T = [ 0.0973868106889, 0.0914631339137, 0.0961269923547, 0.0980892316585, 0.0979693400859, 0.109802150382,
     0.109764831726, 0.107852684515, 0.10608759013, 0.107104039925, 0.106913057367, 0.108626822757, 0.108865037294,
     0.10906644133, 0.110088129853, 0.10893313875, 0.110961614607, 0.109661903325, 0.1096222989 ]

    addText(ax, '11-16', 0.8, '(c)')
    drawGapLine(ax)
    set_Pat_scatter(ax)
    drawPicture(titleString, ax, xLabel, yLabel)

def draw_Terry_JINF(ax, xLabel, yLabel) :
    global x_C, y_C, x_J, y_J, x_P, y_P, x_T, y_T

    titleString = "Terry JINF"

    x_C = ['11-12', '11-12start', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24', '11-30', '@12-01', '12-02',
     '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001']
    y_C = [ 0.140322074219, 0.110432633838, 0.131517651868, 0.134242395879, 0.137010296741, 0.0893246097587,
        0.0807882538258, 0.0942153028029, 0.0967808169246, 0.0888109963088, 0.0873644012839, 0.0866048441638,
        0.0842034627186, 0.0840670402225, 0.0808164539709, 0.0839790074876, 0.0849064821959, 0.0824864862531,
        0.0818219236164 ]

    x_J = ['11-12', '11-12start', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24', '11-30', '@12-01', '12-02',
     '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001']
    y_J = [ 0.126104896921, 0.0971666193073, 0.113690176802, 0.111738894176, 0.11932159636, 0.0947788626625, 0.107050897524,
        0.119296560192, 0.121295976415, 0.121048462733, 0.119925583972, 0.11965704884, 0.116209302132, 0.117668042039,
        0.108761421956, 0.108699754513, 0.100316319455, 0.100754079419, 0.101355135756 ]

    x_P = ['11-12', '11-12start', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24', '11-30', '@12-01', '12-02',
     '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001']
    y_P = [ 0.123864497741, 0.0966176117978, 0.127712089544, 0.125277455546, 0.12090920082, 0.088451405272, 0.105187109655,
        0.119325428362, 0.115933496043, 0.108353909317, 0.108053678863, 0.110654914949, 0.107085911364, 0.102596580257,
        0.0991277759336, 0.100117122462, 0.0931324721503, 0.0918124197486, 0.0918765432307 ]

    x_T = [ '11-12', '11-12start', '11-16', '11-17', '11-18', '@11-19', '11-20', '@11-23', '11-24', '11-30', '@12-01',
        '12-02', '@12-03', '12-04', '@12-07', '12-08', '12-09', '12-10', '12-11-001' ]
    y_T = [ 0.273859142866, 0.249071705883, 0.286550316572, 0.28299247045, 0.276143776549, 0.310806996514, 0.342008539799,
        0.376096350346, 0.403466302521, 0.463962362116, 0.464326570283, 0.468183489089, 0.473603678679, 0.477291732092,
        0.488679853353, 0.496992359566, 0.492537620639, 0.492321549245, 0.484517352939 ]

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



def draw_4_JINF():
    global WorkingDir
    #fig = plt.figure(figsize=(4, 6))

    plt.style.use('grayscale')
    fig, axes = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=True, figsize=(5, 12))

    adjustSubPlot()
    setMarkerValues()
    xLabel = False
    yLabel = True
    draw_Charlie_JINF(axes[0][0], xLabel, yLabel)
    xLabel = False
    yLabel = False
    draw_Jo_JINF(axes[0][1], xLabel, yLabel)
    xLabel = True
    yLabel = True
    #draw_Pat_JIWF(axes[1][0], xLabel, yLabel)
    draw_Pat_JINF_wit_Gap(axes[1][0], xLabel, yLabel)
    xLabel = True
    yLabel = False
    draw_Terry_JINF(axes[1][1], xLabel, yLabel)

    TitleString = "JINF_4_EMP"
    picFile = WorkingDir + TitleString + '.' + fileType
    # plt.savefig(picFile, bbox_inches="tight", pad_inches=2, dpi=600)
    fig.savefig(picFile, bbox_inches="tight", pad_inches=2, dpi=600, orientation='landscape')
    plt.show()



# =====================
#   main()
# ---------------------
def main():
    global ax1

    #print("draw_4_JINF() -- normalized JI")
    draw_4_JINF()



##############  SET UP AREA ###########
if __name__ == '__main__':
    print("main called")

    WorkingDir = "C:/Research/IFIP/matplotResult/"

    main()

