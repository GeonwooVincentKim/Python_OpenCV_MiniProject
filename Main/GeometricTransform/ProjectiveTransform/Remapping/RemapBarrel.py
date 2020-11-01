import cv2
import numpy as np


k1, k2, k3 = 0.5, 0.2, 0.0

img = cv2.imread('../../../../img/People.jpg')
rows, cols = img.shape[:2]

mapY, mapX = np.indices((rows, cols), dtype=np.float32)

mapX = 2 * mapX / (cols - 1) - 1
mapY = 2 * mapY / (rows - 1) - 1
r, theta = cv2.cartToPolar(mapX, mapY)

ru = r * (1 + k1 * (r ** 2) + k2 * (r ** 4), k3 * (r ** 6))

mapX = mapY = cv2.polarToCart(ru, theta)
mapX = ((mapX + 1) * cols - 1) / 2
mapY = ((mapY + 1) * rows - 1) / 2

distorted = cv2.remap(img, mapX, mapY, cv2.INTER_LINEAR)

cv2.imshow('origin', img)
cv2.imshow('distorted', distorted)
cv2.waitKey()
cv2.destroyAllWindows()
