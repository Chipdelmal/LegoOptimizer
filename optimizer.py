
from time import time
from ortools.linear_solver import pywraplp
import constants as cst
import functions as fun

###############################################################################
# Problem Input
###############################################################################
gaps = [4, 2, 6, 3]
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 5, 6, 4, 3, 5, 6]
values = cst.DEFAULT_BLOCK_VALUES
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
