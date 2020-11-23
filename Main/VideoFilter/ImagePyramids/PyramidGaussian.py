import cv2


img = cv2.imread("../../../img/People.jpg")

smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(img)
