import numpy as np
import matplotlib.pyplot as plt

# Define the data for an exponentially decaying curve and plot it.
t = np.linspace(0.0, 5.0, 100)
y = np.sin(2 * np.pi * t) * np.exp(-t/2)
plt.plot(t, y, 'm')

plt.annotate('local max', xy=(1.3, 0.6),  xycoords='data',
             xytext=(2.8, 0.7), textcoords='data',
             arrowprops=dict(facecolor='black', shrink=0.05),
             horizontalalignment='center', verticalalignment='top',)

plt.show()
