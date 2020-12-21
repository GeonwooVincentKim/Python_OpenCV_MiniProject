import cv2
import numpy as np


img = cv2.imread("../../../img/taekwonv1.jpg")
rows, cols = img.shape[:2]
mask = np.zeros(
    (
        rows + 2,
        cols + 2
    ),
    np.uint8
)

newVal = (255, 255, 255)
loDiff, upDiff = (10, 10, 10), (10, 10, 10)
