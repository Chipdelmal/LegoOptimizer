
from os import path
from sys import argv
from compress_pickle import dump
from PIL import Image, ImageColor
import functions as fun
import constants as cst


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
SIZE = cst.DOWNSCALE_SIZE
PALETTE = cst.WIDE_COLORS
###############################################################################
# Load image
###############################################################################
pth = path.join(fPath, fName)
img = Image.open(pth).convert('RGB')
###############################################################################
# Quantize
#   0: median cut, 1: maximum coverage, 2: fast octree
###############################################################################
if not isinstance(PALETTE, tuple):
    imgQnt = fun.quantizeImage(img, int(PALETTE), method=0)
else:
    cpal = fun.paletteReshape(PALETTE)
    imgQnt = fun.quantizeImage(
        img, colorsNumber=cpal[0], colorPalette=cpal[1], method=0
    )
###############################################################################
# Downscale
#   Image.NEAREST, Image.BILINEAR, Image.BICUBIC, Image.LANCZOS, Image.NEAREST
###############################################################################
pthDWN = path.join(fPath, fName.split('.png')[0]+'_DWN.png')
imgDwn = imgQnt.resize(SIZE, resample=Image.BILINEAR)
imgDwn.save(pthDWN)
