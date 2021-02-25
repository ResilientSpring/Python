from numpy.core.function_base import linspace

import matplotlib.pyplot as plt;

l = 4;
v = l ** 3;

array = linspace(1, 3, 3);

print(array);
print(v);

l2 = linspace(1, 3, 3);
v2 = 1*2*3;

plt.plot(v2, l2);
plt.xlabel('Volume');
plt.ylabel('Length');
plt.show();