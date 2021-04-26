import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.random.set_seed(1)
np.random.seed(1)

# We generate a toy dataset of 200 training examples with 2 features (x0, x1) drawn from a
# uniform distribution between [-1, 1)
x = np.random.uniform(low=-1, high=1, size=(200, 2))
print(x)

y = np.ones(len(x))
