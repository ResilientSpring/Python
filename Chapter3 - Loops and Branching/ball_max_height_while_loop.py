# Exercise on page 71 of the textbook

# We could alternatively have solved the maximum height problem here by utilizing that
# y[i+1] > y[i] as the ball moves towards the top.

import numpy as np
import matplotlib.pyplot as plt

v0 = 5;   # Initial velocity
g = 9.81; # Acceleration of gravity
t = np.linspace(0, 1, 1000);  # 1000 points in time interval
y = v0 * t - 0.5 * g * t**2;  # Generate 1000 heights.

# At this point, the array y with all the heights is ready,
# and we need to find the largest value within y.

largest_height = y[0]; # Starting value for search

i = 0;
while y[i+1] > y[i]:  # y[i+1] is definitely larger than y[i] before the ball reaches the top.
    i += 1;
    if y[i] > largest_height:
        largest_height = y[i];

print("The largest height achieved was {:g} m".format(largest_height));

# We might also like to plot the path again just to compare.
plt.plot(t, y);
plt.xlabel("Time (s)");
plt.ylabel("Height (m)");
plt.show();