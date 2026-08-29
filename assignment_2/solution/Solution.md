# Create functions for padding, cropping, resizing, copying, grayscale, hue-shift, HSV, smoothing, rotation

## Padding 
**Create a border around the original image which reflects the edges of the original image.**
Using ![OpenCV dokumentation](http://www.bim-times.com/opencv/3.3.0/d3/df2/tutorial_py_basic_ops.html) to make paddings that reflects. 

## Cropping
**Cut the image such that it returns only the part of the image which is of interest (in your case, the center of the iris)**
To do this, the documentation from ![LearOpenCV](https://learnopencv.com/cropping-an-image-using-opencv/) was used. We also needed the dimention of the photo from assignment 1. A better aproche whold also perhaps gather the information on new in the function, but this was not used for this time. 

## Resize
**Create a function which lets you resize the image**
The dcumentation from ![geeks for geeks](https://www.geeksforgeeks.org/python/image-resizing-using-opencv-python/) was followed to do this task. 

## Manual Copy
**use what we learned in Lab 1 to get the width, height, and channels, and create a new empty array with**
When Copying an image manually with arrays we copy pixel by pixel with help of three for loops since each pixel hase a hight position, with position and a color value (channel). 


## Grayscale: 
**Convert the colored image to a grayscale image.**
Following the documentation from ![techtutorialsx](https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/) to convert given image into black and white colored photo. 

## HSV
**Convert an RGB image to use HSV**
HSV stands for Hue Saturation and Value. To convert the image from RGB to HSV the documentation from ![techtutorialsx](https://techtutorialsx.com/2019/11/08/python-opencv-converting-image-to-hsv/) was used. 