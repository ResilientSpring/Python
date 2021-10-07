import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(num=1, figsize=(8, 6),)
axes = plt.axes()
axes.plot(np.random.randn(1000).cumsum())

axes.set_xticks([0, 250, 500, 750, 1000])
axes.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize='small')

axes.set_yticks([0, 10, 20, 30, 40, 50, 60])
axes.set_yticklabels(['0.0', '10.0', '20.0', '30.0', '40.0', '50.0', '60.0'])

plt.show()
