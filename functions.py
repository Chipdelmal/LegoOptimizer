
from time import time
from termcolor import colored
from itertools import groupby
from ortools.linear_solver import pywraplp
import constants as cst

###############################################################################
# Auxiliary
###############################################################################
def runLength(s_list):
    # https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-75.php
    grp = groupby(s_list)
    runL = tuple([tuple([len(list(group)), key]) for key, group in grp])
    return runL

def flatten(t):
    # https://stackoverflow.com/questions/952914/how-to-make-a-flat-list-out-of-a-list-of-lists
    return [item for sublist in t for item in sublist]

def rgbToHex(rgb):
    # https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
    return '%02x%02x%02x' % rgb

def isNotebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True
        elif shell == 'TerminalInteractiveShell':
            return False
        else:
            return False
    except NameError:
        return False

###############################################################################
# Optimization
#   https://developers.google.com/optimization/bin/multiple_knapsack
###############################################################################
def genSolverData(gaps, blocks, values=cst.LARGE_FIRST_BLOCK_VALUES):
    data = {}
    data['weights'] = blocks
    data['values'] = [values[i] for i in blocks]
    assert len(data['weights']) == len(data['values'])
    data['num_items'] = len(data['weights'])
    data['all_items'] = range(data['num_items'])
    data['bin_capacities'] = gaps
    data['num_bins'] = len(data['bin_capacities'])
    data['all_bins'] = range(data['num_bins'])
    return data

def genSolverXVector(data, solver):
    # x[i, b] = 1 if item i is packed in bin b
    x = {}
    for i in data['all_items']:
        for b in data['all_bins']:
            x[i, b] = solver.BoolVar(f'x_{i}_{b}')
    return (x, solver)

def setSolverConstraints(data, x, solver):
    # Each item is assigned to at most one bin.
    for i in data['all_items']:
        solver.Add(sum(x[i, b] for b in data['all_bins']) <= 1)
    # The amount packed in each bin cannot exceed its capacity.
    for b in data['all_bins']:
        solver.Add(
            sum(x[i, b] * data['weights'][i]
                for i in data['all_items']) <= data['bin_capacities'][b])
    return (x, solver)


def setSolverObjective(data, x, solver):
    objective = solver.Objective()
    for i in data['all_items']:
        for b in data['all_bins']:
            objective.SetCoefficient(x[i, b], data['values'][i])
    objective.SetMaximization()
    return (x, solver, objective)

def convertSolution(data, x, blocks):
    blocksAtBins = {}
    for b in data['all_bins']:
        elementsInBin = []
        for i in data['all_items']:
            if x[i, b].solution_value() > 0:
                elementsInBin.append(blocks[i])
        blocksAtBins[b] = elementsInBin
    return blocksAtBins


def solveColor(
        gaps, blocks, 
        values=cst.LARGE_FIRST_BLOCK_VALUES, verbose=True
    ):
    # Start timer and generate data structure for solver ----------------------
    tic = time()
    data = genSolverData(gaps, blocks, values=values)
    # Setup problem -----------------------------------------------------------
    solver = pywraplp.Solver.CreateSolver('SCIP')
    (x, solver) = genSolverXVector(data, solver)
    (x, solver) = setSolverConstraints(data, x, solver)
    (x, solver, objective) = setSolverObjective(data, x, solver)
    # Solve problem -----------------------------------------------------------
    status = solver.Solve()
    # Timing ------------------------------------------------------------------
    toc = time()
    rTime = (toc-tic)/60
    # Assemble and return solution --------------------------------------------
    solution = convertSolution(data, x, blocks)
    if verbose:
        (gLen, gNum) = (len(gaps), sum(gaps))
        print(
            colored(
                f"[{rTime:.2f} mins for {gLen:04d} elements with {gNum:04d} length]",
                'red'
            )
        )
    outDict = solution
    return outDict