import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(figsize=(8, 6))
axes = plt.axes()
axes.plot(np.random.randn(1000).cumsum())

ticks = axes.set_xticks([0, 250, 500, 750, 1000])
labels = axes.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')

axes.set_title('My first matplotlib plot')
axes.set_xlabel('Stages')

plt.show()
