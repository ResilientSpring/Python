import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

for i, marker in enumerate(Line2D.markers):
    plt.scatter(x=i%10, y=i, marker=marker, s=100)  # plot each of the markers in size of 100.

plt.show()

