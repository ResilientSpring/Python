# Create a multidimensional array with random.generator.

import numpy as np

rng = np.random.default_rng(520); # 520 is a seed. [1]
array = rng.integers(low=0, high=10, size=(5, 2), dtype=int, endpoint=True); # [2]
print(array);


# Reference:
# 1. https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng
# 2. https://numpy.org/doc/stable/reference/random/generator.html#simple-random-data