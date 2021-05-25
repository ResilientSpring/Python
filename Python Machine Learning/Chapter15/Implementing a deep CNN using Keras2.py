import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from keras.optimizers import Adam
from keras.losses import SparseCategoricalCrossentropy
import numpy as np

(x_train, train_label), (x_test, test_label) = mnist.load_data()

print(x_train.shape)
print(train_label.shape)

x_train = np.expand_dims(x_train, -1)

print(x_train.shape)
