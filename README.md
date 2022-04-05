# LegoOptimizer


## Problem Statement

Given a pixel-based image and a pool of colored Lego blocks: Can I recreate the image with my available blocks?
  * If so, how should I arrange them so that I don't run out without the image being completed?
  * If not, what blocks are missing for me to complete the image?

Unfortunately, this is not as easy of a problem as it looks at first glance and it will take image quantizing, run-length encoding, multiple-knapsack problems instances, and some image overlays to get it all done!


## Pipeline

These steps are taken sequentially in the [main.sh](./main.sh) bash script:

1. [Image Preprocessing](./pimage.py): quantize, downsample and export image
2. [Data Preprocess](./preprocess.py): color to key mapping, run-length encoding, export problem vectors
3. [Optimization](./optimizer.py): solve multiple-knappsack problem
4. [Postproces](./decoder.py): decode run-length to image reconstruct
5. [Image reconstruction](./reconstruct.py): reconstruct image with block highlights


## Dependencies

To run the code, install the following dependencies: [matplotlib](https://matplotlib.org/), [opencv-python](https://pypi.org/project/opencv-python/), [Pillow](https://pillow.readthedocs.io/en/stable/), [numpy](https://numpy.org/), [OR-Tools](https://developers.google.com/optimization/install), [compress-pickle](https://pypi.org/project/compress-pickle/), [termcolor](https://pypi.org/project/termcolor2/). Which are also defined in the [REQUIREMENTS.yml](./REQUIREMENTS.yml) and [REQUIREMENTS.txt](./REQUIREMENTS.txt). 

Working in an independent virtual environment like [anaconda](https://www.anaconda.com/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) is highly recommended!


## Sources

* https://www.educative.io/m/find-all-sum-combinations
* https://developers.google.com/optimization/bin/multiple_knapsack
* https://stackoverflow.com/questions/42422921/multiple-subset-sum-calculation
* https://stackoverflow.com/questions/43618910/pil-drawing-a-semi-transparent-square-overlay-on-image#43620169

## To Do

* Break the missing rectangles into lego blocks

## Author

Héctor M. Sánchez C.
