# LegoOptimizer


Steps:

1. Image Preprocessing: quantize, downsample and export image
2. [Data Preprocess](./preprocess.py): color to key mapping, run-length encoding, export problem vectors
3. [Optimization](./optimizer.py): solve multiple-knappsack problem
4. [Postproces](./decoder.py): decode run-length to image reconstruct
5. Image visualization: reconstruct image with block highlights


# Sources

* https://www.educative.io/m/find-all-sum-combinations
* https://stackoverflow.com/questions/42422921/multiple-subset-sum-calculation
* https://developers.google.com/optimization/bin/multiple_knapsack