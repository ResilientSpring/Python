import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

plt.plot(randn(30).cumsum(), linestyle='--', color='k', marker='o')

plt.show()
