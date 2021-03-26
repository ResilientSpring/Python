import numpy as np
a = np.arange(6).reshape((3, 2));
print(a);

b = np.reshape(a, (2, 3)); # C-like index ordering.
print(b);

# Examples
aa = np.array([[1, 2, 3], [4, 5, 6]]);
print(np.reshape(a, 6));
print(np.reshape(a, (3, -1))); # the unspecifiend value is inferred to be 2.

# Reference:
# https://numpy.org/doc/stable/reference/generated/numpy.reshape.html