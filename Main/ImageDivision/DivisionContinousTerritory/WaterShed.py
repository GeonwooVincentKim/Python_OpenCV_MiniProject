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


def onMouse(event, x, y, flags, param):
    global img_draw, marker, markerID, isDragging

    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        colors.append((
            markerID,
            img[y, x]
        ))

    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            marker[y, x] = markerID
            cv2.circle(
                img_draw,
                (x, y),
                3,
                (0, 0, 255),
                -1
            )

    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            markerID += 1
