import cv2
import numpy as np


img1 = cv2.imread("../../../img/morph_dot.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("../../../img/morph_hole.png", cv2.IMREAD_GRAYSCALE)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k)
