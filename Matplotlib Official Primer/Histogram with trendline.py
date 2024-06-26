import matplotlib.pyplot as plt
import numpy as np

random_state = np.random.RandomState(19680801)
X = random_state.randn(10000)

fig, ax = plt.subplots()
ax.hist(X, bins=25, density=True)
x = np.linspace(-5, 5, 1000)
ax.plot(x, 1 / np.sqrt(2*np.pi) * np.exp(-(x**2)/2), linewidth=4)
ax.set_xticks([])
ax.set_yticks([])

plt.show()

# Reference:
# https://matplotlib.org/stable/gallery/frontpage/histogram.html#sphx-glr-gallery-frontpage-histogram-py
