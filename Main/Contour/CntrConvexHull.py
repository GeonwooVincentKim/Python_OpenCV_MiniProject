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
