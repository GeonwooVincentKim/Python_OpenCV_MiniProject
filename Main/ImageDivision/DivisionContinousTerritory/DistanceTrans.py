import cv2
import numpy as np


img = cv2.imread("../../../img/full_body.jpg", cv2.IMREAD_GRAYSCALE)
bi_img = cv2.threshold(
    img,
    127, 255,
    cv2.THRESH_BINARY_INV
)
