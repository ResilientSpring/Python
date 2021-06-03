import tensorflow_datasets as tfds
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Lambda
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import sparse_categorical_crossentropy

dataset = tfds.load(name='cifar10', batch_size=128, as_supervised=True)

cifar10_train = dataset['train'].prefetch(1)

model = Sequential([Flatten(input_shape=(32, 32, 3)),
                    Lambda(lambda images: tf.cast(images, tf.float32)),
                    Dense(units=10, activation='softmax')])

model.compile(loss=sparse_categorical_crossentropy, optimizer=SGD(learning_rate=1e-3),
              metrics=['accuracy'])

model.fit(x=cifar10_train, steps_per_epoch=60000 // 32, epochs=5)
