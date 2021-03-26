# Multidimensional arrays can have one index per axis.
# These indices are given in a tuple separated by commas:

import numpy as np;

def f(x, y):
    return 10 * x + y;

b = np.fromfunction(f, (5, 4), dtype=int);
print(b);

print(b[2, 3]);