# Example on page 66 of the textbook
from numpy.core.function_base import linspace

v0 = 4.5;  # initial velocity
g = 9.81;
t = linspace(0, 1, 1000);  # 1000 points in time interval.
y = v0 * t - 0.5 * g * t ** 2;  # Generate all heights.

# Find index where ball approximately has reached y = 0
i = 0;
while y[i] >= 0:
    i = i + 1;

# Since y[i] is the heighy at time t[i], we do know the
# time as well when we have the index i...
print("Time of flight (in seconds): {:g} ".format(t[i]));

# We plot the path again just for comparison.
import matplotlib.pyplot as plt;

plt.plot(t, y);
plt.plot(t, 0 * t, 'g--');
plt.xlabel("Time (s)");
plt.ylabel("Height (m)");
plt.show();
