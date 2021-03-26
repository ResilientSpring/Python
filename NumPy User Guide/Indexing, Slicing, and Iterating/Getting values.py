# The syntax for accessing the element of an array is heterogeneous from
# that for slicing an array.

import numpy as np;

def f(x, y):
    return 10 * x + y;

b = np.fromfunction(f, (5, 4), dtype=int);
print(b);

print(b[2][3]);
print(b[2, 3]);