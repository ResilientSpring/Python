# class range(stop)
# class range(start, stop, step)
#  If the step argument is omitted, it defaults to 1.
#  If the start argument is omitted, it defaults to 0.

# The advantage of the range type over a regular list or tuple is that
# a range object will always take the same (small) amount of memory
# Reference: https://docs.python.org/3.7/library/stdtypes.html#range

import numpy as np

r = range(0, 20, 2);
print(r);

array = np.array(r);
print(array);
print(array[0]);
print(array[1]);
print(array[2]);

for i in range(3, len(array), 1):
    print(array[i]);

x = np.zeros(10, dtype=int);
print(x);