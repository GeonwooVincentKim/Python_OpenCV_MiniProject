import cv2
import numpy as np


k1, k2, k3 = 0.5, 0.2, 0.0

img = cv2.imread('../../../../img/People.jpg')
rows, cols = img.shape[:2]

mapY, mapX = np.indices((rows, cols), dtype=np.float32)

mapX = 2 * mapX / (cols - 1) - 1
mapY = 2 * mapY / (rows - 1) - 1
r, theta = cv2.cartToPolar(mapX, mapY)

