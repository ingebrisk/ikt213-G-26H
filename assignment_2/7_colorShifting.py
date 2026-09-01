import cv2
import numpy as np

def hue_shifted(image,emptyPictureArray, hue):
    print("Running function: hue_shifted()")
    	
    height, width, channels = image.shape
    for h in range(height):
            for w in range(width):
                for c in range(channels):
                    
                    emptyPictureArray[h, w, c] = (int(image[h, w, c]) + hue) % 256
    
    cv2.imshow("hue changed photo", emptyPictureArray)
    
    cv2.imwrite("assignment_2/solution/images/7_color_shifting_image.png", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def main(): 
    image = cv2.imread("assignment_2/images/iris.png")
    height, width, channels = image.shape
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    hue = 50
    hue_shifted(image, emptyPictureArray, hue)


if __name__ == "__main__":
    main()


