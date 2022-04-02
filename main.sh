#!/bin/bash

PTH='./demo'
FNAME='DWN-Resurrect_32-rocketsPalette.png'

echo "* Reshaping image data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics (could take a while)..."
python optimizer.py $PTH $FNAME
echo "* Decoding results..."
python decoder.py $PTH $FNAME
echo "* Reconstructing image..."
python reconstruct.py $PTH $FNAME