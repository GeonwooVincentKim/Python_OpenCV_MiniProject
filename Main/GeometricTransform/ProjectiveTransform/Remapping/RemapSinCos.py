import cv2
import numpy as np

l = 20
amp = 15

img = cv2.imread("../../../../img/taekwonv1.jpg")
rows, cols = img.shape[:2]

mapY, mapX = np.indices((rows, cols), dtype=np.float32)
sinX = mapX + amp * np.sin(mapY / l)
sinY = mapY + amp * np.sin(mapX / l)
