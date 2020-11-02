    import cv2
    import numpy as np


    win_title = "Liquify"
    half = 50
    isDraggin = False


    def liquify(img, cx1, cy1, cx2, cy2):
        x, y, w, h = cx1 - half, cy1 - half, half * 2, half * 2
        roi = img[y: y + h, x: w + h].copy()
        out = roi.copy()

        offset_cx1, offset_cy1 = cx1 - x, cy1 - y
        offset_cx2, offset_cy2 = cx2 - x, cy2 - y

        tri1 = [[(0, 0), (w, 0), (offset_cx1, offset_cy1)],
                [[0, 0], [0, h], [offset_cx1, offset_cy1]],
                [[w, 0], [offset_cx1, offset_cy1], [w, h]],
                [[0, h], [offset_cx1, offset_cy1], [w, h]]]

        tri2 = [[(0, 0), (w, 0), (offset_cx2, offset_cy2)],
                [[0, 0], [0, h], [offset_cx2, offset_cy2]],
                [[w, 0], [offset_cx2, offset_cy2], [w, h]],
                [[0, h], [offset_cx2, offset_cy2], [w, h]]]

