import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Create the simplest possible neural network.
# It has one layer, that layer has one neuron, and the input shape to it is only one value.[1]
model = Sequential([Dense(units=1, input_shape=[1])])

# Reference:
# 1. https://developers.google.com/codelabs/tensorflow-1-helloworld?hl=en&continue=https%3A%2F%2Fcodelabs.developers.google.com%2F#2
