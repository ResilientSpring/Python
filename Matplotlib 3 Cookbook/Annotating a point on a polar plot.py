import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

# Define the axes and declares it as a polar plot. (You can also use polar=True)
ax = fig.add_subplot(111, projection='polar')

# r and theta set the data for radius, and the angle for the plot of the polar coordinates.
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r

# Plot the polar chart with theta and r.
ax.plot(theta, r, color=[0.9, 0.4, 0.7], lw=3) # lw = line width
# color is specified with R, G, and B color values to create a custom color.
# R, G, and B values vary from 0 (dark) to 1 (bright).

# Plot a point with diamond marker at the 600 point on the polar curve.
ind = 600
pointr, pointtheta = r[ind], theta[ind]

ax.plot([pointtheta], [pointr], 'D', markersize=10)

# Define the annotation for the diamond point
ax.annotate('a polar annotation', xy=(pointtheta, pointr), xytext=(1.0, 0.75),
            textcoords='figure fraction', arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()
