

from os import path
from sys import argv
from PIL import Image
from collections import Counter
from compress_pickle import dump, load
import selections as sel
import functions as fun
import selections as sel

if fun.isNotebook():
    (fPath, fName) = ('./demo', 'awoofy.png')
else:
    (fPath, fName) = (argv[1], argv[2])
###############################################################################
# Load image and decoded data
###############################################################################
dFName = path.join(fPath, fName.split('.png')[0])+'_Lego.png'
img = Image.open(dFName)
# Read decoded data -----------------------------------------------------------
dFName = path.join(fPath, fName.split('.png')[0])+'_Decoded.pkl'
decoded = load(dFName)
###############################################################################
# Get colors
###############################################################################
cSet = set()
for row in decoded:
    cSet = cSet.union(set([i[0] for i in row]))
###############################################################################
# Get colors blocks
###############################################################################
cDict = {i: [] for i in sorted(list(cSet))}
for row in decoded:
    rowDict = {c: v for (c, v) in row}
    for clr in rowDict.keys():
        cDict[clr].extend(rowDict[clr])
###############################################################################
# Get color blocks counts
###############################################################################
cList = list(cDict.keys())
cCounts = {col: dict(Counter(sorted(cDict[col]))) for col in cList}