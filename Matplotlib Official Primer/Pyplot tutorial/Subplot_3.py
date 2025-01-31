import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)                # the first figure
plt.subplot(211)             # the first subplot in the first figure

plt.plot([1, 2, 3])

plt.subplot(212)             # the second subplot in the first figure

plt.plot([4, 5, 6])


plt.figure(2)                # a second figure
plt.plot([4, 5, 6])          # creates a subplot() by default

plt.figure(1)                # figure 1 current; subplot(212) still current
plt.subplot(211)             # make subplot(211) in figure1 current
plt.title('Easy as 1, 2, 3') # subplot 211 title

plt.show()

# Source: https://matplotlib.org/stable/tutorials/introductory/pyplot.html#working-with-multiple-figures-and-axes
