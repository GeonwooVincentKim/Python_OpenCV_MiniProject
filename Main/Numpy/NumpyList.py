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
