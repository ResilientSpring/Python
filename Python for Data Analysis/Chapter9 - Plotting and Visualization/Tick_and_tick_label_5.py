import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(figsize=(8, 6))
axes = plt.axes()
axes.plot(np.random.randn(1000).cumsum())
