import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Dense
from keras.models import Sequential
import keras
from keras.utils import plot_model
from keras.losses import sparse_categorical_crossentropy
from keras.optimizers import Adam

url = "https://raw.githubusercontent.com/ResilientSpring/Python/master/Deep_learning_class_2021/Project1/waveform.data"

# Load dataset
waveform_data = pd.read_csv(filepath_or_buffer=url, header=None)
print(waveform_data)

# Feature set
waveform_feature = waveform_data.iloc[:, 0:21]
print(waveform_feature)
print(waveform_feature.shape)

# Label set
waveform_label = waveform_data.iloc[:, 21]
print(waveform_label)

X_train, X_test, y_train, y_test = train_test_split(waveform_feature, waveform_label,
                                                    test_size=0.33, random_state=42)

model = Sequential()

# Feed input's shape to the model.
model.add(keras.Input(shape=(21, )))
model.add(Dense(units=128, activation="relu", name="layer1"))
model.add(Dense(units=64, activation="relu", name="layer2"))
model.add(Dense(units=3, activation="softmax", name="layer3"))

print(model.summary())

plot_model(model=model, show_shapes=True, show_layer_names=True)

# Compile
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics='accuracy')

# Train
history = model.fit(x=X_train, y=y_train, epochs=100, batch_size=10, validation_split=0.33)

pd.DataFrame(data=history.history).plot(figsize=(8, 5))
plt.grid(True)

plt.ylabel("loss")
plt.xlabel("epoch")
plt.title("model loss")

plt.savefig("Waveform_DNN.jpg")

plt.show()

y_prediction = model.predict(x=X_test)
print(y_prediction)
print(np.mean(y_prediction))

y_prediction_bool = np.argmax(y_prediction, axis=1)

print(classification_report(y_true=y_test, y_pred=y_prediction_bool))