# New code should use the standard_normal method of a default_rng() instance; [1]
from numpy.random import default_rng

rng = default_rng();
vals = rng.standard_normal(10);
print(vals);

# instead of this (legacy version) [2]
from numpy import random
vals2 = random.standard_normal(10);
print(vals2);

# References:
# 1. https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
# 2. https://numpy.org/doc/stable/reference/random/index.html#quick-start