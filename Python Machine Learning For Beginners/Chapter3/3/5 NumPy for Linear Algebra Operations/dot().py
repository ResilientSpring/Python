# Script 25

import numpy as np

A = np.random.randn(4, 5);

B = np.random.randn(5, 4);

Z = np.dot(A,B);

print(Z);

# numpy.random.randn()

# If positive int_like arguments are provided, randn generates an array of
# shape (d0, d1, ..., dn), filled with random floats sampled from a univariate “normal”
# (Gaussian) distribution of mean 0 and variance 1.

# Two-by-four array of samples from N(3, 6.25)
# >>> 3 + 2.5 * np.random.randn(2, 4)
# array([[-4.49401501,  4.00950034, -1.81814867,  7.29718677],   # random
#        [ 0.39924804,  4.68456316,  4.99394529,  4.84057254]])  # random

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html