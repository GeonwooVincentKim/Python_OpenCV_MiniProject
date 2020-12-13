import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 50, 200)

lines = cv2.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    10, None,
    20, 2
)
