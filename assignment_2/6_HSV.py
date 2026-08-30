import cv2

def hsv(image):
    print("Running function: hsv()")
    	
    hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    cv2.imshow('HSV image', hsvImage)
    
    cv2.imwrite("assignment_2/solution/images/6_HSV_image.png", hsvImage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(): 
    image = cv2.imread("assignment_2/images/iris.png")
    hsv(image)

if __name__ == "__main__":
    main()
