import cv2
import numpy as np
from matplotlib import pyplot as plt

def resize(image, width, height):
    print("Running function: resize()")
    
    Resized_picture = cv2.resize(image, (width, height) ,interpolation=cv2.INTER_AREA)
    
    cv2.imwrite("assignment_2/solution/images/3_resized_image.png", Resized_picture)
    
    plt.imshow(cv2.cvtColor(Resized_picture, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()


def main():
    image = cv2.imread("assignment_2/images/iris.png")
    
    width = 200
    height = 200 
    resize(image, width, height)



if __name__ == "__main__":
    main()