# LegoOptimizer

This codebase solves the following problem

__Given a pixel-based image and a pool of colored Lego blocks:__

* __Can I recreate the image with my available blocks?__
* __How should I arrange them so that I don't run out without the image being completed?__
* __What blocks are missing for me to complete the image?__

## Pipeline

1. Image Preprocessing: quantize, downsample and export image
2. [Data Preprocess](./preprocess.py): color to key mapping, run-length encoding, export problem vectors
3. [Optimization](./optimizer.py): solve multiple-knappsack problem
4. [Postproces](./decoder.py): decode run-length to image reconstruct
5. [Image reconstruction](./reconstruct.py): reconstruct image with block highlights



## Dependencies

* [opencv-python](https://pypi.org/project/opencv-python/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [numpy](https://numpy.org/)
* [OR-Tools](https://developers.google.com/optimization/install)
* [compress-pickle](https://pypi.org/project/compress-pickle/)
* [termcolor](https://pypi.org/project/termcolor2/)


## Sources

* https://www.educative.io/m/find-all-sum-combinations
* https://stackoverflow.com/questions/42422921/multiple-subset-sum-calculation
* https://developers.google.com/optimization/bin/multiple_knapsack
* https://stackoverflow.com/questions/43618910/pil-drawing-a-semi-transparent-square-overlay-on-image#43620169
