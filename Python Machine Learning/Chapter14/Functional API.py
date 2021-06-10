
import tensorflow as tf
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.losses import BinaryCrossentropy
from tensorflow.keras.metrics import BinaryAccuracy
import numpy as np

tf.random.set_seed(1)

X = np.random.uniform(low=-1, high=1, size=(200, 2))
print(X)

y = np.ones(len(X))
print(y)

# if X0 * X1 <0, y = 0
y[X[:,0] * X[:, 1] < 0] = 0

X_train = X[:100, :]
y_train = y[:100]
X_valid = X[100:, :]
y_valid = y[100:]

# Input layer
inputs = tf.keras.Input(shape=(2, ))

# Hidden layers
hidden1 = tf.keras.layers.Dense(units=4, activation='relu')(inputs)
hidden2 = tf.keras.layers.Dense(units=4, activation='relu')(hidden1)
hidden3 = tf.keras.layers.Dense(units=4, activation='relu')(hidden2)

outputs = tf.keras.layers.Dense(units=1, activation='sigmoid')(hidden3)

# Construct a model
model = tf.keras.Model(inputs=inputs, outputs=outputs)

print(model.summary())

# Compile the model
model.compile(optimizer=SGD(),
              loss=BinaryCrossentropy(),
              metrics=[BinaryAccuracy()])

# Train the model
history = model.fit(x=X_train, y=y_train,
                    validation_data=(X_valid, y_valid),
                    epochs=200, batch_size=2, verbose=0)

