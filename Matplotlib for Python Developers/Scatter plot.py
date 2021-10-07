import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

r = np.random.rand(2, 100)

# Plot the x and y coordinates of the random dots on a scatter plot
plt.scatter(r[0], r[1])

plt.show()
