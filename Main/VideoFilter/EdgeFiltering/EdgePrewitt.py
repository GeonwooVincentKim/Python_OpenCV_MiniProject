import cv2
import numpy as np


file_name = "../../../img/sudoku.png"
img = cv2.imread(file_name)

gx_k = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
gy_k = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)
