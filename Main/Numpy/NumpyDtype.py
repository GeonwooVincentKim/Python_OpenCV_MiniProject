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
print(a+b)
