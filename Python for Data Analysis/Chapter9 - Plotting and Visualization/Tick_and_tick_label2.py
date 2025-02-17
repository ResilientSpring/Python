import matplotlib.pyplot as plt
import numpy as np

# There is no need to follow figure, axes = plt.subplots()
# if you are not planning to plot multiple subplots in the same figure.

plt.rcParams["figure.figsize"] = [8, 6]

plt.plot(np.random.randn(1000).cumsum())

plt.show()
