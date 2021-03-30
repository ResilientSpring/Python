import numpy as np

rng = np.random.default_rng(520);
print(type(rng));

matrix = rng.random(size=(4, 4)); # [1][2]
print(matrix);

# References:
# 1. https://numpy.org/doc/stable/reference/random/generator.html#simple-random-data
# 2. https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random
