import cv2


ksize = 30
win_title = 'mosaic'
img = cv2.imread("../../../img/taekwonv1.jpg")

while True:
    x, y, w, h = cv2.selectROI(win_title, img, False)
