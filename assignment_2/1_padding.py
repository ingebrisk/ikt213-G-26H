import cv2
import numpy as np
from matplotlib import pyplot as plt
#1. Padding: Create a border around the original image which reflects the edges of the original image

def padding(image, border_width):
    # make paddings to images
    print("running function: padding()")
    
    reflect = cv2.copyMakeBorder(image,border_width,border_width,border_width,border_width,cv2.BORDER_REFLECT)
    
    #save image
    cv2.imwrite("assignment_2/solution/images/1_padded_reflect.png", reflect)
    
    #show image
    plt.imshow(reflect,'gray'),plt.title('REFLECT')
    plt.axis('off')
    plt.show()
    
def main():
    image = cv2.imread("assignment_2/images/iris.png")
    border_width = 100 
    padding(image, border_width)



if __name__ == "__main__":
    main()
