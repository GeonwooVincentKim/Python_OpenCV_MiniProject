import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")
img2 = img.copy()
h, w = img.shape[:2]
