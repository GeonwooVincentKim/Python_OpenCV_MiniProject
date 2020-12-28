import cv2
import numpy as np


img = cv2.imread("../../../img/taekwonv1.jpg")
img_draw = img.copy()

mask = np.zeros(
    img.shape[:2],
    dtype=np.uint8
)
rect = [0, 0, 0, 0]
mode = cv2.GC_EVAL
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
