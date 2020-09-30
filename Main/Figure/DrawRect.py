import cv2

img = cv2.imread('../../img/blank_500.jpg')

cv2.rectangle(img, (50, 50), (150, 150), (255, 0, 0))
cv2.rectangle(img, (300, 300), (100, 100), (255, 0, 0))

