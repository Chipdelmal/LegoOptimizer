
import cv2
import numpy as np
from os import path
from sys import argv
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from compress_pickle import dump, load
import functions as fun


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'DWN-Resurrect_32-rocketsPalette.png')
else:
    (fPath, fName) = (argv[1], argv[2])
SCALER = 10
BLOCKS_ALPHA = 1
(RB_COL, RN_COL, BK_COL) = ((0, 0, 0, 127), (255, 0, 0, 255), (255, 255, 255, 0))
(LW, LG) = (2, 1)
###############################################################################
# Load image and decoded data
###############################################################################
img = Image.open(path.join(fPath, fName))
img = img.convert('RGBA')
img = img.resize((np.array(img.size)*SCALER).astype(int), resample=0)
# Read decoded data -----------------------------------------------------------
dFName = path.join(fPath, fName.split('.png')[0])+'_Decoded.pkl'
decoded = load(dFName)
###############################################################################
# Add block grid (currently not working)
###############################################################################
draw = ImageDraw.Draw(img)
for x in range(0, img.width, SCALER):
    line = ((x, 0), (x, img.height))
    draw.line(line, fill=BK_COL, width=LG)
for y in range(0, img.height, SCALER):
    line = ((0, y), (img.width, y))
    draw.line(line, fill=BK_COL, width=LG)
###############################################################################
# Annotate rectangles 
###############################################################################
# Add frame all around image --------------------------------------------------
draw.rectangle(((0, 0), (img.width-LW/2, img.height-LW/2)), outline=RB_COL, width=LW)
# Iterate through the decoded array (rix: row index)
for rix in range(len(decoded)):
    # Get row information (dRow: decoded row)
    dRow = decoded[rix]
    # Get the iterators started
    (row, col) = (rix, 0)
    # Load info from the block index
    for bix in range(len(dRow)):
        (bColor, bLensVct) = dRow[bix]
        bColsLen = len(bLensVct)
        for bCols in range(bColsLen):
            # Setup the drawer to the left-top corner
            tlCrnr = (SCALER*col+LW/2, SCALER*row+LW/2)
            # The length of the block is defined by the array (height is constant for all)
            (w, h) = (bLensVct[bCols]*SCALER, 1*SCALER)
            rectCol = RB_COL if (w > 0) else RN_COL
            w = abs(w)
            blocks = (tlCrnr, (tlCrnr[0]+w-LW/2, tlCrnr[1]+h-LW/2))
            # Draw the resulting block 
            draw = ImageDraw.Draw(img)
            # draw.rectangle(blocks, fill=(*bColor, int(255*BLOCKS_ALPHA)))
            draw.rectangle(blocks, outline=rectCol, width=LW)
            # Shift column iterator
            col = col + abs(bLensVct[bCols])
###############################################################################
# Export Resulting Image
###############################################################################
dFName = path.join(fPath, fName.split('.png')[0])+'_Lego.png'
img.save(dFName)
