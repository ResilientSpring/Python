# Here we use default_rng to create an instance of Generator to generate a random float:
import numpy as np

rng = np.random.default_rng(12345);
print(rng);

random_float = rng.random();
print(random_float);

# Reference:
# https://numpy.org/doc/stable/reference/random/index.html#quick-start