import cv2
import numpy as np


img = cv2.imread("../../img/shapes.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
img2, contours, hierachy = cv2.findContours(
    th, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for c in contours:
    mmt = cv2.moments(c)
    cx = int(mmt['m10'] / mmt['m00'])
    cy = int(mmt['m01'] / mmt['m00'])

    a = mmt['m00']
    l = cv2.arcLength(c, True)
