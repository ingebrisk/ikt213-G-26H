import cv2

def canny_edge_detection(image, threshold_1, threshold_2):
    print("Running fundtion: canny_edge_detection")

    image_blur = cv2.GaussianBlur(image,(3,3),  sigmaX=0)
    canny_edges = cv2.Canny(image=image_blur,threshold1=threshold_1, threshold2=threshold_2)

    cv2.imshow('Canny Edge Detection', canny_edges)
    cv2.imwrite("assignment_3/solution/images/2_canny_edges_image.png", canny_edges)
    cv2.waitKey(0)


def main(): 
    image = cv2.imread("assignment_3/images/lambo.png")
    threshold_1=50
    threshold_2=50
    canny_edge_detection(image, threshold_1, threshold_2)

if __name__ == "__main__":
    main()
    