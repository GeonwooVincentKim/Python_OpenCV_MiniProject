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

c = np.reshape(a, (2, 3))
print(c)

d = np.arange(100).reshape(2, -1)
print(d)

e = np.arange(100).reshape(-1, 5)
print(e, e.shape)

f = np.zeros((2, 3))
print(f, f.reshape((6, )), f.reshape(-1), np.ravel(f))

g = np.arange(10).reshape(2, -1)
print(g, g.T)

myList = list(range(10))
print(myList)

for i in range(len(myList)):
    myList[i] = myList[i] + 1
print(myList)

a = np.arange(10)
print(a)
print(a+1)

a = np.arange(5)
print(a)
print(a+5)
print(a-2)
print(a*2)
print(a/2)
print(a**2)

b = np.arange(6).reshape(2, -1)
print(b)
print(b*2)

print(a)
print(a > 2)

a = np.arange(10, 60, 10)
b = np.arange(1, 6)
print(a, b)
print(a+b, a-b, a*b, a/b, a**b)

a = np.ones((2, 3))
b = np.ones((3, 2))
# print(a+b)
print(a, b)

c = np.arange(3)
print(c, a+c)

d = np.arange(2)
# print(a + d)
print(a, d)

d = np.arange(2).reshape(2, 1)
print(d)
print(a + d)

a = np.arange(10)
print(a, a[5])

b = np.arange(12).reshape(3, 4)
print(b, b[1])

print(a)
a[5] = 9
print(a, b)

b[0] = 0
print(b)

b[1, 2] = 99
print(b)

a = np.arange(10)
print(a, a[2:5], a[5:], a[:])

b = np.arange(12).reshape(3, 4)
print(b, b[0:2, 1], b[0:2, 1], b[0:2, 1:3], b[2, :], b[:, 1])

b[0:2, 1:3] = 0
print(b)

bb = b[0:2, 1:3]
print(bb)

bb[0] = 99
print(b)
