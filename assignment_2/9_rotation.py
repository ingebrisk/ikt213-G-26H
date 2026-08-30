import cv2

def rotation(image, rotation_angle):
    print("Running function: rotation()")
   
    if rotation_angle == 90:
        rotation = cv2.ROTATE_90_CLOCKWISE
    elif rotation_angle == 180:
        rotation = cv2.ROTATE_180

    
    rotated = cv2.rotate(image, rotation)
    cv2.imshow("rotated photo", rotated)
        
    cv2.imwrite("assignment_2/solution/images/9_rotated_image.png", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    image = cv2.imread("assignment_2/images/iris.png")
    rotation_angle = 180
    rotation(image, rotation_angle)


if __name__ == "__main__":
    main()
