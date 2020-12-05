import cv2
import numpy as np


img = cv2.imread("../../img/lightning.png")
img_gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)

ret, th = cv2.threshold(
    img_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

im, contours, hr = cv2.findContours(
    th, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contr = contours[0]

x, y, w, h = cv2.boundingRect(contr)
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 0, 0),
    3
)
