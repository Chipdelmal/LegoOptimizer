#!/bin/bash

FNAME='sami.png'
PTH='./demo'

echo "* Quantize and downscale image..."
python pimage.py $PTH $FNAME
echo "* Reshaping image data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics (could take a while)..."
python optimizer.py $PTH $FNAME
echo "* Decoding results..."
python decoder.py $PTH $FNAME
echo "* Reconstructing image..."
python reconstruct.py $PTH $FNAME
echo '* Generating BOM...'
python bom.py $PTH $FNAME