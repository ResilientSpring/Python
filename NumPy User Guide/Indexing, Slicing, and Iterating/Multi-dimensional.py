# Multidimensional arrays can have one index per axis.
# These indices are given in a tuple separated by commas:

import numpy as np;

def f(x, y):
    return 10 * x + y;

b = np.fromfunction(f, (5, 4), dtype=int);
print(b);

print(b[2, 3]);

print(b[0 : 5, 1]);  # each row in the second column of b.

print(b[ : , 1]);    # equivalent to the previous example.

print(b[1 : 3, : ]); # each column in the second and third row of b.

print(b[-1, :]);

print(b[-1])  # the last row. Equivalent to b[-1, : ].

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#indexing-slicing-and-iterating