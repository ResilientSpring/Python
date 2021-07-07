import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

x = np.arange(3)
plt.bar(x, height=[1, 2, 3])
plt.xticks(x, ['a', 'b', 'c'])

plt.show()

# Source: https://stackoverflow.com/a/33203848