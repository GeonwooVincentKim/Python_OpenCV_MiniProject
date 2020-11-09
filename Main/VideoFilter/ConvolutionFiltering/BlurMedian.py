import cv2
import numpy as np


img = cv2.imread("../../../img/salt_pepper_noise.jpg")

blur = cv2.medianBlur(img, 5)

