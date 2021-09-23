import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r

ax.plot(theta, r, color=[0.9, 0.4, 0.7], lw=3)

# Plot a point with diamond marker at the 600 point on the polar curve.
ind = 600
pointr, pointtheta = r[ind], theta[ind]

ax.plot([pointtheta], [pointr], 'D', markersize=10)

# Define the annotation for the diamond point
ax.annotate('a polar annotation', xy=(pointtheta, pointr), xytext=(1.0, 0.75),
            textcoords='figure fraction', arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')

plt.show()
