# Exercise 3.9 on page 75 of the textbook.

import numpy as np
import matplotlib.pyplot as plt

v0 = 5;   # Initial velocity
g = 9.81; # Acceleration of gravity
t = [1, 2, 3, 4];
y = v0 * t - 0.5 * g * t**2;

largest_height = y[0]; # Starting value for search
for i in range (1, len(y), 1):
    if y[i] > largest_height:
        largest_height = y[i];

print("The largest height achieved was {:g} m".format(largest_height));

# We might also like to plot the path again just to compare.
plt.plot(t, y);
plt.xlabel("Time (s)");
plt.ylabel("Height (m)");
plt.show();