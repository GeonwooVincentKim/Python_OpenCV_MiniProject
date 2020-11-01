import numpy as np
import cv2


img = np.full((300, 400, 3), 255, np.uint8)
img[::10, :, :] = 0
img[:, ::10, :] = 0
width = img.shape[1]
height = img.shape[0]
