from numpy.core.function_base import linspace

import matplotlib.pyplot as plt;

l = 4;
v = l ** 3;

array = linspace(1, 3, 3);

print(array);
print(v);

plt.plot(v, l);