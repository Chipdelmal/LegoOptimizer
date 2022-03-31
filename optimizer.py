
import constants as cst
from ortools.linear_solver import pywraplp
import functions as fun

###############################################################################
# Problem Input
###############################################################################
gaps = [4, 2, 6, 3]
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
values = cst.DEFAULT_BLOCK_VALUES
data = fun.genSolverData(gaps, blocks, values=values)
###############################################################################
# Problem Setup
###############################################################################
solver = pywraplp.Solver.CreateSolver('SCIP')
(x, solver) = fun.genSolverXVector(data, solver)
(x, solver) = fun.setSolverConstraints(data, x, solver)
(x, solver, objective) = fun.setSolverObjective(data, x, solver)
###############################################################################
# Solve
###############################################################################
status = solver.Solve()
fun.convertSolution(data, x, blocks)
