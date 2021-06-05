from tensorflow.keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Dropout, MaxPool2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.losses import sparse_categorical_crossentropy

cifar_dataset = cifar10

(training_images, training_labels), (test_images, test_labels) = cifar_dataset.load_data()

training_images, test_images = training_images / 255.0, test_images / 255.0
training_labels, test_labels = training_labels.flatten(), test_labels.flatten()

print(training_labels.shape)
print(training_images.shape)

output_classes = len(set(training_labels))

print('Number of output classes is: ', output_classes)

model = Sequential([Conv2D(filters=32, kernel_size=3, strides=2, activation='relu', input_shape=training_images[0].shape),
                    MaxPool2D(2, 2),
                    Conv2D(filters=64, kernel_size=3, strides=2, activation='relu'),
                    Conv2D(filters=128, kernel_size=3, strides=2, activation='relu'),
                    Flatten(),
                    Dropout(rate=0.2),
                    Dense(units=512, activation='relu'),
                    Dropout(rate=0.2),
                    Dense(units=output_classes, activation='softmax')])

model.compile(optimizer='adam', loss=sparse_categorical_crossentropy, metrics=['accuracy'])

model_history = model.fit(x=training_images, y=training_labels, epochs=20,
                          validation_data=(test_images, test_labels), verbose=1)


