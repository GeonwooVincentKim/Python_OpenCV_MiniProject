import cv2
import numpy as np


img = cv2.imread("../../../img/full_body.jpg", cv2.IMREAD_GRAYSCALE)
bi_img = cv2.threshold(
    img,
    127, 255,
    cv2.THRESH_BINARY_INV
)

dst = cv2.distanceTransform(
    bi_img,
    cv2.DIST_L2,
    5
)

dst = dst / (
    dst.max()
    - dst.min()
    * 255
).astype(
    np.uint8
)

skeleton = cv2.adaptiveThreshold(
    dst,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    7,
    -3
)
