import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure()

axes1 = figure.add_subplot(1, 1, 1)

axes1.plot(np.random.randn(1000).cumsum())

plt.show()
