import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import plot_model
from mlxtend.plotting import plot_decision_regions
from keras.layers import Dense
from keras import Input

tf.random.set_seed(1)
np.random.seed(1)

# We generate a toy dataset of 200 training examples with 2 features (x0, x1) drawn from a
# uniform distribution between [-1, 1)
x = np.random.uniform(low=-1, high=1, size=(200, 2))
print(x)

# Assign the ground truth label
y = np.ones(len(x))
print(y)

## Applying the threshold rule:
y[x[:, 0] * x[:, 1] < 0] = 0

# Use half of the data (100 training examples) for training and the remaining half for
# validation
## feature set (0 - 99)
x_train = x[:100, :]
print(x_train)
print(x_train.shape)

## label set (0- 99)
y_train = y[:100]
print(y_train)
print(y_train.shape)

## the feature set for validation (100 - 199)
x_valid = x[100:, :]

## the label set for validation (100 - 199)
y_valid = y[100:]

fig = plt.figure(figsize=(6, 6))
plt.plot(x[y == 0, 0], x[y == 0, 1], 'o', alpha=0.75, markersize=10)
plt.plot(x[y == 1, 0], x[y == 1, 1], '<', alpha=0.75, markersize=10)
plt.xlabel(r'$x_1$', size=15)
plt.ylabel(r'$x_2$', size=15)
plt.show()