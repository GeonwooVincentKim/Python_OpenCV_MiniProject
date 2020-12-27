import cv2
import numpy as np


img = cv2.imread("../../../img/taekwonv1.jpg")
rows, cols = img.shape[:2]
img_draw = img.copy()

marker = np.zeros(
    (
        rows, cols
    ),
    np.int32
)

markerID = 1
colors = []
isDragging = False
