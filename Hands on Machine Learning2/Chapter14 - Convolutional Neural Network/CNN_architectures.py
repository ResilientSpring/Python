from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.datasets import fashion_mnist

(X_train_full, y_train_full), (X_test, y_test) = fashion_mnist.load_data()
X_train, X_valid = X_train_full[:-5000], X_train_full[-5000:]
y_train, y_valid = y_train_full[:-5000], y_train_full[-5000:]

X_mean = X_train.mean(axis=0, keepdims=True)
X_std = X_train.std(axis=0, keepdims=True) + 1e-7
X_train = (X_train - X_mean) / X_std
X_valid = (X_valid - X_mean) / X_std
X_test = (X_test - X_mean) / X_std

X_train = X_train[..., np.newaxis]
X_valid = X_valid[..., np.newaxis]
X_test = X_test[..., np.newaxis]

model = Sequential(
    [Conv2D(filters=64, kernel_size=7, activation='relu', padding='same', input_shape=[28, 28, 1]),
     MaxPooling2D(pool_size=2),
     Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'),
     MaxPooling2D(pool_size=2),
     Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'),
     MaxPooling2D(pool_size=2),
     Flatten(),
     Dense(units=128, activation='relu'),
     Dropout(rate=0.5),
     Dense(units=64, activation='relu'),
     Dropout(rate=0.5),
     Dense(units=10, activation='softmax')])
