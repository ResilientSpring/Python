import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="#4CAF50")
plt.show()

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color="hotpink")
plt.show()

plt.bar(x, y, color = "red")
plt.show()

# Source: https://www.w3schools.com/python/matplotlib_bars.asp