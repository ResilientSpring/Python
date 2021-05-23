from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

train_pipeline = tf.data.Dataset.from_tensor_slices((X_train, y_train))
test_pipeline = tf.data.Dataset.from_tensor_slices((X_test, y_test))

# Check if the data is colorful or grayscale, i.e., the number of channels.
plt.figure(figsize=(20, 20))
for i, (image, label) in enumerate(train_pipeline.take(5)):
    ax = plt.subplot(5, 5, i + 1)
    plt.imshow(image)
    plt.title(CLASS_NAMES[label.numpy()[0]])
    plt.axis('off')

plt.savefig('AlexNet.jpg')
plt.show()


def process_images(image, label):
    # Normalize images to have a mean of 0 and standard deviation of 1
    image = tf.image.per_image_standardization(image)

    # Resize images from 32x32 to 277x277 as the AlexNet network input expects a 227x227 image.
    image = tf.image.resize(image, (227, 227))

    return image, label


train_pipeline_size = tf.data.experimental.cardinality(train_pipeline).numpy()
test_pipeline_size = tf.data.experimental.cardinality(test_pipeline).numpy()

# It's a good idea to shuffle your training data if you are training by batches,
# especially if the batch size is small. [1]
train_pipeline = (train_pipeline.map(process_images).batch(batch_size=32, drop_remainder=True).
                  shuffle(buffer_size=train_pipeline_size))

test_pipeline = (test_pipeline_size)

# References:
# 1. https://stackoverflow.com/a/41176694/14900011