import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

tf.random.set_seed(1)
np.random.seed(1)

X = np.random.uniform(low=-1, high=1, size=(200, 2))
print(X)

y = np.ones(len(X))
print(y)
