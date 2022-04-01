
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
###############################################################################
# Load image and decoded data
###############################################################################
# Read original image to matplotlib -------------------------------------------
# img = mpimg.imread(path.join(fPath, fName))
# Read original image to PIL --------------------------------------------------
img = Image.open(path.join(fPath, fName))
img = img.resize((np.array(img.size)*SCALER).astype(int), resample=0)
# Read original image to opencv -----------------------------------------------
# img = cv2.imread(path.join(fPath, fName))
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow('ellipse Image',img)
# Read decoded data -----------------------------------------------------------
dFName = path.join(fPath, fName.split('.png')[0])+'_Decoded.pkl'
decoded = load(dFName)
###############################################################################
# Annotate rectangles
###############################################################################
tlCrnr = (0, 0)
(w, h) = (3*SCALER, 1*SCALER)
blocks = (tlCrnr, (tlCrnr[0]+w, tlCrnr[1]+h))

draw = ImageDraw.Draw(img, "RGBA")  
draw.rectangle(blocks, outline=(0, 0, 0, 127), width=3)
img