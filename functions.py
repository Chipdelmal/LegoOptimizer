
import numpy as np
from time import time
from termcolor import colored
from itertools import groupby
import matplotlib.pyplot as plt
from PIL import Image, ImageColor
import matplotlib.patches as mpatch
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

def isInt(element):
    try:
        int(element)
        return True
    except ValueError:
        return False

###############################################################################
# Image Preprocessing
###############################################################################
def rgbToHex(rgb):
    # https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
    return '%02x%02x%02x' % rgb

def paletteReshape(colorPalette):
    # Hex to entries
    rgbTuples = [ImageColor.getrgb(i) for i in colorPalette]
    pal = [item for sublist in rgbTuples for item in sublist]
    entries = int(len(pal)/3)
    # Palette swatch
    palette = pal + [0,]*(256-entries)*3
    resnp = np.arange(entries, dtype=np.uint8).reshape(entries, 1)
    resim = Image.fromarray(resnp, mode='P')
    resim.putpalette(palette)
    # Return
    return (len(pal), resim)

def quantizeImage(img, colorsNumber=255, colorPalette=None, method=0, dither=False):
    if colorPalette is None:
        img = img.quantize(colorsNumber, method=method, dither=dither)
    else:
        img = img.quantize(
            palette=colorPalette, method=method, dither=dither
        )
    return img

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
    blocksAtBins = []
    for b in data['all_bins']:
        elementsInBin = []
        for i in data['all_items']:
            if x[i, b].solution_value() > 0:
                elementsInBin.append(blocks[i])
        blocksAtBins.append(elementsInBin)
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
    # print(solution)
    if verbose:
        (gLen, gNum) = (len(gaps), sum(gaps))
        if (gNum==sum(flatten(solution))):
            pCol = 'green'
        else:
            pCol = 'red'
        # Print summary to terminal -------------------------------------------
        print(
            colored(
                f"[{rTime:.2f} mins for {gLen:04d} elements with {gNum:04d} length]",
                pCol
            )
        )
    outDict = solution
    return outDict

###############################################################################
# BOM Swatch
###############################################################################
def genColorCounts(
        imgPalette, width, height, imgSize, upscale=1,
        fontdict = {'family':'monospace', 'weight':'normal', 'size':30},
        xlim = (0, 1.25)
    ):
    pal = imgPalette
    # Create canvas
    fig = plt.gcf()
    DPI = fig.get_dpi()
    ax = fig.add_axes([0, 0, 1, 1])
    fig.set_size_inches(width/float(DPI), height/float(DPI))
    # Setting up groups
    n_groups = 1
    n_rows = len(pal)//n_groups+1
    # Generate swatch with count
    for j in range(len(pal)):
        (wr, hr) = (.25, 1)
        (color, count) = pal[j]
        rgb = [i/255 for i in ImageColor.getcolor(color, "RGB")]
        # Color rows
        col_shift = (j//n_rows)*3
        y_pos = (j%(n_rows))*hr
        # Print rectangle and text
        hshift = .05
        ax.add_patch(mpatch.Rectangle(
            (hshift+col_shift, y_pos), wr, hr, color=rgb, ec='k', lw=4
        ))
        colorText = color.upper()
        ax.text(
            hshift+wr*1.1+col_shift, y_pos+hr/2, 
            f' {colorText} ({count:05}) ', 
            color='k', va='center', ha='left', fontdict=fontdict
        )
    # Add pixel size and total count
    pxSize = [int(i/upscale) for i in imgSize]
    y_pos = ((0)%(n_rows))*hr
    ax.text(
        hshift, y_pos-hr/2, 
        f'Size: {pxSize[0]}x{pxSize[1]}', 
        color='k', va='center', ha='left', fontdict=fontdict
    )
    y_pos = ((j+1)%(n_rows))*hr
    ax.text(
        hshift, y_pos+hr/2, 
        f'Total: {pxSize[0]*pxSize[1]}', 
        color='k', va='center', ha='left', fontdict=fontdict
    )
    # Clean up the axes
    ax.set_xlim(xlim[0], xlim[1]*n_groups)
    ax.set_ylim((n_rows), -1)
    ax.axis('off')
    # Return figure
    return (fig, ax)
