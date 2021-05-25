import tensorflow as tf
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D

(x_train, train_label), (x_test, test_label) = mnist.load_data()

model = Sequential([Conv2D(filters=32, kernel_size=5, strides=1, padding='same', data_format='channels_last', name='Conv_1', activation='relu')])