from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.layers import Conv2D, Flatten, MaxPool2D, BatchNormalization, Dense, Dropout

model = Sequential([Conv2D(filters=32, kernel_size=3, strides=2, activation=tf.nn.relu,
                           input_shape=[32, 32, 3], data_format='channels_last', name='Conv1'),
                    MaxPool2D(2, 2, name='MaxPool1'),
                    Conv2D(filters=64, kernel_size=3, strides=2, activation=tf.nn.relu,
                           name='Conv2'),
                    Conv2D(filters=128, kernel_size=3, strides=2, activation=tf.nn.relu,
                           name='Conv3'),
                    Flatten(),
                    Dense(units=512, activation=tf.nn.relu),
                    Dense(units=10, activation=tf.nn.softmax)])

model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])

