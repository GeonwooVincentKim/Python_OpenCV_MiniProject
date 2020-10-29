import cv2
import numpy as np


win_name = "scanning"
img = cv2.imread('../../../../img/paper.jpg')
rows, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4, 2), dtype=np.float32)


def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        pts[pts_cnt] = [x, y]
        pts_cnt = 1
