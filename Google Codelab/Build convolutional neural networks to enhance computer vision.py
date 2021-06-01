import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.losses import SparseCategoricalCrossentropy

mnist = fashion_mnist

(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = training_images.reshape(60000, 28, 28, 1)
training_images = training_images / 255.0

test_images = test_images.reshape(10000, 28, 28, 1)
test_images = test_images / 255.0

model = Sequential([Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=(28, 28, 1)),
                    MaxPooling2D(pool_size=2),
                    Conv2D(filters=64, kernel_size=3, activation='relu'),
                    MaxPooling2D(pool_size=2),
                    Flatten(),
                    Dense(units=128, activation='relu'),
                    Dense(units=10, activation='softmax')])

model.compile(optimizer='adam', loss=SparseCategoricalCrossentropy(), metrics=['accuracy'])

model.summary()

model.fit(x=training_images, y=training_labels, epochs=5)

test_loss, test_accuracy = model.evaluate(x=test_images, y=test_labels)

print('Test loss: {}, Test accuracy: {}'.format(test_loss, test_accuracy * 100))
