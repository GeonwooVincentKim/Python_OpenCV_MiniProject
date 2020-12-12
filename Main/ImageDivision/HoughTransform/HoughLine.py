import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")
img2 = img.copy()
h, w = img.shape[:2]

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 100, 200)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 130)
