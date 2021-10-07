import numpy as np
import matplotlib.pyplot as plt

# Define the font dictionary to be applied to all the text in the plot.
font = {'family': 'DejaVu Sans', 'name': 'Times New Roman', 'style': 'italic',
        'color': 'orange', 'weight': 'bold', 'size': 16}

# Define the data for an exponentially decaying curve and plot it.
t = np.linspace(0.0, 5.0, 100)
y = np.sin(2 * np.pi * t) * np.exp(-t/2)
plt.plot(t, y, 'm')

# Define the text, title, and labels, and print them on the plot.
plt.text(x=2, y=0.65, s=r'$\sin(2 \pi t) \exp(-t/2)$', fontdict=font)

plt.title('Damped exponential decay', fontdict=font)

plt.xlabel('time (s)', fontdict=font)
plt.ylabel('voltage (mV)', fontdict=font)

# Adjust the space to prevent clipping of ylabel.
plt.subplots_adjust(left=0.15)

plt.show()
