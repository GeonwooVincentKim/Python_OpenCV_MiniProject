import cv2
import numpy as np


win_name = "scan"
img = cv2.imread("../../../../img/paper.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
draw = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 200)
cv2.imshow(win_name, edged)
cv2.waitKey(0)
