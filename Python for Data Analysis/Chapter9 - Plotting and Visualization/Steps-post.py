import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

data = np.random.randn(30).cumsum()

plt.plot(data, color='k', linestyle='--', label='default')

plt.plot(data, color='k', linestyle='--', drawstyle='steps-post', label='steps-post')

plt.legend(loc='best')

plt.show()
