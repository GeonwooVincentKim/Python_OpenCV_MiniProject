import cv2
import numpy as np


img = cv2.imread("../../img/my_hand.jpg")
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(
    gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

temp, contours, heiarchy = cv2.findContours(
    th,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

cntr = contours[0]
cv2.drawContours(
    img,
    [cntr],
    -1,
    (0, 255, 0),
    1
)

hull = cv2.convexHull(cntr)
cv2.drawContours(
    img2,
    [hull],
    -1,
    (0, 255, 0),
    1
)

print(
    cv2.isContourConvex(cntr),
    cv2.isContourConvex(hull)
)

hull2 = cv2.convexHull(
    cntr,
    returnPoints=False
)
defects = cv2.convexityDefects(
    cntr,
    hull2
)
