
import constants as cst
from ortools.linear_solver import pywraplp
import functions as fun

###############################################################################
# Problem Input
###############################################################################
gaps = [4, 2, 6, 2]
blocks = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
values = cst.NULL_BLOCK_VALUES
data = fun.genSolverData(gaps, blocks, values=values)
###############################################################################
# Problem Setup
###############################################################################
solver = pywraplp.Solver.CreateSolver('SCIP')
(x, solver) = fun.genSolverXVector(data, solver)
(x, solver) = fun.setSolverConstraints(data, x, solver)
(x, solver, objective) = fun.setSolverObjective(data, x, solver)
###############################################################################
# Objective
###############################################################################

status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    print(f'Total packed value: {objective.Value()}')
    total_weight = 0
    for b in data['all_bins']:
        print(f'Bin {b}')
        bin_weight = 0
        bin_value = 0
        for i in data['all_items']:
            if x[i, b].solution_value() > 0:
                print(
                    f"Item {i} weight: {data['weights'][i]} value: {data['values'][i]}"
                )
                bin_weight += data['weights'][i]
                bin_value += data['values'][i]
        print(f'Packed bin weight: {bin_weight}')
        print(f'Packed bin value: {bin_value}\n')
        total_weight += bin_weight
    print(f'Total packed weight: {total_weight}')
else:
    print('The problem does not have an optimal solution.')
