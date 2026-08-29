import cv2
import numpy as np

def copy(image, emptyPictureArray):
    print("Running function: copy()")
    
    height, width, channels = image.shape
    
    for h in range(height):
        for w in range(width):
            for c in range(channels):
                emptyPictureArray[h,w,c] = image[h,w,c]
    
    cv2.imwrite("assignment_2/solution/images/4_manually_copied_image.png", emptyPictureArray)
    
    cv2.imshow("Manualy copied picture", emptyPictureArray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
        
    
def main():
    image = cv2.imread("assignment_2/images/iris.png")
    height, width, channels = image.shape
    emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)
    copy(image, emptyPictureArray)
    
if __name__ == "__main__":
    main()