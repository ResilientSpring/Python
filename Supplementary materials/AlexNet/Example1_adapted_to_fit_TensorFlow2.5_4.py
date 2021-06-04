import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Dropout, BatchNormalization, Flatten, MaxPool2D
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import Adam
import os
import time

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

validation_images, validation_labels = train_images[:5000], train_labels[:5000]
train_images, train_labels = train_images[5000:], train_labels[5000:]

train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels))
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels))
validation_ds = tf.data.Dataset.from_tensor_slices((validation_images, validation_labels))

def process_images(image, label):
    # Resize images from 32x32 to 277x277 as the AlexNet network input expects a 227x227 image.
    image = tf.image.resize(image, (227, 227))
    image = image / 255.0

    return image, label


# Let’s get the size of each of the dataset partition we created;
# the sizes of the dataset partitions are required to ensure that the dataset is thoroughly
# shuffled before passed through the network.
train_ds_size = tf.data.experimental.cardinality(train_ds).numpy()
test_ds_size = tf.data.experimental.cardinality(test_ds).numpy()
validation_ds_size = tf.data.experimental.cardinality(validation_ds).numpy()
print("Training data size:", train_ds_size)
print("Test data size:", test_ds_size)
print("Validation data size:", validation_ds_size)

# For our basic input/data pipeline, we will conduct three primary operations:
train_ds = (train_ds
            .map(process_images)  # First, preprocessing the data within the dataset
            .shuffle(buffer_size=train_ds_size)  # Second, shuffle the dataset
            .batch(batch_size=32, drop_remainder=True))  # Third, batch data within the dataset
test_ds = (test_ds
           .map(process_images)
           .shuffle(buffer_size=train_ds_size)
           .batch(batch_size=32, drop_remainder=True))
validation_ds = (validation_ds
                 .map(process_images)
                 .shuffle(buffer_size=train_ds_size)
                 .batch(batch_size=32, drop_remainder=True))

# The code snippet represents the Keras implementation of the AlexNet CNN architecture.
model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', input_shape=(227, 227, 3)),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    Flatten(),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(4096, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# To train the network, we have to compile it.
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=Adam(),
              metrics=['accuracy'])

# We can also provide a summary of the network to have more insight into the layer composition
# of the network by running the model.summary()function.
print(model.summary())

# Training the custom AlexNet network is very simple with the Keras module enabled through
# TensorFlow. We simply have to call the fit()method and pass relevant arguments.
model.fit(train_ds,
          epochs=50,
          validation_data=validation_ds,
          validation_freq=1,
          batch_size=2)

# The last official step is to assess the trained network through network evaluation.
# The evaluation phase will provide a performance score of the trained model on unseen data.
y_prediction = model.evaluate(test_ds)

# References:
# 1. https://megalodon.jp/2021-0523-1837-57/https://towardsdatascience.com:443/implementing-alexnet-cnn-architecture-using-tensorflow-2-0-and-keras-2113e090ad98
# 2. https://archive.ph/P1DiU
