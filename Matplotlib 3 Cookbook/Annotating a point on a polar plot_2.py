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
index = 600
point_r, point_theta = r[index], theta[index]

# the coordinates point_theta and point_r
ax.plot([point_theta], [point_r], 'D', markersize=10)

# Define the annotation for the diamond point
## xy specifies the coordinates of the point to be annotated.
## xytext specifies the coordinates where the text description should be placed.
ax.annotate('a polar annotation', xy=(point_theta, point_r), xytext=(1.0, 0.75),
            textcoords='figure fraction', arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()
