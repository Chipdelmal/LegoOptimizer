
from os import path
from sys import argv
from termcolor import colored
from compress_pickle import dump, load
import constants as cst
import functions as fun


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
values = cst.LARGE_FIRST_BLOCK_VALUES
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 6, 4, 3, 5, 6]*100
VERBOSE = True
###############################################################################
# Load data
###############################################################################
pklFName=path.join(fPath, fName.split('.png')[0])+'.pkl'
pDict = load(pklFName)
###############################################################################
# Solve Multiple-Knapsack for every color
# -----------------------------------------------------------------------------
#   solution: {colorIndex: {gapIndex: blocks combination}}
###############################################################################
solution = {}
colorsNum = len(pDict['runLengthVectors'])
for colorIx in range(colorsNum):
    if VERBOSE:
        cHex = fun.rgbToHex(pDict['colorDeMapper'][colorIx])
        print(
            colored(
                f"+ Solved for #{cHex} ({(colorIx+1):03d}/{colorsNum:03d})", 
                'blue'
            ), 
            end = ' '
        )
    # Solve entry -------------------------------------------------------------
    gaps = pDict['runLengthVectors'][colorIx]
    solution[colorIx] = fun.solveColor(
        gaps, blocks, values=values, verbose=VERBOSE
    )
###############################################################################
# Export solution
###############################################################################
pklFName = path.join(fPath, fName.split('.png')[0])+'_Solved.pkl'
dump(pDict, pklFName)