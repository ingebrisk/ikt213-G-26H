import cv2

def smoothing(image):
    print("Running function: smoothing()")
    ksize=(15,15)
    blurred = cv2.GaussianBlur(image, (15, 15), 0)
    cv2.imshow("blurred photo", blurred)
        
    cv2.imwrite("assignment_2/solution/images/8_smoothing_image.png", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image = cv2.imread("assignment_2/images/iris.png")
    smoothing(image)


if __name__ == "__main__":
    main()
    