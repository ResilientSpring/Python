import tensorflow as tf
from tensorflow import keras

fashion_mnist = keras.datasets.fashion_mnist

(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()

print(X_train_full.shape)
print(X_train_full.dtype)

# Create their validation sets and scale them down to 0-1 by dividing them by 255.0
X_valid, X_train = X_train_full[:5000] / 255.0, X_train_full[5000:]

y_valid, y_train = y_train_full[:5000], y_train_full[5000:]

# List the class names to know what we are dealing with:
class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Scandal", "Shirt",
              "Sneaker", "Bag", "Angle boot"]

## The first image in the training set represents a coat:
print(class_names[y_train[0]])