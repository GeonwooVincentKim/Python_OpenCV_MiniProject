import cv2
img = cv2.imread('../../img/blank_500.jpg')
type(img)

print(img.ndim)
print(img.shape)
print(img.dtype)
print(img.itemsize)
