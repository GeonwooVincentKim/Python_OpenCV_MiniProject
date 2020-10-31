import cv2
import numpy as np
import time

img = cv2.imread('../../../../img/People.jpg')
rows, cols = img.shape[:2]

st = time.time()
mFlip = np.float32([[-1, 0, cols - 1], [0, -1, rows - 1]])
flipped1 = cv2.warpAffine(img, mFlip, (cols, rows))
print("Matrix: ", time.time() - st)

