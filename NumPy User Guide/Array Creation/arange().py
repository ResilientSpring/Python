# To create sequences of numbers, NumPy provides the arange function
# which is analogous to the Python built-in range, but returns an array.

import numpy as np

array1 = np.arange(10, 30, 5);
print(array1);

array2 = np.arange(0, 2, 0.3); # it accepts float arguments.
print(array2);

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#array-creation