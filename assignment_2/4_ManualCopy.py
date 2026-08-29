import cv2
import numpy as np

def copy(image):
    height, width, channels = image.shape
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)

def main():
    image = cv2.imread("assignment_1/images/iris-1.jpg")
    copy(image)
    
if __name__ == "__main__":
    main()