import numpy as np

arr = np.arange(15).reshape((3, 5));
print(arr);

arr2 = np.transpose(arr);

print(arr2);

# Reference:
# https://numpy.org/doc/stable/reference/generated/numpy.transpose.html