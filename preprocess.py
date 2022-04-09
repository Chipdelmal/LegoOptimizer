
import cv2
from math import ceil
import itertools
from os import path
from sys import argv

from compress_pickle import dump
from termcolor import colored
import functions as fun
import selections as sel

if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
VERBOSE = True
###############################################################################
# Load image
###############################################################################
img = cv2.imread(path.join(fPath, fName.split(".png")[0]+'_DWN.png'))
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
# Get run length (need to modularize, as it's duplicated in split encoding)
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
###############################################################################
# Terminal Summary
###############################################################################
pSums = {i: sum(pVectors[i]) for i in pVectors.keys()}
if VERBOSE:
    print(colored(f'+ Vector lengths: {pSums}', 'blue'))
###############################################################################
# Split longer entries (need to modularize)
###############################################################################
if sel.USER_SEL['lengthMax'] is not None:
    (colDict, colDeDict, scrambler) = fun.genScrambleDicts(
        pDict, threshold=sel.USER_SEL['lengthMax']
    )
    pixDict = fun.scramblePixDict(pixDict, scrambler)
    # Re-encode ---------------------------------------------------------------
    dictVals = sorted(fun.flatten(scrambler.values()))
    runL = [fun.runLength(i) for i in pixDict]
    # Get flattened vectors counts --------------------------------------------
    pVectors = {}
    for dix in dictVals:
        pValPerRow = [[c if i == dix else 0 for (c, i) in row] for row in runL]
        pValPerRow = [[c for (c, i) in row if i==dix] for row in runL]
        pValPerRow = fun.flatten(pValPerRow)
        pVectors[dix] = pValPerRow
    pLengths = {i: len(pVectors[i]) for i in pVectors.keys()}
    # Setup new dictionary ----------------------------------------------------
    pDict = {
        'colorMapper': colDict,
        'colorDeMapper': colDeDict,
        'imageMapped': pixDict,
        'runLengthVectors': pVectors,
        'runLengthLengths': pLengths
    }
    pklFName = path.join(fPath, fName.split('.png')[0])+'.pkl'
    dump(pDict, pklFName)
    # Terminal Summary --------------------------------------------------------
    pSums = {i: sum(pVectors[i]) for i in pVectors.keys()}
    if VERBOSE:
        print(colored(f'+ Split Vector lengths: {pSums}', 'blue'))