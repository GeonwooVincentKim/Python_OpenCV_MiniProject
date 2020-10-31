import cv2
import numpy as np

l = 20
amp = 15

img = cv2.imread("../../../../img/taekwonv1.jpg")
rows, cols = img.shape[:2]

mapY, mapX = np.indices((rows, cols), dtype=np.float32)
sinX = mapX + amp * np.sin(mapY / l)
cosY = mapY + amp * np.sin(mapX / l)

img_sinX = cv2.remap(img, sinX, mapY, cv2.INTER_LINEAR)
img_cosY = cv2.remap(img, mapX, cosY, cv2.INTER_LINEAR)
img_both = cv2.remap(img, sinX, cosY, cv2.INTER_LINEAR,
                     None, cv2.BORDER_REPLICATE)

cv2.imshow('origin', img)
cv2.imshow('sin x', img_sinX)
cv2.imshow('cos y', img_cosY)
cv2.imshow('sin cos', img_both)

cv2.waitKey()
cv2.destroyAllWindows()
