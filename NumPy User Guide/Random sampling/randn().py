import numpy as np

# random.randn(d0, d1, ..., dn)
# Return a sample (or samples) from the “standard normal” distribution
# , as opposed to "uniform" distribution.
# If positive int_like arguments are provided, randn generates an array of
# shape (dimension_0, d1, ..., dn), filled with random floats sampled from a univariate “normal”
# (Gaussian) distribution of mean 0 and variance 1.

# This function takes a tuple to specify the size of the output,
# which is consistent with other NumPy functions like numpy.zeros and numpy.ones.
livelihood = np.random.randn(2, 4);
print(livelihood);

# A single float randomly sampled from the distribution is returned if no argument is provided.
lifeblood = np.random.randn;
print(lifeblood);

lifeblood = np.random.randn();
print(lifeblood);

# Reference:
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
