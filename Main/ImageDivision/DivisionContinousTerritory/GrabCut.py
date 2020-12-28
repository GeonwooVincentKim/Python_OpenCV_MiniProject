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


def onMouse(event, x, y, flags, param):
    global mouse_mode, rect, mask, mode
    if event == cv2.EVENT_LBUTTONDOWN:
        if flags <= 1:
            mode = cv2.GC_INIT_WITH_RECT
            rect[:2] = x, y

    elif event == cv2.EVENT_MOUSEMOVE and flags & cv2.EVENT_FLAG_LBUTTON:
        if mode == cv2.GC_INIT_WITH_RECT:
            img_temp = img.copy()
            cv2.rectangle(
                img_temp,
                (
                    rect[0],
                    rect[1]
                ),
                (x, y),
                (0, 255, 0),
                2
            )
            cv2.imshow("img", img_temp)
