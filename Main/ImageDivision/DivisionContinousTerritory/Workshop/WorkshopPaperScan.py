import cv2
import numpy as np


win_name = "scan"
img = cv2.imread("../../../../img/paper.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
draw = img.copy()
