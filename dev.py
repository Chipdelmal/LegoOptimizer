import itertools
import cv2
from cv2 import imread


img = imread('./demo/DWN-Resurrect_32-rocketsPalette.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

###############################################################################
# Process image for colors
###############################################################################
pixs = tuple([tuple([tuple(i) for i in row]) for row in img])
colPal = list(set(list(itertools.chain(*pixs))))
###############################################################################
# Change colors into keys
###############################################################################
colDict = {col: ix for (ix, col) in enumerate(colPal)}
pixDict = tuple([tuple([colDict[i] for i in row]) for row in pixs])