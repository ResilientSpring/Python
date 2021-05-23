from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import keras
from sklearn.metrics import classification_report

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

labels_ = [
    1 if 'airplane' in CLASS_NAMES else 2 if 'automobile' else 3 if 'bird' else 4 if 'cat' else 5 if 'deer' else 6 if 'dog' else 7 if 'frog' else 8 if 'horse' else 9 if 'ship' else 10]

y_train_labels = labels_
y_test_labels = labels_

train_pipeline = tf.data.Dataset.from_tensor_slices((X_train, y_train_labels))
test_pipeline = tf.data.Dataset.from_tensor_slices((X_test, y_test_labels))

# Check if the data is colorful or grayscale, i.e., the number of channels.
plt.figure(figsize=(20, 20))
for i, (image, label) in enumerate(train_pipeline.take(5)):
    ax = plt.subplot(5, 5, i + 1)
    plt.imshow(image)
    plt.title(CLASS_NAMES[label.numpy()[0]])
    plt.axis('off')

plt.savefig('AlexNet.jpg')
plt.show()


def process_images(image, label):
    # Normalize images to have a mean of 0 and standard deviation of 1
    image = tf.image.per_image_standardization(image)

    # Resize images from 32x32 to 277x277 as the AlexNet network input expects a 227x227 image.
    image = tf.image.resize(image, (227, 227))

    return image, label


train_pipeline_size = tf.data.experimental.cardinality(train_pipeline).numpy()
test_pipeline_size = tf.data.experimental.cardinality(test_pipeline).numpy()

# It's a good idea to shuffle your training data if you are training by batches,
# especially if the batch size is small. [1]
train_pipeline = (train_pipeline.map(process_images).batch(batch_size=8, drop_remainder=True).
                  shuffle(buffer_size=train_pipeline_size))

test_pipeline = (test_pipeline.map(process_images).batch(batch_size=8, drop_remainder=True).
                 shuffle(buffer_size=test_pipeline_size))

# The code snippet represents the Keras implementation of the AlexNet CNN architecture.
model = keras.models.Sequential([
    keras.layers.Conv2D(filters=96, kernel_size=(11, 11), strides=(4, 4), activation='relu', input_shape=(227, 227, 3)),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Conv2D(filters=256, kernel_size=(5, 5), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(filters=384, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(filters=256, kernel_size=(3, 3), strides=(1, 1), activation='relu', padding="same"),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPool2D(pool_size=(3, 3), strides=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(4096, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(4096, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(10, activation='softmax')
])

# Compile the model.
model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.optimizers.SGD(lr=0.001),
              metrics=['accuracy'])

model.fit(train_pipeline, epochs=4, validation_split=0.3)

y_prediction = model.predict(x=X_test)

test_label = np.argmax(y_test, axis=1)

print(classification_report(y_true=test_label, y_pred=np.argmax(y_prediction, axis=1)))

# References:
# 1. https://stackoverflow.com/a/41176694/14900011

