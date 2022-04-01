#!/bin/bash

PTH='./demo'
FNAME='DWN-SGBM1A_4-sami.png'

echo "* Reshaping image data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics (could take a while)..."
python optimizer.py $PTH $FNAME
echo "* Decoding image..."
python decoder.py $PTH $FNAME
echo "* Exporting image..."
python reconstruct.py $PTH $FNAME