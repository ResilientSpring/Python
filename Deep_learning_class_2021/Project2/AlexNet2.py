import tensorflow as tf
import keras
from keras.datasets import cifar10
import matplotlib.pyplot as plt
import os
import time
from sklearn.metrics import classification_report
import numpy as np

(train_images, train_labels), (test_images, test_labels) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

validation_images, validation_labels = train_images[:5000], train_labels[:5000]
train_images, train_labels = train_images[5000:], train_labels[5000:]

train_ds = tf.data.Dataset.from_tensor_slices((train_images, train_labels))
test_ds = tf.data.Dataset.from_tensor_slices((test_images, test_labels))
validation_ds = tf.data.Dataset.from_tensor_slices((validation_images, validation_labels))

plt.figure(figsize=(20, 20))
for i, (image, label) in enumerate(train_ds.take(5)):
    ax = plt.subplot(5, 5, i + 1)
    plt.imshow(image)
    plt.title(CLASS_NAMES[label.numpy()[0]])
    plt.axis('off')


def process_images(image, label):
    # Normalize images to have a mean of 0 and standard deviation of 1
    image = tf.image.per_image_standardization(image)

    # Resize images from 32x32 to 277x277 as the AlexNet network input expects a 227x227 image.
    image = tf.image.resize(image, (227, 227))
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
