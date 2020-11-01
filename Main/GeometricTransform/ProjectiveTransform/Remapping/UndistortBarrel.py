import cv2
import numpy as np


img = np.full((300, 400, 3), 255, np.uint8)
img[::10, :, :] = 0
img[:, ::10, :] = 0
width = img.shape[1]
height = img.shape[0]

k1, k2, p1, p2 = 0.001, 0, 0, 0
distCoeff = np.float64([k1, k2, p1, p2])

# Set the random value of Camera Matrix
fx, fy = 10, 10
cx, cy = width / 2, height / 2
camMatrix = np.float32([[fx, 0, cx,
                         0, fy, cy],
                        [0, 0, 1]])

