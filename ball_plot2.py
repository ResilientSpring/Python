# To see the plot on JetBrain IDEA, see https://www.jetbrains.com/help/pycharm/matplotlib-support.html#sm

from numpy.core.function_base import linspace

# The standard import statement, including "nickname", is as follows.
import matplotlib.pyplot as plt;  # Refer to <Programming for Computations - Python, Second Edition> page on 19.

v0 = 5;
g = 9.81;

# linspace(a, b, n) shows when n evenly spaced floating point numbers are sought on an interval [a,b]
t = linspace(0, 1, 1001);
# The object returned from linspace is an array of number.

# When we start computing with t in the right hand side in the following expression,
y = v0 * t - 0.5 * g * t ** 2;
# the right hand side is computed for every number in array t, yielding the results stored as an array.

plt.plot(t, y);  # plots all y coordinates vs. all t coordinates
plt.xlabel('t (s)');  # places the text t (s) on x-axis
plt.ylabel('y (m)');  # places the text y (m) on y-axis
plt.show();  # displays the figure
