import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()

ax = figure.add_subplot(1, 1, 1)

ax.plot(np.random.randn(1000).cumsum())

plt.show()
