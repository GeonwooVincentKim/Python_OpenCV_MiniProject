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

offset1 = np.zeros((3, 2), dtype=np.float32)
offset2 = np.zeros((3, 2), dtype=np.float32)

for i in range(3):
    offset1[i][0], offset2[i][1] = pts1[i][0] - x1, pts2[i][1] - y1
    offset1[i][0], offset2[i][1] = pts1[i][0] - x2, pts2[i][1] - y2


mtrx = cv2.getAffineTransform(offset1, offset2)
warped = cv2.warpAffine(roi1, mtrx, (w2, h2), None,
                        cv2.INTER_LINEAR, cv2.BORDER_REFLECT_101)

mask = np.zeros([h2, w2], dtype=np.uint8)
cv2.fillConvexPoly(mask, np.int32(offset2), (255))

