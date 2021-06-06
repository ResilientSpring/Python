import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy, sparse_categorical_crossentropy
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPool2D, Flatten, Dense, Dropout
from sklearn.metrics import classification_report
import numpy as np

(ds_train, ds_test), ds_info = tfds.load(
    name='cifar10',
    split=['train', 'test'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

# TFDS provide the images as tf.uint8, while the model expect tf.float32, so normalize images
def normalize_img(image, label):
    """Normalizes images: `uint8` -> `float32`."""
    return tf.cast(image, tf.float32) / 255., label


AUTO = tf.data.experimental.AUTOTUNE

# Build training pipeline
ds_train = ds_train.map(normalize_img, num_parallel_calls=AUTO)
ds_train = ds_train.cache()
ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
ds_train = ds_train.batch(128)
ds_train = ds_train.prefetch(AUTO)

# Build evaluation pipeline
ds_test = ds_test.map(normalize_img, num_parallel_calls=AUTO)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(AUTO)

print(ds_test)

label_train = []  # [1]
for i, item in enumerate(ds_train):
    label_train.append(item[1].numpy())

label_test = []
for i, item in enumerate(ds_test):
    label_test.append(item[1].numpy())


print(label_train)
print(label_test)

# Reference:
# 1. https://github.com/rasbt/python-machine-learning-book-3rd-edition/blob/master/ch13/ch13_part2.py
