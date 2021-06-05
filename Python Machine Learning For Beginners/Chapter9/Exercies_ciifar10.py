from tensorflow.keras.datasets import cifar10
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Dropout, MaxPool2D
from tensorflow.keras.models import Sequential

cifar_dataset = cifar10

(training_images, training_labels), (test_images, test_labels) = cifar_dataset.load_data()

training_images, test_images = training_images / 255.0, test_images / 255.0
training_labels, test_labels = training_labels.flatten(), test_labels.flatten()

print(training_labels.shape)
print(training_images.shape)

output_classes = len(set(training_labels))

print('Number of output classes is: ', output_classes)
