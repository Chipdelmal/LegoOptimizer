
import cv2
import time
import itertools
from os import path
from compress_pickle import dump
import functions as fun
import constants as cst

from datetime import datetime
from ortools.linear_solver import pywraplp


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
# Export vectors
###############################################################################
outDict = {
    'colorMapper': colDict,
    'colorDeMapper': colDeDict,
    'pixelsMapped': pixDict,
    'pVectors': pVectors,
    'pLengths': pLengths
}
pklFName = path.join(fPath, fName.split('.png')[0])+'.pkl'
dump(outDict, pklFName)

ix = 7
###############################################################################
# Problem Input
###############################################################################
(gaps, nel) = (pVectors[ix], pLengths[ix])
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 6, 4, 3, 5, 6]*100
values = cst.LARGER_FIRST_BLOCK_VALUES
data = fun.genSolverData(gaps, blocks, values=values)
###############################################################################
# Problem Setup
###############################################################################
tic = time.time()
solver = pywraplp.Solver.CreateSolver('SCIP')
(x, solver) = fun.genSolverXVector(data, solver)
(x, solver) = fun.setSolverConstraints(data, x, solver)
(x, solver, objective) = fun.setSolverObjective(data, x, solver)
status = solver.Solve()
toc = time.time()
print(f"Timing for {nel:2d} elements: {(toc-tic)/60:.2f} mins")
fun.convertSolution(data, x, blocks)
