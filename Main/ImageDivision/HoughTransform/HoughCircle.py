import cv2
import numpy as np


img = cv2.imread("../../../img/coins_spread1.jpg")
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)
blur = cv2.GaussianBlur(
    gray,
    (3, 3),
    0
)

circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    1, 5, 30,
    None,
    200
)
