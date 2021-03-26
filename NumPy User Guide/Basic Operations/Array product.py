# Unlike in many matrix languages, the product operator * operates elementwise
# in NumPy arrays.
# The matrix product can be performed using the @ operator (in python >=3.5)
# or the dot function or method:

import numpy as np

row1 = [1, 1];
row2 = [0, 1];

row3 = [2, 0];
row4 = [3, 4];

A = np.array([row1, row2]);
B = np.array([row3, row4]);

print(A * B);

# Reference:
# https://numpy.org/devdocs/user/quickstart.html#basic-operations