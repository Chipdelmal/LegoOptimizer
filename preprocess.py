
import cv2
import itertools
import functions as fun
from os import path

(fPath, fName) = ('./demo', 'DWN-Resurrect_32-rocketsPalette.png')
###############################################################################
# Load image
###############################################################################
img = cv2.imread(path.join(fPath, fName))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
###############################################################################
# Process image for colors
###############################################################################
pixs = tuple([tuple([tuple(i) for i in row]) for row in img])
colPal = list(set(list(itertools.chain(*pixs))))
###############################################################################
# Change colors into keys
###############################################################################
colDict = {col: ix for (ix, col) in enumerate(colPal)}
pixDict = tuple([tuple([colDict[i] for i in row]) for row in pixs])
###############################################################################
# Get run length
###############################################################################
dictVals = list(colDict.values())
runL = [fun.runLength(i) for i in pixDict]
# Get flattened vectors counts ------------------------------------------------
pVectors = {}
for dix in dictVals:
    pValPerRow = [[c for (c, i) in row if i == dix] for row in runL]
    pVector = fun.flatten(pValPerRow)
    pVectors[dix] = pVector
pVectors
###############################################################################
# Export vectors
###############################################################################
