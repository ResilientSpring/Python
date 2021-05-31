import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.metrics import SparseCategoricalAccuracy

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Pre-process the data (these are numpy arrays)
X_train = X_train.reshape(60000, 784).astype('float32') / 255
X_test = X_test.reshape(10000, 784).astype('float32') / 255

y_train = y_train.astype('float32')
y_test = y_test.astype('float32')

model = Sequential([InputLayer(input_shape=(784, ), name="digits"),
                    Dense(units=64, activation='relu', name='dense_1'),
                    Dense(units=64, activation='relu', name="dense_2"),
                    Dense(units=10, activation='softmax', name='predictions')])

model.compile(optimizer=RMSprop(), loss=SparseCategoricalCrossentropy(),
              metrics=[SparseCategoricalAccuracy()])

history = model.fit(x=X_train, y=y_train, batch_size=64, epochs=2, validation_split=0.1)

print(history.history)

results = model.evaluate(x=X_test, y=y_test, batch_size=128)
print("Test loss, test acc:", results)

y_predictions = model.predict(x=X_test[:3]) # Generate predictions for 3 samples
print('Predictions shape:', y_predictions.shape)
