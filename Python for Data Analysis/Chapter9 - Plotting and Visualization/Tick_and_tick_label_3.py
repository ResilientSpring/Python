import matplotlib.pyplot as plt
import numpy as np

# Call the figure() method via the plt module, which draws an empty figure.
figure = plt.figure()

# Next, call the axes() method, which returns an axes object.
axes = plt.axes()

# You can then call the plot() method from the axes object to create a plot.
axes.plot(np.random.randn(1000).cumsum())

plt.show()
