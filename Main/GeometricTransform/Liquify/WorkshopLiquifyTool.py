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

    for i in range(4):
        matrix = cv2.getAffineTransform(
            np.float32(tri1[i]), np.float32(tri2[i])
        )
        warped = cv2.warpAffine(
            roi.copy(), matrix, (w, h),
            None, flags=cv2.INTER_LINEAR,
            borderMode=cv2.BORDER_REFLECT_101
        )
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.fillConvexPoly(
            mask, np.int32(tri2[i]),
            (255, 255, 255)
        )

        warped = cv2.bitwise_and(warped, warped, mask=mask)
        out = cv2.bitwise_and(out, out, mask=cv2.bitwise_not(mask))
        out = out + warped

    img[y: y + h, x: x + w] = out
    return img

