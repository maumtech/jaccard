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

import matplotlib.text as text


import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Ellipse
from matplotlib.patches import Rectangle
from PIL import Image

fileType = 'eps'
def addText(ax, xPos, yPos, textString, normalFont):
    if ('DISK' not in textString) :
        size = 18
    else:
        size = 25

    if ( normalFont == True) :
        weight = 'normal'
    else :
        weight = 'bold'
    txt = text.Text(xPos, yPos, textString, ha='left', va='bottom', fontweight=weight, fontsize=size, axes=ax)
    ax.add_artist(txt)

xDisk1 = 70
yDisk1 = 55
xDisk2 = 349
yDisk2 = yDisk1
xPos1 = 50
xPos2 = 160
xPos3 = 320
xPos4 = 445
yPos1 = 104
yPos2 = 140
yPos3 = 177
yPos4 = 213
yPos5 = 249
def drawTwoHardwith3CommonSectors():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from PIL import Image
    global WorkingDir


   # picture ='x.jpg'
    picture = '2disk.png'
    picFile = WorkingDir + picture
    im = np.array(Image.open(picFile), dtype=np.uint8)

    # Create figure and axes
    fig, ax = plt.subplots(1)
    #ax.set(xlim=[0, 1], ylim=[0, 1], aspect='equal')
    plt.axis("off")
    # Display the image

    textString = 'DISK A'
    addText(ax, xDisk1, yDisk1, textString, False)

    textString = 'AAA'
    addText(ax, xPos1, yPos1, textString, True)

    textString = 'FFF'
    addText(ax, xPos1, yPos2, textString, False)

    textString = 'CCC'
    addText(ax, xPos1, yPos3, textString, True)

    textString = 'GGG'
    addText(ax, xPos1, yPos4, textString, False)

    textString = 'JJJ'
    addText(ax, xPos1, yPos5, textString, True)

    textString = 'HHH'
    addText(ax, xPos2, yPos1, textString, True)

    textString = 'KKK'
    addText(ax, xPos2, yPos2, textString, True)

    textString = 'TTT'
    addText(ax, xPos2, yPos3, textString, True)

    textString = 'OOO'
    addText(ax, xPos2, yPos4, textString, False)

    textString = 'LLL'
    addText(ax, xPos2, yPos5, textString, True)

    #### Disk B ###########
    textString = 'DISK B'
    addText(ax, xDisk2, yDisk1, textString, False)

    textString = 'XYZ'
    addText(ax, xPos3, yPos1, textString, True)

    textString = 'OOO'
    addText(ax, xPos3, yPos2, textString, False)

    textString = 'ABC'
    addText(ax, xPos3, yPos3, textString, True)

    textString = 'FFF'
    addText(ax, xPos3, yPos4, textString, False)

    textString = 'AKL'
    addText(ax, xPos3, yPos5, textString, True)

    textString = 'GGG'
    addText(ax, xPos4, yPos1, textString, False)

    textString = 'KLA'
    addText(ax, xPos4, yPos2, textString, True)

    textString = 'IOT'
    addText(ax, xPos4, yPos3, textString, True)

    textString = 'OXO'
    addText(ax, xPos4, yPos4, textString, True)

    textString = 'LAX'
    addText(ax, xPos4, yPos5, textString, True)
    # Create a Rectangle patch
    #rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    #ax.add_patch(rect)



    bbox_inches = 'tight'
    ax.imshow(im)
    picture = 'twoHardWith3CommonSectors.eps'
    savepicFile = WorkingDir + picture
    plt.show()
    fig.savefig(savepicFile, bbox_inches=0)

def drawTwoHardwith3CommonNullSpaceSectors():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from PIL import Image
    global WorkingDir


   # picture ='x.jpg'
    picture = '2disk.png'
    picFile = WorkingDir + picture
    im = np.array(Image.open(picFile), dtype=np.uint8)

    # Create figure and axes
    fig, ax = plt.subplots(1)
    #ax.set(xlim=[0, 1], ylim=[0, 1], aspect='equal')
    plt.axis("off")
    # Display the image

    textString = 'DISK A'
    addText(ax, xDisk1, yDisk1, textString, False)

    textString = 'NUL'
    addText(ax, xPos1, yPos1, textString, True)

    textString = 'FFF'
    addText(ax, xPos1, yPos2, textString, False)

    textString = 'NUL'
    addText(ax, xPos1, yPos3, textString, True)

    textString = 'GGG'
    addText(ax, xPos1, yPos4, textString, False)

    textString = 'NUL'
    addText(ax, xPos1, yPos5, textString, True)

    textString = 'NUL'
    addText(ax, xPos2, yPos1, textString, True)

    textString = 'NUL'
    addText(ax, xPos2, yPos2, textString, True)

    textString = 'NUL'
    addText(ax, xPos2, yPos3, textString, True)

    textString = 'OOO'
    addText(ax, xPos2, yPos4, textString, False)

    textString = 'NUL'
    addText(ax, xPos2, yPos5, textString, True)

    #### Disk B ###########
    textString = 'DISK B'
    addText(ax, xDisk2, yDisk1, textString, False)

    textString = 'SPA'
    addText(ax, xPos3, yPos1, textString, True)

    textString = 'OOO'
    addText(ax, xPos3, yPos2, textString, False)

    textString = 'SPA'
    addText(ax, xPos3, yPos3, textString, True)

    textString = 'FFF'
    addText(ax, xPos3, yPos4, textString, False)

    textString = 'SPA'
    addText(ax, xPos3, yPos5, textString, True)

    textString = 'GGG'
    addText(ax, xPos4, yPos1, textString, False)

    textString = 'SPA'
    addText(ax, xPos4, yPos2, textString, True)

    textString = 'SPA'
    addText(ax, xPos4, yPos3, textString, True)

    textString = 'SPA'
    addText(ax, xPos4, yPos4, textString, True)

    textString = 'SPA'
    addText(ax, xPos4, yPos5, textString, True)
    # Create a Rectangle patch
    #rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    #ax.add_patch(rect)



    bbox_inches = 'tight'
    ax.imshow(im)
    picture = 'twoHardWithNullSpaceSectors.eps'
    savepicFile = WorkingDir + picture
    plt.show()
    fig.savefig(savepicFile, bbox_inches=0)


# =====================
#   main()
# ---------------------
def main():
    #test2()

    drawTwoHardwith3CommonNullSpaceSectors()
    #drawTwoHardwith3CommonSectors()
    '''  
    # Create figure and axes
    fig, ax = plt.subplots(1)
    plt.axis("off")
    # Display the image

    plt.style.use('grayscale')

    #print("draw_4_JIWF()")
    drawCircle(ax)
    drawEllipse(ax)
    drawRectanle(ax)
   # testdraw1(ax)
   # testdraw(ax)

    picture = 'twoHardWithSectors'
    picFile = WorkingDir + picture + '.eps'
    fig.savefig(picFile, bbox_inches='tight')
    plt.show()
    '''
##############  SET UP AREA ###########
if __name__ == '__main__':
    print("main called")

    WorkingDir = "C:/Research/IFIP/matplotResult/"

    main()
