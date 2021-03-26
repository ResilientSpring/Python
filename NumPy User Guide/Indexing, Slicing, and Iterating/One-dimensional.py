# One-dimensional arrays can be indexed, sliced and iterated over,
# much like lists and other Python sequences.

import numpy as np

a = np.arange(10)**3;
print(a);

print(a[2]);

print(a[2:5]);

# equivalent to a[0:6:2] = 1000;
# from start to position 6, exclusive, set every 2nd element to 1000.
a[ : 6 : 2] = 1000;
print(a);

b = a[ : : -1]; # reversed a
print(b, a);

for i in a:
    print(i ** (1 / 3.));

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#indexing-slicing-and-iterating