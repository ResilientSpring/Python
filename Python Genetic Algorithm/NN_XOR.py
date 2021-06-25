import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, InputLayer, Input
import tensorflow.keras
import pygad.kerasga
import numpy
import pygad
from tensorflow.keras.initializers import Ones, ones
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy, MeanAbsoluteError
from tensorflow.keras.activations import sigmoid
from tensorflow.keras import Model
from tensorflow.keras.utils import plot_model, pack_x_y_sample_weight
from tensorflow.keras.models import Sequential


# Create a Keras model
model = Sequential([])