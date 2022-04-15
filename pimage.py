
from os import path
from sys import argv
from PIL import Image
import functions as fun
import constants as cst
import settings as sel


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
###############################################################################
# Get user selections from file
###############################################################################
(SIZE, PALETTE) = (sel.USER_SEL['size'], sel.USER_SEL['palette'])
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
imgDwn = imgQnt.resize(SIZE, resample=Image.LANCZOS)
imgDwn.save(pthDWN)
