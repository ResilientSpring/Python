# To sample Unif[a, b), b > a
# multiply the output of random by (b-a) and add a:
# (b - a) * random() + a
# [1]
import numpy as np

rng = np.random.default_rng(1234); # Construct a Generator object. [2]

# Three-by-two array of random numbers from [-5, 0):
matrix = (0-(-5)) * rng.random(size=(3, 2)) + (-5);
print(matrix);

# References:
# 1. https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.random.html#numpy-random-generator-random
# 2. https://numpy.org/doc/stable/reference/random/generator.html#random-generator