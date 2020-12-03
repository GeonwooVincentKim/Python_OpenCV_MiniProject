import cv2
import numpy as np


img = cv2.imread("../../img/shapes.png")
img2 = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imth_res = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

img2, contour, hierarchy = cv2.findContours(
    imth_res, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

img2, contour2, hierarchy = cv2.findContours(
    imth_res, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

print('Number of Figure : %d {%d}' % (len(contour), len(contour2)))
cv2.drawContours(img, contour, -1, (0, 255, 0), 4)
cv2.drawContours(img2, contour2, -1, (0, 255, 0), 4)
