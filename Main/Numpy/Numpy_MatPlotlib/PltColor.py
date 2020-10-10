import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = x ** 2
fig, ax = plt.subplots(nrows=1, ncols=1)
plt.plot(x, y, 'b')
ax.set_facecolor('xkcd:black')
ax.set_facecolor((1.0, 0.47, 0.42))
plt.show()
