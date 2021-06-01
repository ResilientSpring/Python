from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt

data = cifar10

(training_images, training_labels), (test_images, test_labels) = data.load_data()

plt.imshow(training_images[0])

plt.show()

print(training_labels[0])
print(training_images[0])
