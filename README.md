# Gridder
A simple utility to take an image as input and divide it into smaller parts by specifying a grid size.

## Installation

Clone the repository and run the following command:

    poetry install

## Usage

To use the script, run the following command in the terminal, replacing `<image_path>`, `<width>` and `<height>` with the path to your image and the desired width and height of the grid.

    python gridder.py <image_path> <width> <height>

For example, to split the image "image.jpg" into a grid of 7 columns and 2 rows, you would run the following command:

    python gridder.py image.jpg 7 2

The output will be a set of images saved in the `outputs/` folder, with names like `cell_0_0.jpg`, `cell_0_1.jpg`, `cell_1_0.jpg`...
