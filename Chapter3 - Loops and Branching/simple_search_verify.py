# Exercise 3.9 on page 75 of the textbook.

import numpy as np
import matplotlib.pyplot as plt

v0 = 5;   # Initial velocity
g = 9.81; # Acceleration of gravity
t = np.array([0, 1, 2, 3, 4]);
y = v0 * t - 0.5 * g * t**2;

print(t);
print(y);

largest_height = y[0]; # Starting value for search
for i in range (0, len(y), 1):
    print("The ball was at {:.2f} meter at the {:d} second upon taking flight.".format(y[i], t[i]));
    if y[i] > largest_height:
        largest_height = y[i];
    print("The largest height in this round of for loop is {:.3f} meter.".format(largest_height));

print("The largest height achieved was {:g} m".format(largest_height));

# We might also like to plot the path again just to compare.
plt.plot(t, y);
plt.xlabel("Time (s)");
plt.ylabel("Height (m)");
plt.grid("ON");
plt.show();