import cv2
import numpy as np


img = cv2.imread("../../img/shapes_donut.png")
img2 = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imth_res = cv2.threshold(
    img_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

im2, contour2, hierarchy = cv2.findContours(
    imth_res,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

print(len(contour2), hierarchy)

im2, contour2, hierarchy = cv2.findContours(
    imth_res,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

print(len(contour2), hierarchy)
