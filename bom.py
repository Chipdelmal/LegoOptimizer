

from os import path
from sys import argv
from PIL import Image
from collections import Counter
from compress_pickle import load
import matplotlib.pyplot as plt
import settings as sel
import functions as fun


if fun.isNotebook():
    (fPath, fName) = (
        '/Users/sanchez.hmsc/Documents/SyncMega/LegoOptimizer/', 
        'megaman.png'
    )
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
row = decoded[0]
for row in decoded:
    # rowDict = {c: v for (c, v) in row}
    rowDict = {}
    rowC = list(set([i[0] for i in row]))
    for col in rowC:
        rowDict[col] = fun.flatten([i[1] for i in row if i[0]==col])
    for clr in rowDict.keys():
        cDict[clr].extend(rowDict[clr])
###############################################################################
# Get color blocks counts
###############################################################################
cList = list(cDict.keys())
cCounts = {col: dict(Counter(sorted(cDict[col]))) for col in cList}
# Patch missing blocks index --------------------------------------------------
# for k in list(cCounts.keys()):
#     try: cCounts[k]['M'] = cCounts[k].pop(-1)
#     except: continue
###############################################################################
# Generate BOM image
###############################################################################
bom = fun.genColorCounts(
    cCounts, 250, img.size[1], img.size, upscale=sel.USER_SEL['scaler']
)
dFName = path.join(fPath, fName.split('.png')[0])+'_BOM.png'
plt.savefig(
    dFName, bbox_inches='tight', pad_inches=0, facecolor='w'
)
plt.close('all')
###############################################################################
# Concatenate images
###############################################################################
imgBOM = Image.open(dFName).convert('RGB')
ccat = fun.hConcat(img, imgBOM)
dFName = path.join(fPath, fName.split('.png')[0])+'_FNL.png'
ccat.save(dFName)



# sum([i for i in cDict[(55, 33, 0)] if i==-1])
# fun.flatten([i[1] for i in row if i[0]==rowC[0]])
