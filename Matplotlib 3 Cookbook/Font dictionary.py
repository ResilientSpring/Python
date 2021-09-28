import numpy as np
import matplotlib.pyplot as plt

# Define the font dictionary to be applied to all the text in the plot.
font = {'family': 'DejaVu Sans', 'name': 'Times New Roman', 'style': 'italic',
        'color': 'orange', 'weight': 'bold', 'size': 16}

# Define the data for an exponentially decaying curve and plot it.
t = np.linspace(0.0, 5.0, 100)
y = np.sin(2 * np.pi * t) * np.exp(-t/2)
plt.plot(t, y, 'm')

#
