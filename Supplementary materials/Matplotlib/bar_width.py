import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width=0.1)

plt.savefig('bar_width.jpg')
plt.show()

# Source: https://www.w3schools.com/python/matplotlib_bars.asp
