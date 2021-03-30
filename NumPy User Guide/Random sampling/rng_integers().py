# Here we use default_rng to create an instance of Generator to
# generate 3 random integers between 0 (inclusive) and 10 (exclusive):
import numpy as np

rng = np.random.default_rng(12345);
random_integers = rng.integers(low=0, high=10, size=3);
print(random_integers);
print(type(random_integers[0]));

# https://numpy.org/doc/stable/reference/random/index.html#quick-start