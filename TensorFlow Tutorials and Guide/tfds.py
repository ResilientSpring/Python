import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy, sparse_categorical_crossentropy
from tensorflow.keras.layers import Conv2D, BatchNormalization, MaxPool2D, Flatten, Dense, Dropout
from tensorflow.keras.metrics import sparse_categorical_accuracy

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

# Plug the input pipeline into Keras.
model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation=tf.nn.relu,
           data_format='channels_last', input_shape=(32, 32, 3)),
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

model.compile(optimizer=Adam(0.001),
              loss=sparse_categorical_crossentropy,
              metrics=['accuracy'])

model.fit(
    ds_train,
    epochs=6,
    validation_data=ds_test,
)

# Reference:
# 1. https://www.tensorflow.org/datasets/keras_example
# 2. https://www.tensorflow.org/datasets/overview
