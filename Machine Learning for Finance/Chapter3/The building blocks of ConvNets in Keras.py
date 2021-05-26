from keras.datasets import mnist
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, Activation, MaxPool2D, Flatten, Dense
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# MNIST characters are black and white, so the data shape usually doesn't include color channels:
print(X_train.shape)

# Expand data dimensions to show that it has only one-color channel.
X_train = np.expand_dims(X_train, axis=-1)

X_test = np.expand_dims(X_test, axis=-1)

print(X_train.shape)
print(X_test.shape)

model = Sequential([Conv2D(filters=6, kernel_size=3, strides=1, padding='valid',
                           input_shape=(28, 28, 1), data_format='channels_last', activation='relu'),
                    MaxPool2D(pool_size=2, strides=2),
                    Conv2D(filters=12, kernel_size=3, activation='relu'),
                    MaxPool2D(pool_size=2, strides=2),
                    Flatten(),
                    Dense(units=10, activation='softmax')])

print(model.summary())

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(x=X_train, y=y_train, batch_size=32, epochs=5,
                    validation_data=(X_test, y_test))

fig, ax = plt.subplots(figsize=(10, 6))

gen = ax.plot(history.history['val_accuracy'], label='Validation_Accuracy')

fr = ax.plot(history.history['accuracy'], dashes=[5, 2], label='Training Accuracy')

legend = ax.legend(loc='lower center', shadow=True)

plt.savefig('learning_curves.jpg')

plt.show()
