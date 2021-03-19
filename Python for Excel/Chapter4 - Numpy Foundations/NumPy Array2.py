# First, let's import NumPy
import numpy as np

# Constructing an array with a simple list results in a 1d array
array1 = np.array([10, 100, 1000.]);

# Constructing an array with a nested list results in a 2d array
array2 = np.array([[1., 2., 3.],
                   [4., 5., 6.]]);

print(array1.dtype);

print(float(array1[0]));

print(array2 + 1);