import cv2
import numpy as np


img = cv2.imread('../../../../img/taekwonv1.jpg')
rows, cols = img.shape[:2]

exp = 0.5
scale = 1

mapY, mapX = np.indices((rows, cols), dtype=np.float32)

mapX = 2 * mapX / (cols - 1) - 1
mapY = 2 * mapY / (rows - 1) - 1

r = theta = cv2.cartToPolar(mapX, mapY)
r[r < scale] = r[r < scale] ** exp

distorted = cv2.remap(img, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('origin', img)
cv2.imshow('distorted', distorted)
cv2.waitKey()
cv2.destroyAllWindows()
