![](https://chipdelmal.github.io/media/lego/banner.png)

Please have a look at my [blog post](https://chipdelmal.github.io/artsci/2022-04-04-LegoOptimizer.html) for more info on how this pipeline works, and the reasoning behind the solution!

## Problem Statement

Given a pixel-based image and a pool of colored Lego blocks: can I recreate the image with my available blocks?
* If so, how should I arrange them so that I don't run out of them without the image being completed?
* If not, what blocks are missing for me to complete the image?

Unfortunately, this is not as easy of a problem as it looks at first glance and it will take image quantizing, run-length encoding, multiple-knapsack problems instances, and some image overlays to get it all done!



## Features

* Automatic image re-scaling.
* Arbitrary color-palette quantization (or quantization to a given number of colors).
* Prioritization of certain block-lengths provided by the user.
* Arbitrary pools of blocks can be defined.
* Highlighting of missing pieces for the image to be completed.
* Generation of the "bill of materials".


## Pipeline

To get the code up and running, have a look at the [selections.py](./selections.py) and [constants](./constants.py) files to setup the parameters of your portraits (might streamline it a bit in the future when I have some time).

Now, just run the [main.sh](./main.sh) file with:

``` bash
main.sh FILE_PATH FILE_NAME
```


This bash wrapper runs the following scripts in order:

1. [Image Preprocessing](./pimage.py): quantize, downsample and export image
2. [Data Preprocess](./preprocess.py): color to key mapping, run-length encoding, export problem vectors
3. [Optimization](./optimizer.py): solve multiple-knappsack problem
4. [Postproces](./decoder.py): decode run-length to image reconstruct
5. [Image reconstruction](./reconstruct.py): reconstruct image with block highlights
6. [Bill of Materials](./bom.py): Get the BOM and add it to the image


![](https://chipdelmal.github.io/media/lego/bike_FNL.png)


## Dependencies

To run the code, install the following dependencies: [matplotlib](https://matplotlib.org/), [opencv-python](https://pypi.org/project/opencv-python/), [Pillow](https://pillow.readthedocs.io/en/stable/), [numpy](https://numpy.org/), [OR-Tools](https://developers.google.com/optimization/install), [compress-pickle](https://pypi.org/project/compress-pickle/), [termcolor](https://pypi.org/project/termcolor2/). Working in an independent virtual environment like [anaconda](https://www.anaconda.com/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) is highly recommended!

```bash
pip install ortools
pip install numpy
pip install matplotlib
pip install compress-pickle
pip install termcolor
```

## Author

<img src="https://chipdelmal.github.io/MGSurvE_Presentations/2022_Lab/images/detective.png" height="125px" align="middle">

[Héctor M. Sánchez C.](https://chipdelmal.github.io/)
