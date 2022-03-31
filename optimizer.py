
from os import path
from compress_pickle import dump, load
import constants as cst
import functions as fun


(fPath, fName) = ('./demo', 'DWN-Resurrect_32-rocketsPalette.png')
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
#   solution: Dictionary solution to the problem with 'timing' information and
#               combinations of blocks that solve each element of the 
#               run-length vector (index for the dictionary). Each entry is
#               a (timing, solution) pair for the gaps to be solved.
###############################################################################
solution = {}
for colorIx in range(len(pDict['runLengthVectors'])):
    gaps = pDict['runLengthVectors'][colorIx]
    solution[colorIx] = {
        colorIx: fun.solveColor(gaps, blocks, values=values, verbose=VERBOSE)
    }
###############################################################################
# Export solution
###############################################################################
pklFName = path.join(fPath, fName.split('.png')[0])+'_Solved.pkl'
dump(pDict, pklFName)