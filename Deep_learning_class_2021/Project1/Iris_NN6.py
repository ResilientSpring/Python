import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from keras.utils import plot_model
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import numpy as np
from sklearn.metrics import classification_report

iris = load_iris()

iris_data = iris.data
print(iris_data)

iris_label = iris.target
print(iris_label)

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.33,
                                                    random_state=42)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Input's shape
print(X_train.shape)

model = Sequential()

# Feed input's shape to the model.
model.add(keras.Input(shape=(4, )))
model.add(Dense(units=128, activation="relu", name="layer1"))
model.add(Dense(units=64, activation="relu", name="layer2"))
model.add(Dense(units=3, activation="softmax", name="layer3"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# Compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# Train
history = model.fit(x=X_train, y=y_train, epochs=200, batch_size=10, validation_split=0.33)

y_prediction = model.predict(x=X_test)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=y_test, y_pred=y_prediction_bool, target_names=iris.target_names))

