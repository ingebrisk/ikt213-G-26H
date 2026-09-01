import cv2
import numpy as np
from matplotlib import pyplot as plt


def resize(image, scale_factor:int, up_or_down:str):
    print("Running fundtion: resize")

    rows, cols, _channels = map(int, image.shape)
    
    cv2.imshow('Pyramids Demo', image)
    
    if up_or_down == "up":
        image = cv2.pyrUp(image, dstsize=(2 * cols, 2 * rows))
        cv2.imwrite('assignment_3/solution/images/4_resize_UP_image.png',image)
        print (f'** Zoom In: Image x {scale_factor}')         
    elif up_or_down == 'down':
        image = cv2.pyrDown(image, dstsize=(cols // 2, rows // 2))
        cv2.imwrite('assignment_3/solution/images/4_resize_DOWN_image.png',image)
        print (f'** Zoom Out: Image / {scale_factor}')
    else:
        print("Error: not correct input")

    cv2.destroyAllWindows()
    return 0

def main(): 
    image = cv2.imread("assignment_3/images/lambo.png")

    resize(image, 2, "down")


if __name__ == "__main__":
    main()
    




