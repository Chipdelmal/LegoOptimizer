
from os import path
from time import time
from ortools.linear_solver import pywraplp
from compress_pickle import load
import constants as cst
import functions as fun

(fPath, fName) = ('./demo', 'DWN-Resurrect_32-rocketsPalette.png')
values = cst.LARGE_FIRST_BLOCK_VALUES
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 6, 4, 3, 5, 6]*100
###############################################################################
# Load data
###############################################################################
pklFName=path.join(fPath, fName.split('.png')[0])+'.pkl'
pDict = load(pklFName)
###############################################################################
# Solve Multiple-Knapsack
###############################################################################
ix = 7
gaps = pDict['runLengthVectors'][ix]
fun.solveColor(gaps, blocks, values=values, verbose=True)

###############################################################################
# Problem Setup and Solution
###############################################################################
tic = time.time()
data = fun.genSolverData(gaps, blocks, values=values)
# Setup problem ---------------------------------------------------------------
solver = pywraplp.Solver.CreateSolver('SCIP')
(x, solver) = fun.genSolverXVector(data, solver)
(x, solver) = fun.setSolverConstraints(data, x, solver)
(x, solver, objective) = fun.setSolverObjective(data, x, solver)
# Solve problem ---------------------------------------------------------------
status = solver.Solve()
# Timing ----------------------------------------------------------------------
toc = time.time()
runTime = (toc-tic)/60
###############################################################################
# Assemble and Export Solution
###############################################################################
fun.convertSolution(data, x, blocks)
