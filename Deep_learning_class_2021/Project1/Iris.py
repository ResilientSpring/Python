import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.utils import plot_model

iris = load_iris()
iris_data=iris.data
print(iris_data)
X_train, X_test, y_train, y_test = train_test_split(iris_data, iris.target, test_size=0.2);

print(X_train.shape)

model = Sequential()

# Feed input's shape to the model.
model.add(keras.Input(shape=(4, )))
model.add(Dense(units=128, activation="relu"))
model.add(Dense(units=64, activation="relu"))
model.add(Dense(units=3, activation="softmax"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# Compile
model.compile(optimizer=keras.optimizers.SGD(), loss=keras.losses.BinaryCrossentropy(),
              metrics=[keras.metrics.BinaryAccuracy()])