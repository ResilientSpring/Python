# Arithmetic operators on arrays apply element-wise.

import numpy as np

a = np.array([20, 30, 40, 50]);
b = np.arange(4);
print(b);

c = a - b;
print(c);

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#basic-operations