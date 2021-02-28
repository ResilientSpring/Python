# Example on page 25

import matplotlib.pyplot as plt
from numpy import exp
from numpy.core.function_base import linspace

t = linspace(-2, 2, 100);  # Choose 100 points in time interval.

f_values = t ** 2;
g_values = exp(t);

plt.plot(t, f_values, 'r', t, g_values, 'b--');
plt.xlabel('t');
plt.ylabel('f and g');
plt.legend(['t**2', 'e**t']);
plt.title('Plotting of two functions (t**2 and e**t)');
plt.grid('on');
plt.axis([-3, 3, -1, 10]);
plt.show();
