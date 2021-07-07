import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)

plt.savefig('horizontal bars.jpg')
plt.show()

# Source: https://www.w3schools.com/python/matplotlib_bars.asp