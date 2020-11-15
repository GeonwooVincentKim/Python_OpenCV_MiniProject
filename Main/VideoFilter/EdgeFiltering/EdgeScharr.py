import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")

gx_k = np.array([[-3, 0, 3], [-10, 0, 10], [-3, 0, 3]])
gy_k = np.array([[-3, -10, -3], [0, 0, 0], [3, 10, 3]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

scharr_x = cv2.Scharr(img, -1, 1, 0)
scharr_y = cv2.Scharr(img, -1, 0, 1)