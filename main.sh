#!/bin/bash

PTH='./demo'
FNAME='DWN-Resurrect_32-rocketsPalette.png'

echo "* Reshaping image data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics..."
python optimizer.py $PTH $FNAME
echo "* Decoding image..."
python decoder.py $PTH $FNAME