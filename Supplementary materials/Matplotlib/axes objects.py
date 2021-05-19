import matplotlib.pyplot as plt
import numpy as np

plt.plot(np.random.rand(20))
plt.title('test title')

plt.savefig('axes_objects.jpg')

plt.show()

# when we draw a graph using plt:
# A Figure object is generated (shown in green)
# An Axes object is generated implicitly with the plotted line chart (shown in red)
# All the elements of the plot such as x and y-axis are rendered inside the Axes object (shown in blue)

# References:
# 1. https://archive.ph/mWja8
