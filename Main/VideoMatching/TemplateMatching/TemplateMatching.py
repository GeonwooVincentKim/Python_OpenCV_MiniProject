import cv2
import numpy as np


img = cv2.imread("../../../img/figures.jpg")
template = cv2.imread("../../../img/taekwonv1.jpg")
th, tw = template.shape[:2]
cv2.imshow("template", template)

methods = [
    'cv2.TM_CCOEFF_NORMED',
    'cv2.TM_CCORR_NORMED',
    'cv2.TM_SQDIFF_NORMED'
]
