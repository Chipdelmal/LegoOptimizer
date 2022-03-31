
import cv2
import itertools
from os import path
from sys import argv
from compress_pickle import dump
import functions as fun
import constants as cst


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
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
colDeDict = {ix: col for (ix, col) in enumerate(colPal)}
pixDict = tuple([tuple([colDict[i] for i in row]) for row in pixs])
###############################################################################
# Get run length
###############################################################################
dictVals = list(colDict.values())
runL = [fun.runLength(i) for i in pixDict]
# Get flattened vectors counts ------------------------------------------------
pVectors = {}
for dix in dictVals:
    pValPerRow = [[c if i == dix else 0 for (c, i) in row] for row in runL]
    pValPerRow = [[c for (c, i) in row if i==dix] for row in runL]
    pValPerRow = fun.flatten(pValPerRow)
    pVectors[dix] = pValPerRow
pLengths = {i: len(pVectors[i]) for i in pVectors.keys()}
###############################################################################
# Assemble and export vectors
# -----------------------------------------------------------------------------
#   colorMapper: RGB tuple to color-index mapper dictionary
#   colorDeMapper: Color-index to RGB mapper dictionary
#   imageMapped: Color-index pixel representation of the original image
#   runLengthVectors: Run-length encoded vectors by color
#   runLengthLengths: Run-length lengths per color
###############################################################################
pDict = {
    'colorMapper': colDict,
    'colorDeMapper': colDeDict,
    'imageMapped': pixDict,
    'runLengthVectors': pVectors,
    'runLengthLengths': pLengths
}
pklFName = path.join(fPath, fName.split('.png')[0])+'.pkl'
dump(pDict, pklFName)
