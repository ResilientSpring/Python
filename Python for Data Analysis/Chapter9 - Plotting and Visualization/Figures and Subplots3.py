import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()

axes1 = figure.add_subplot(2, 2, 1)
axes2 = figure.add_subplot(2, 2, 2)
axes3 = figure.add_subplot(2, 2, 3)

plt.plot(np.random.randn(50).cumsum(), 'k--')

plt.show()
