import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

custom_markers = ['$'+x+'$' for x in ['\$', '\%', '\clubsuit', '\sigma', '😎']]

for i, marker in enumerate(custom_markers):
    plt.scatter(i%10, i, marker=marker, s=500) # plot each of the markers in size of 100

plt.show()
