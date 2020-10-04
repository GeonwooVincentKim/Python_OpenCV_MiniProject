import cv2
import numpy as np


a = np.array([1, 2, 3, 4])
print(a)
print(a.dtype)
print(a.shape)

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)
print(b.shape)

c = np.array([1, 2, 3.14, 4])
print(c)
print(c.dtype)

d = np.array([1, 2, 3, 4], dtype=np.float32)
print(d)

a = np.uint8([1, 2, 3, 4])
print(a)
a = np.empty((2, 3))
print(a)
print(a.dtype)

a.fill(255)
print(a)

b = np.zeros((2, 3))
print(b)
print(b.dtype)

c = np.zeros((2, 3), dtype=np.int8)
print(c)

d = np.ones((2, 3), dtype=np.int16)
print(d)

e = np.full((2, 3, 4), 255, dtype=np.uint8)
print(e)

img = cv2.imread('../../img/People.jpg')
print(img)

print(img.shape)

a = np.empty_like(img)
b = np.zeros_like(img)
c = np.ones_like(img)
d = np.full_like(img, 255)

print(a)
print(a.shape)

print(b)
print(b.shape)

print(c)
print(c.shape)

print(d)
print(d.shape)
