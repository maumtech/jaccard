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


import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib as mpl

def testdraw():

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_zorder(1000)
    ax.patch.set_alpha(0.5)
    ax.patch.set_color('r')

    ax2 = fig.add_subplot(111)
    ax2.plot(range(10), range(10))

    fig.savefig('twoHardWithSectors.png', bbox_inches='tight')
    plt.show()

def testdraw1():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    from PIL import Image
    global WorkingDir

    picture ='x.jpg'
    picFile = WorkingDir + picture
    im = np.array(Image.open(picFile), dtype=np.uint8)

    # Create figure and axes
    fig, ax = plt.subplots(1)
    plt.axis("off")
    # Display the image


    # Create a Rectangle patch
    rect = patches.Rectangle((50, 100), 40, 30, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rect)

    bbox_inches = 'tight'
    ax.imshow(im)
    picture = 'twoHardWithSectors.png'
    savepicFile = WorkingDir + picture

    fig.savefig(savepicFile, bbox_inches=0)

def drawRectanle():
    from matplotlib import pyplot as plt
    from matplotlib.patches import Rectangle
    plt.axis('off')

    someX, someY = 0.5, 0.5
    fig, ax = plt.subplots()
    plt.axis("off")
    currentAxis = plt.gca()
    #currentAxis.add_patch(Rectangle((someX - 0.1, someY - 0.1), 0.2, 0.2, fill=None, alpha=1, facecolor='none'))
    ax.add_patch(Rectangle((someX - 0.1, someY - 0.1), 0.2, 0.2, fill=None, alpha = 1, facecolor = 'none'))

    plt.show()

def drawEllipse():
    mean = [ 19.92977907 ,  5.07380955]
    width = 30
    height = 1.01828848
    angle = 0
    ell = mpl.patches.Ellipse(xy=mean, width=width, height=height, angle = 180+angle)
    fig, ax = plt.subplots()
    plt.axis("off")

    ax.add_patch(ell)
    ax.set_aspect('equal')
    ax.autoscale()
    plt.show()

def drawCircle():
    global WorkingDir
    plt.style.use('grayscale')
    plt.axis("off")
    circle1 = plt.Circle((0, 0), 0.2)
    circle2 = plt.Circle((0.5, 0.5), 0.2)
    #circle3 = plt.Circle((1, 1), 0.2, color='g', clip_on=False)

    fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
    # (or if you have an existing figure)
    # fig = plt.gcf()
    # ax = fig.gca()

    ax.add_artist(circle1)
    ax.add_artist(circle2)
    #ax.add_artist(circle3)

    fig.savefig('twoHardWithSectors.png', bbox_inches='tight')
    plt.show()


# =====================
#   main()
# ---------------------
def main():
    global ax1

    #print("draw_4_JIWF()")
    drawCircle()
    drawEllipse()
    drawRectanle()
    testdraw1()
    testdraw()

##############  SET UP AREA ###########
if __name__ == '__main__':
    print("main called")

    WorkingDir = "C:/Research/IFIP/matplotResult/"

    main()
