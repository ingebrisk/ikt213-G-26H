import cv2

def grayscale(image):
    print("Running function: grayscale()")
    	
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray)
    
    cv2.imwrite("assignment_2/solution/images/5_grayscale_image.png", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(): 
    image = cv2.imread("assignment_2/images/iris.png")
    grayscale(image)


if __name__ == "__main__":
    main()


