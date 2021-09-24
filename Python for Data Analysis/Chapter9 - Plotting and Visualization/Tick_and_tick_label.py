import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

axes[1, 1].plot(np.random.randn(1000).cumsum())

plt.show()
