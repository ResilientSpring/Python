# To see the plot on JetBrain IDEA, see https://www.jetbrains.com/help/pycharm/matplotlib-support.html#sm

from matplotlib.backends.backend_template import show
from matplotlib.pyplot import plot, xlabel, ylabel
from numpy.core.function_base import linspace

v0 = 5;
g = 9.81;
t = linspace(0, 1, 1001);

y = v0*t - 0.5*g*t**2;

plot(t,y);            # plots all y coordinates vs. all t coordinates
xlabel('t (s)');      # places the text t (s) on x-axis
ylabel('y (m)');      # places the text y (m) on y-axis
show();               # displays the figure


