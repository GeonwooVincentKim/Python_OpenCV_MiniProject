import cv2
import numpy as np


img = cv2.imread("../../../../img/coins_connected.jpg")
rows, cols = img.shape[: 2]
cv2.imshow("original", img)
