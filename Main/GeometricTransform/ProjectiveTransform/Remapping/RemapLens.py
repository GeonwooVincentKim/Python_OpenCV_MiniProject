import cv2
import numpy as np


img = cv2.imread('../../../../img/taekwonv1.jpg')
rows, cols = img.shape[:2]

exp = 0.5
scale = 1

mapY, mapX = np.incides((rows, cols), dtype=np.float32)

mapX = 2 * mapX / (cols - 1) - 1
mapY = 2 * mapY / (rows - 1) - 1

r = theta = cv2.cartToPolar(mapX, mapY)
r[r < scale] = r[r < scale] ** exp
