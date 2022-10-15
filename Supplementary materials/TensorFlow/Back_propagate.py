import numpy as np
import tensorflow as tf

np.random.seed(0)

# Sample random numbers from a normal distribution with mean 1 and standard deviation of 0.1.
x_values = np.random.normal(1, 0.1, 100).astype(np.float)

print(x_values)
