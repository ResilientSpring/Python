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

label_train = []  # [1]
for image, label in tfds.as_numpy(ds_train):
    label_train.append(label)

label_test = []
for image, label in tfds.as_numpy(ds_test):
    label_test.append(label)


print(label_train)
print(label_test)

# flatten is NumPy's method, not Python's list. [2]
# label_train, label_test = label_train.flatten(), label_test.flatten()

label_train = np.array(label_train)
label_test = np.array(label_test)

label_train, label_test = label_train.flatten(), label_test.flatten()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

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

history = model.fit(ds_train, epochs=20)

evaluation = model.evaluate(ds_test)

print(evaluation)

print('\n', 30*"=", '\n')

y_prediction = model.predict(ds_test)

print(y_prediction)

print('\n', 30*"=", '\n')

# Get most likely class. [1]
y_prediction_bool = np.argmax(y_prediction, axis=1)

print(y_prediction_bool)

print(classification_report(y_true=label_test, y_pred=y_prediction_bool, target_names=CLASS_NAMES))

# Reference:
# 1. https://github.com/keras-team/keras/issues/2607#issuecomment-302365916
# 2. https://stackoverflow.com/a/65874930/14900011