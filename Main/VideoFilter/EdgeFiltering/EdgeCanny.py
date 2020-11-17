import cv2
import numpy as np


img = cv2.imread('../../../img/sudoku.png')

edges = cv2.Canny(img, 100, 200)
