import cv2
import numpy as np
import matplotlib.pylab as plt


win_name = 'back_projection'
img = cv2.imread('../../../../../img/pump_horse.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
draw = img.copy()


def masking(bp, win_name):
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cv2.filter2D(bp, -1, disc, bp)
    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow(win_name, result)


def backProject_manual(hist_roi):
    hist_img = cv2.calcHist([hsv_img], [0, 1], None, [100, 256], [0, 180, 0, 256])
    hist_rate = hist_roi / (hist_img + 1)
    h, s, v = cv2.split(hsv_img)
    bp = hist_rate(h.ravel(), s.ravel())
    bp = np.minimum(bp, 1)
    masking(bp, 'result_manual')



