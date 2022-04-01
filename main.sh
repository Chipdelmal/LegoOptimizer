#!/bin/bash

PTH='./demo'
FNAME='sami.png'

echo "* Reshaping image data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics (could take a while)..."
python optimizer.py $PTH $FNAME
echo "* Decoding image..."
python decoder.py $PTH $FNAME
echo "* Exporting image..."
python reconstruct.py $PTH $FNAME