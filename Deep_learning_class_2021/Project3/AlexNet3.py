from tensorflow.keras.datasets import cifar10
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy, sparse_categorical_crossentropy
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPool2D, Flatten, Dense, Dropout

data = cifar10

(training_images, training_labels), (test_images, test_labels) = data.load_data()

plt.imshow(training_images[0])

plt.show()

print(training_labels[0])
print(training_images[0])

training_images = training_images.reshape(50000, 32, 32, 3)
training_images = training_images / 255.0

test_images = test_images.reshape(10000, 32, 32, 3)
test_images = test_images / 255.0

model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation=tf.nn.relu,
           data_format='channels_last', input_shape=(227, 227, 3)),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'), # Prevent Negative dimension size caused by subtracting 3 from 2 for '{{node max_pooling2d_10/MaxPool}} [1]
    Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'), # [1]
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'), # [1]
    Flatten(),
    Dense(4096, activation=tf.nn.relu),
    Dropout(0.5),
    Dense(4096, activation=tf.nn.relu),
    Dropout(0.5),
    Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer=Adam(), loss=sparse_categorical_crossentropy, metrics=['accuracy'])

history = model.fit(x=training_images, y=training_labels, epochs=20, batch_size=32)

model.evaluate(x=test_images, y=test_labels)

# References:
# 1. https://stackoverflow.com/questions/49079115/valueerror-negative-dimension-size-caused-by-subtracting-2-from-1-for-max-pool