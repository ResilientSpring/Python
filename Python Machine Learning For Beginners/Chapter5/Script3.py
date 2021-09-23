import matplotlib.pyplot as plt
import numpy as np
import math

# Set the plot size 8 inches wide and 6 inches tall.
plt.rcParams["figure.figsize"] = [8, 6]

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]

plt.plot(x_vals, y_vals)

plt.show()
