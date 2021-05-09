from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
import numpy as np
import keras

cancer_data = load_breast_cancer()

X = cancer_data.data
y = cancer_data.target

print('Input data size: ', X.shape)
print('Output data size: ', y.shape)

# Check to see if it's a binary or multi-class classification.
print('Label names: ', cancer_data.target_names)

# Determine if the data distribution among the dataset is balanced.
n_positive = (y == 1).sum()
n_negative = (y == 0).sum()
print(f'{n_positive} positive samples and {n_negative} negative samples.')

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.33)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

# Input's shape
print(X_train.shape)

model = keras.Sequential()

model.add(keras.Input(shape=(30, )))
model.add(keras.layers.Dense(units=128, activation='relu', name='layer1'))
model.add(keras.layers.Dense(units=64, activation='relu', name='layer2'))
model.add(keras.layers.Dense(units=3, activation='softmax', name='layer3'))

print(model.summary())

keras.utils.plot_model(model=model, show_shapes=True, show_layer_names=True)

# compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# Train
history = model.fit(x=X_train, y=y_train, epochs=200, batch_size=10, validation_split=0.33)

y_prediction = model.predict(x=X_test)

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=y_test, y_pred=y_prediction_bool,
                            target_names=cancer_data.target_names))
