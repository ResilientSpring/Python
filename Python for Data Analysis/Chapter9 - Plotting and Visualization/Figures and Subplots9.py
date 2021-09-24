import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(nrows=2, ncols=3, figsize=(8, 6))

axes[0, 0].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)
axes[0, 1].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
axes[0, 2].plot(np.random.randn(50).cumsum(), linestyle='--', color='k')
axes[1, 0].plot([1.5, 3.5, -2, 1.6])

plt.show()
