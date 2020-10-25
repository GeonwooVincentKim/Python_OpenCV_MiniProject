import cv2
import numpy as np


alpha_width_rate = 15

img_face = cv2.imread('../../../../img/man_face.jpg')
img_skull = cv2.imread('../../../../img/skull.jpg')

img_comp = np.zeros_like(img_face)
