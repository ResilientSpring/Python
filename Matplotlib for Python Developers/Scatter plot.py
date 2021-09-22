import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

r = np.random.rand(2, 100)

plt.scatter(r[0], r[1])
