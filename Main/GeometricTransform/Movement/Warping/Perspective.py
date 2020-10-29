import cv2
import numpy as np


file_name = "../../../../img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

pts1 = np.float32([[0, 0], [0, rows], [cols, 0], [cols, rows]])
pts2 = np.float32([[100, 50], [10, rows - 50], [cols - 100, 50], [cols - 10, rows - 50]])

cv2.circle(img, (0, 0), 10, (255, 0, 0), -1)
cv2.circle(img, (0, rows), 10, (0, 255, 0), -1)
cv2.circle(img, (cols, 0), 10, (0, 0, 255), -1)
cv2.circle(img, (cols, rows), 10, (0, 255, 255), -1)

mtrx = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, mtrx, (cols, rows))

cv2.imshow('origin', img)
cv2.imshow('perspective', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
