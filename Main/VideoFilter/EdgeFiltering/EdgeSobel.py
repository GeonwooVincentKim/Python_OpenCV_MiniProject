import cv2
import numpy as np


file_name = "../../../img/sudoku.png"
img = cv2.imread(file_name)

gx_k = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
gy_k = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edge_gx = cv2.filter2D(img, -1, gx_k)
edge_gy = cv2.filter2D(img, -1, gy_k)

sobel_x = cv2.Sobel(img, -1, 1, 0, ksize=3)
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize=3)

merged1 = np.hstack((img, edge_gx, edge_gy, edge_gx + edge_gy))
merged2 = np.hstack((img, sobel_x, sobel_y, sobel_x + sobel_y))
merged = np.vstack((merged1, merged2))

cv2.imshow('sobel', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
