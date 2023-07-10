# General overview

- A mosaic image is composed of multiple very small images that are visible when viewed up close, but give a different image when viewed from a distance. In this project, we aim to create such images.
- This project is written in Python, and we recommend reading the documentation thoroughly to familiarize yourself with each component of the project and its problem-solving algorithm.

# Project objective
The objective of this project is to implement a mosaic image generator using the OpenCV library. The mosaic image generator takes an input of a target image and a set of source images, divides the image into a specific grid of tiles based on a predefined network of tiles, and then replaces each tile with the most similar source image.

# Used libraries
The main library used in this project is OpenCV, which is used for image processing and machine learning. The next library is Numpy, which allows for various operations on numerical data stored in memory.

# Project functions review
- readSamples
  
This function takes the name of a directory as input and saves all sample images in an array, returning it as output. The purpose of using this function is to read sample images from the target directory.

- resizeSamples

This function takes an array of sample images as input and resizes these images according to the size of the mosaics requested by the user. The purpose of this function is to standardize the size of all sample images with the input size.

- avgRGB

This function takes an image as input and calculates the average color in its red, green, and blue channels, returning it as an array. The purpose of this function is to compare the minimum average color between two target images for replacement in the original image.

- cropImage

This function takes an image, mosaic size, and the required number of mosaics (horizontally and vertically) as input. It then cuts the target image based on the number of mosaics. This is done using nested loops, and each time a section of the target image is separated equal to the mosaic size, it is saved in an array. The output of this function is the saved array of cropped images. The purpose of this function is to divide the original image into smaller sections for comparing their average color intensity.

- getBestMatch
  
This function receives two inputs: a cropped section of the original image and the average color of all sample images. It calculates the distance between these two average colors, which are represented as vectors, using the L2 norm, and selects the sample image with the smallest color distance.

- createMosaicImg
  
The functionality of this function is almost similar to cropImage, with the difference that we provide it with a sample image and want to replace the original image with it. For this purpose, we create an empty image with the length and width of the original image and traverse it like the algorithm in the cropImage function, placing the desired sample image in it.

# Algorithm exploration
1. Read the original image and sample images.
2. Enter the desired mosaic size and then calculate the required number of mosaics based on the length and height of the original image.
3. Sometimes, our width may not be divisible by the mosaic size, and there may be extra pixels on both sides. This time, we change the size of the original image based on the number of mosaics and the mosaic size.
4.Perform a preview on all sample images and calculate their average colors.
5. Now, cut the original image based on the required mosaics and their size.
6. At this stage, our image processing has just begun, and now we compare the average of each cropped image with each sample image, selecting the one with the minimum distance.
7. At this stage, we replace the best sample images from the previous stage, which are specified as indices, with the original image.
8. Finally, we save and display the final image.

5. Perform a preview on all sample images and calculate their average colors.
6. Now, cut the original image based on the required mosaics and their size.
7. At this stage, our image processing has just begun, and now we compare the average of each cropped image with each sample image, selecting the one with the minimum distance.
8. At this stage, we replace the best sample images from the previous stage, which are specified as indices, with the original image.
9. Finally, we save and display the final image.
