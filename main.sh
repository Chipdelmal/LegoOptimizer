#!/bin/bash

PTH='./demo'
FNAME='sami.png'

echo "* Preprocessing data..."
python preprocess.py $PTH $FNAME
echo "* Optimizing combinatorics..."
python optimizer.py $PTH $FNAME