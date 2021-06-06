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

def preprocessing(image, label):
    image = tf.image.resize(image, [168, 168], preserve_aspect_ratio=True) # 28 x 6 = 168; 28 x 8 = 224
    image = tf.image.rgb_to_grayscale(image) # Reduce the memory usage
    image = tf.cast(image, tf.float32) / 255.0  # convert image to floats in [0, 1] range

    return image, label


AUTO = tf.data.experimental.AUTOTUNE

# Build training pipeline
ds_train = ds_train.map(preprocessing, num_parallel_calls=AUTO)
ds_train = ds_train.cache()
ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples)
ds_train = ds_train.batch(8)# 128 works on GPU too but comes very close to the memory limit of the Colab GPU. [1]
ds_train = ds_train.prefetch(AUTO)

# Build evaluation pipeline
ds_test = ds_test.map(preprocessing, num_parallel_calls=AUTO)
ds_test = ds_test.batch(8) # On Colab/GPU, a higher batch size does not help and sometimes does not fit on the GPU (OOM).[2]
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(AUTO)

print(ds_test)

# Plug the input pipeline into Keras.
model = Sequential([
    Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation=tf.nn.relu,
           data_format='channels_last', input_shape=(168, 168, 1)),
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

model.compile(optimizer=Adam(),
              loss=sparse_categorical_crossentropy,
              metrics=['accuracy'])

history = model.fit(ds_train, epochs=20, validation_data=ds_test)

y_prediction = model.predict(ds_test)

print(y_prediction)

print('\n', 30*"=", '\n')

# Get most likely class. [1]
y_prediction_bool = np.argmax(y_prediction, axis=1)

print(y_prediction_bool)

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship',
               'truck']

print(classification_report(y_true=label_test, y_pred=y_prediction_bool,
                            target_names=CLASS_NAMES))

# References:
# 1. https://colab.research.google.com/github/GoogleCloudPlatform/training-data-analyst/blob/master/courses/fast-and-lean-data-science/04_Keras_Flowers_transfer_learning_solution.ipynb#scrollTo=M3G-2aUBQJ-H&line=4&uniqifier=1
# 2. https://colab.research.google.com/github/GoogleCloudPlatform/training-data-analyst/blob/master/courses/fast-and-lean-data-science/07_Keras_Flowers_TPU_solution.ipynb#scrollTo=M3G-2aUBQJ-H&line=7&uniqifier=1