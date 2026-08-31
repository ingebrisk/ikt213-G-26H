import cv2

def soble_edge_detection(image):
    print("Running fundtion: soble_edge_detection")

    image_blur = cv2.GaussianBlur(image,(3,3),  sigmaX=0)

    sobelx = cv2.Sobel(image_blur, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=1)
    sobely = cv2.Sobel(image_blur, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=1)
    
    sobelxy = cv2.magnitude(sobelx, sobely)
    
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)
    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)
    final_product = cv2.normalize(sobelxy, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    cv2.imshow('Sobel gradient magnitude', final_product )
    cv2.imwrite("assignment_3/solution/images/1_sobel_gradient_magnetude_image.png", final_product)
    cv2.waitKey(0)
    

def main(): 
    image = cv2.imread("assignment_3/images/lambo.png")
    soble_edge_detection(image)

if __name__ == "__main__":
    main()
    