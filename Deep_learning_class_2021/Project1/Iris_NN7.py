import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
from keras.utils import plot_model
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import numpy as np
from sklearn.metrics import classification_report, accuracy_score

iris = load_iris()

iris_data = iris.data
print(iris_data)

iris_label = iris.target
print(iris_label)

X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, test_size=0.33,
                                                    random_state=42)

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
history = model.fit(x=X_train, y=y_train, epochs=100, batch_size=10, validation_split=0.33)

y_prediction = model.predict(x=X_test)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print("Classification report: ", '\n',
      classification_report(y_true=y_test, y_pred=y_prediction_bool,
                            target_names=iris.target_names))
print("Accuracy", accuracy_score(y_true=y_test, y_pred=y_prediction))

scores = cross_val_score(estimator=model, X=X_train, y=y_train, scoring='accuracy', cv=10)

print("10-fold cross validation Scores: ", scores)
print("Mean Scores: ", scores.mean())

y_prediction2 = model.predict(x=X_train)

y_prediction2_bool = np.argmax(y_prediction2, axis=1)

print("Classification report after cross validation: ", '\n',
      classification_report(y_true=y_train, y_pred=y_prediction2_bool,
                            target_names=iris.target_names))
