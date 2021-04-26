import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.utils import plot_model
from mlxtend.plotting import plot_decision_regions

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
## label set (0- 99)
y_train = y[:100]

## the feature set for validation (100 - 199)
x_valid = x[100:, :]

## the label set for validation (100 - 199)
y_valid = y[100:]

# Construct a feedforward NN with three hidden layers.
model = keras.Sequential()
model.add(keras.layers.Dense(units=4, input_shape=(2, ), activation="relu"))
model.add(keras.layers.Dense(units=4, activation="relu"))
model.add(keras.layers.Dense(units=4, activation="relu"))
model.add(keras.layers.Dense(units=1, activation="sigmoid"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)
