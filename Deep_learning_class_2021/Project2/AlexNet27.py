import tensorflow as tf
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.losses import sparse_categorical_crossentropy, categorical_crossentropy
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Conv2D, Dropout, BatchNormalization, MaxPool2D

data = cifar10

(x_train, train_label), (x_test, test_label) = data.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_data = []
for img in x_train:
    resized_img = cv2.resize(img, (227, 227))
    train_data.append(resized_img)

test_data = []
for img in x_test:
    resized_img = cv2.resize(img, (227, 227))
    test_data.append(resized_img)


train_data = np.array(train_data)
test_data = np.array(test_data)

# train_data = train_data.reshape((train_data.shape[0], 227, 227, 3))
train_data = train_data.reshape(50000, 227, 227, 3)
training_images = train_data / 255.0

# test_data = test_data.reshape((test_data.shape[0], 227, 227, 3))
test_data = test_data.reshape(10000, 227, 227, 3)
test_images = test_data / 255.0

train_label = to_categorical(train_label, num_classes=10)
test_label = to_categorical(test_label, num_classes=10)

model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation=tf.nn.relu,
           data_format='channels_last', input_shape=(32, 32, 3), padding='same'),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'),
    Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation=tf.nn.relu, padding="same"),
    BatchNormalization(),
    MaxPool2D(pool_size=(3, 3), strides=(2, 2), padding='same'),
    Flatten(),
    Dense(4096, activation=tf.nn.relu),
    Dropout(0.5),
    Dense(4096, activation=tf.nn.relu),
    Dropout(0.5),
    Dense(10, activation=tf.nn.softmax)
])

model.compile(loss=categorical_crossentropy,
              optimizer=SGD(learning_rate=0.01, momentum=0.9),
              metrics=['accuracy'])

model.fit(x=train_data, y=train_label, batch_size=128, epochs=20)

model.evaluate(x=test_data)

y_prediction = model.predict(x=test_data)

test_label = np.argmax(test_label, axis=1)

print(classification_report(y_true=test_label, y_pred=np.argmax(y_prediction, axis=1)))
