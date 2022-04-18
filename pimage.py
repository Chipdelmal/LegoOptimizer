
from os import path
from sys import argv
from PIL import Image
from PIL.Image import Resampling
from termcolor import colored
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
if isinstance(PALETTE, int):
    # Provided palette is a number of target quantization colors --------------
    imgQnt = fun.quantizeImage(img, int(PALETTE), method=0)
    print(colored(f'+ Quantizing image to {PALETTE} colors', 'red'))
elif isinstance(PALETTE, tuple) or isinstance(PALETTE, list):
    # Provided palette is a list or tuple of colors with no block qty ---------
    cpal = fun.paletteReshape(PALETTE)
    imgQnt = fun.quantizeImage(
        img, colorPalette=cpal[1], method=0
    )
    print(colored(f'+ Quantizing image to palette with no block QTY', 'red'))
elif isinstance(PALETTE, dict):
    # Provided palette is a dictionary of colors with block qty ---------------
    pal = tuple(PALETTE.keys())
    cpal = fun.paletteReshape(pal)
    imgQnt = fun.quantizeImage(
        img, colorPalette=cpal[1], method=0
    )
    print(colored(f'+ Quantizing image to palette with block QTY', 'red'))
else:
    print(colored("Error in the color palette!", "red"))
###############################################################################
# Downscale
#   NEAREST, BILINEAR, BICUBIC, LANCZOS, NEAREST
###############################################################################
pthDWN = path.join(fPath, fName.split('.png')[0]+'_DWN.png')
imgDwn = imgQnt.resize(SIZE, resample=Resampling.NEAREST)
imgDwn.save(pthDWN)
imgDwn.close()