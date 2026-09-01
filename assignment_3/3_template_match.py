import cv2
import numpy as np
from matplotlib import pyplot as plt


def template_match(image, template):
    print("Running fundtion: template_match")

    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    w,h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv2.imwrite('assignment_3/solution/images/3_template_match_image.png',image)

def main(): 
    image = cv2.imread("assignment_3/images/shapes-1.png")
    template = cv2.imread("assignment_3/images/shapes_template.jpg",0)
    template_match(image, template)


if __name__ == "__main__":
    main()
    
