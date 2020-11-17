import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")
edge = cv2.Laplacian(img, -1)
