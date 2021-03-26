import numpy as np

array_example = np.array([[[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0, 1, 2, 3], [4, 5, 6, 7]],
                          [[0, 1, 2, 3], [4, 5, 6, 7]]]);

# shape will display a tuple of integers that indicate the number of elements stored
# along each dimension of the array.
# If, for example, you have a 2-D array with 2 rows and 3 columns,
# the shape of your array if (2, 3).
print(array_example.shape);

# Reference:
# https://numpy.org/devdocs/user/absolute_beginners.html#how-do-you-know-the-shape-and-size-of-an-array
