
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
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
SCALER = 10
ALPHA = .9
###############################################################################
# Load image and decoded data
###############################################################################
img = Image.open(path.join(fPath, fName))
img = img.resize((np.array(img.size)*SCALER).astype(int), resample=0)
# Read decoded data -----------------------------------------------------------
dFName = path.join(fPath, fName.split('.png')[0])+'_Decoded.pkl'
decoded = load(dFName)
###############################################################################
# Annotate rectangles
###############################################################################
# Iterate through the decoded array (rix: row index)
rix = 41
# Get row information (dRow: decoded row)
dRow = decoded[rix]
# Get the iterators started
(row, col) = (rix, 0)
# Load info from the block index
bix = 0
(bColor, bLen) = dRow[bix]
# Setup the drawer to the left-top corner
tlCrnr = (SCALER*col, SCALER*row)
# The length of the block is defined by the array (height is constant for all)
(w, h) = (bLen[0]*SCALER, 1*SCALER)
blocks = (tlCrnr, (tlCrnr[0]+w, tlCrnr[1]+h))
# Draw the resulting block
draw = ImageDraw.Draw(img, "RGBA")  
draw.rectangle(blocks, fill=(*bColor, int(255*ALPHA)))
draw.rectangle(blocks, outline=(0, 0, 0, 127), width=2)
img