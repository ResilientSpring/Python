import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

n = [0, 1, 2, 3, 4]

s = [i**2 * 100 + 100 for i in n]

# Prepare a list of colors
c = ['red', 'orange', 'yellow', 'green', ' blue']

# Draw a scatter plot of n points, with sizes in s and colors in c
plt.scatter(x=n, y=n, s=s, cmap=c)

# Draw a line plot, with n points of black cross markers of size 12
plt.plot(n, marker='x', color='black', ms=12)

# Set axis limits to show the markers completely.
plt.xlim(-0.5, 4.5)
plt.ylim(-1, 5)

plt.show()
