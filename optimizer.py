
from os import path
from sys import argv
from termcolor import colored
from compress_pickle import dump, load
import functions as fun
import settings as sel


if fun.isNotebook():
    (fPath, fName) = (
        '/Users/sanchez.hmsc/Documents/SyncMega/LegoOptimizer/', 
        'megaman.png'
    )
else:
    (fPath, fName) = (argv[1], argv[2])
###############################################################################
# Get user selections from file
###############################################################################
(VALUES, BLOCKS, PALETTE, VERBOSE) = (
    sel.USER_SEL['priority'], sel.USER_SEL['blocks'],
    sel.USER_SEL['palette'], sel.USER_SEL['verbose']
)
###############################################################################
# Check if the palette provides blocks quantities
###############################################################################
if any([isinstance(PALETTE, t) for t in (int, tuple, list)]):
    BLK_QTY = False
else:
    BLK_QTY = True
###############################################################################
# Load data
###############################################################################
pklFName = path.join(fPath, fName.split('.png')[0])+'.pkl'
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
        print(colored(
                f"+ Solved for #{cHex} ({(colorIx):03d}/{colorsNum-1:03d})", 
                'blue'
            ), end = ' ')
    # Solve entry -------------------------------------------------------------
    gaps = pDict['runLengthVectors'][colorIx]
    solution[colorIx] = fun.solveColor(
        gaps, BLOCKS, values=VALUES, verbose=VERBOSE
    )
###############################################################################
# Export solution
###############################################################################
pklFName = path.join(fPath, fName.split('.png')[0])+'_Solved.pkl'
dump(solution, pklFName)