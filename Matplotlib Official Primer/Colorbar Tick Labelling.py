import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from numpy.random import randn


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()

data = np.clip(randn(250, 250), -1, 1)

cax = ax.imshow(data, cmap=cm.coolwarm)
ax.set_title('Gaussian noise with vertical colorbar')

# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar

plt.show()

# Source: https://matplotlib.org/stable/gallery/ticks_and_spines/colorbar_tick_labelling_demo.html#sphx-glr-gallery-ticks-and-spines-colorbar-tick-labelling-demo-py
