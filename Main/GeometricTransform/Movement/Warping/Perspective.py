import cv2
import numpy as np


file_name = "../../../../img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

pts1 = np.float32([[0, 0], [0, rows], [cols, 0], [cols.rows]])
pts2 = np.float32([[100, 50], [10, rows - 50], [cols - 100, 50], [cols - 10, rows - 50]])


