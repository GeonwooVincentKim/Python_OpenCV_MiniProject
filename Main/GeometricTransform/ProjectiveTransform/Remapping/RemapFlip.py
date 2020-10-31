import cv2
import numpy as np
import time

img = cv2.imread('../../../../img/People.jpg')
rows, cols = img.shape[:2]

st = time.time()
mFlip = np.float32([[-1, 0, cols - 1], [0, -1, rows - 1]])
flipped1 = cv2.warpAffine(img, mFlip, (cols, rows))
print("Matrix: ", time.time() - st)

st2 = time.time()
mapY, mapX = np.indices((rows, cols), dtype=np.float32)
mapX = cols - mapX - 1
mapY = cols - mapY - 1
flipped2 = cv2.remap(img, mapX, mapY, cv2.INTER_LINEAR)
print("Remap: ", time.time() - st2)

cv2.imshow("origin", img)
cv2.imshow("flipped1", flipped1)
cv2.imshow("flipped2", flipped2)
cv2.waitKey()
cv2.destroyAllWindows()

