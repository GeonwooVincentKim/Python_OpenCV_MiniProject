import numpy as np
a = np.arange(5)
print(a, a.dtype)

b = a.astype('float32')
print(b, a.dtype)

c = a.astype(np.float64)
print(c, c.dtype)

print(a.dtype)

d = np.uint8(a)
print(d)

a = np.arange(6)
print(a)

b = a.reshape(2, 3)
print(b)

c = a.reshape(a, (2, 3))
print(c)

d = np.arange(100).reshape(2, -1)
print(d)

e = np.arange(100).reshape(-1, 5)
print(e, e.shape)
