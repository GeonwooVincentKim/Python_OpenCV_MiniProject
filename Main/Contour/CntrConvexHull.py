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
