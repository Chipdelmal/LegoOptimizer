
from os import path
from sys import argv
from copy import deepcopy
from compress_pickle import dump, load
import functions as fun


if fun.isNotebook():
    (fPath, fName) = ('./demo', 'sami.png')
else:
    (fPath, fName) = (argv[1], argv[2])
###############################################################################
# Load Data
###############################################################################
pFName = path.join(fPath, fName.split('.png')[0])+'.pkl'
oFName = path.join(fPath, fName.split('.png')[0])+'_Solved.pkl'
(pDict, oDict) = (load(pFName), load(oFName))
lDict = pDict['runLengthVectors']
###############################################################################
# Load Data
###############################################################################
rix = 0
mapDict = {}
for rix in range(len(lDict)):
    (ld, od) = (lDict[rix], oDict[rix])
    mapping = [[ld[bix], od[bix]] for bix in range(len(lDict[rix]))]
    mapDict[rix] = mapping
###############################################################################
# Generate Decoded Image
###############################################################################
# Create a copy of the lists to process (as we will mutate pop) ---------------
mDict = deepcopy(mapDict)
rLens = deepcopy(pDict['runLengthVectors'])
# Decode image to rLen with color maps ----------------------------------------
(rowsNum, colsNum) = (len(pDict['imageMapped']), len(pDict['imageMapped'][0]))
decodedImg = []
for rix in range(rowsNum):
    # Move the pointer to the beginning and get the whole row of pixels
    ixH = 0
    rowMap = pDict['imageMapped'][rix]
    decodedRow = []
    while (ixH < len(rowMap)):
        # Get the color's index at current slot being rLen-decoded
        ixCol = rowMap[ixH]
        # Get the solution's list of encoded blocks
        (solLenIdeal, solBlocks) = mDict[ixCol].pop(0)
        # Check length of gaps versus suggested blocks (needs action for error case)
        orgLength = rLens[ixCol].pop(0)
        rgb = pDict['colorDeMapper'][ixCol]
        # Gets the RGB value of the processed color and the block elements
        solLength = sum(solBlocks)
        if (solLength == orgLength):
            # Base case where a solution was found for the encoding
            dec = (rgb, solBlocks)
            decodedRow.append(dec)
        else:
            # Handles the case where blocks were missing for encoding
            # print(f"Missmatch! ({solLength}/{orgLength})")
            # Missing elements are returned as negative
            if len(solBlocks) > 0:
                dec = (rgb, solBlocks+[solLength-orgLength])
                decodedRow.append(dec)
            else:
                dec = (rgb, solBlocks+[-orgLength])
                decodedRow.append(dec)
        # Update the iterator
        ixH = ixH + orgLength
    decodedImg.append(decodedRow)
###############################################################################
# Export Decoded List
#   decodedImg: List of rows of run-length encoded (rgb, blocks) tuples
###############################################################################
dFName = path.join(fPath, fName.split('.png')[0])+'_Decoded.pkl'
dump(decodedImg, dFName)