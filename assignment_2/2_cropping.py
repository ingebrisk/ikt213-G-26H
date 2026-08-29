import cv2
import numpy as np

def crop(image, x_0, x_1, y_0, y_1):
    # Cut the image such that it returns only the part of the image which is of interest
    print("Running function: cropping()")
    
    cropped_image = image[y_0:y_1, x_0:x_1]
    
    #save image 
    cv2.imwrite("assignment_2/solution/images/2_cropped_image.png", cropped_image)
    
    #show cropped photo
    cv2.imshow("crop", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def main():
    image = cv2.imread("assignment_2/images/iris.png")
    
    x_0 = 200
    y_0 = 200
    x_1 = 800 - 130     # width: 800, from assignment 1 
    y_1 = 600 - 130     # hight: 600, from assignment 1
    
    crop(image, x_0, x_1, y_0, y_1)
    
    
if __name__ == "__main__":
    main()


