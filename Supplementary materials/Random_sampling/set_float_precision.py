# For random float numbers both positive
# and negative with a precision of 1 you can use:

import numpy as np

array = np.random.uniform(-100, 100, size=10);
print(array);

np.set_printoptions(precision=1);
print(array);

# Source: https://stackoverflow.com/a/55020984/14900011