import cv2
import numpy as np


img = cv2.imread("../../../../img/5shapes.jpg")
img2 = img.copy()
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(
    im_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)
