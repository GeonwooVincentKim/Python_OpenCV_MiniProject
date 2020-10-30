import cv2
import numpy as np


img = cv2.imread('../../../../img/taekwonv1.jpg')
img2 = img.copy()
draw = img.copy()

pts1 = np.float32([[188, 14], [85, 202], [294, 216]])
pts2 = np.float32([[128, 40], [85, 307], [306, 167]])

x1, y1, w1, h1 = cv2.boundingRect(pts1)
x2, y2, w2, h2 = cv2.boundingRect(pts2)

roi1 = img[y1: y1 + h1, x1: x1 + w1]
roi2 = img[y2: y2 + h2, x2: x2 + w2]
