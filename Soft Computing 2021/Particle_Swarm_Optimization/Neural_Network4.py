import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, InputLayer, Input
import tensorflow.keras
import pygad.kerasga
from pygad.kerasga import KerasGA
import numpy
import pygad
from tensorflow.keras.initializers import Ones, ones
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy, MeanAbsoluteError
from tensorflow.keras import Model
from tensorflow.keras.utils import plot_model, pack_x_y_sample_weight
from tensorflow.keras.models import Sequential
from tensorflow.keras.activations import sigmoid
from pygad.kerasga import predict
import pyswarms as ps
from pyswarms.backend.topology import Pyramid
from tensorflow.keras.metrics import Sum


def smooth_L1_loss(y_true, y_pred):
    error = y_true - y_pred
    is_small_error = tf.abs(error) < 1
    squared_loss = tf.square(error) / 2
    linear_loss = tf.abs(error) - 0.5

    return tf.where(is_small_error, squared_loss, linear_loss)


class PSOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.001, momentum=0.9, name="MySGDOptimizer", **kwargs):
        """Call super().__init__() and use _set_hyper() to store hyperparameters"""
        super().__init__(name, **kwargs)
        self._set_hyper("learning_rate", kwargs.get("lr", learning_rate))  # handle lr=learning_rate
        self._set_hyper("decay", self._initial_decay)  #
        self._set_hyper("momentum", momentum)


# Create a Keras model
model = Sequential([InputLayer(input_shape=(2, )),
                    Dense(units=2, use_bias=True, bias_initializer=Ones(), activation=sigmoid),
                    Dense(units=1, use_bias=True, bias_initializer=Ones(), activation=sigmoid)])

model.compile(loss=smooth_L1_loss, optimizer=optimizer, metrics=[Sum(), 'accuracy'])

# XOR problem inputs
data_inputs = numpy.array([[0, 0],
                           [0, 1],
                           [1, 0],
                           [1, 1]])

# XOR problem outputs
data_outputs = numpy.array([[0],
                            [1],
                            [1],
                            [0]])

history = model.fit(x=data_inputs, y=data_outputs, epochs=100, shuffle=True)

