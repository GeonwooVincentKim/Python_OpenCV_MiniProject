import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x ** 2
fig, ax = plt.subplots(nrows=1, ncols=1)
ax.set_facecolor('xkcd:black')
ax.set_facecolor((1.0, 0.47, 0.42))

plt.plot(x, y, 'b')
plt.show()
