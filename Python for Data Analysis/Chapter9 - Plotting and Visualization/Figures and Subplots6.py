import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()
axes1 = figure.add_subplot(2, 2, 1)
axes2 = figure.add_subplot(2, 2, 2)
axes3 = figure.add_subplot(2, 2, 3)

axes3.plot(np.random.randn(50).cumsum(), linestyle='--', color='k')
axes2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
axes1.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)

plt.show()
