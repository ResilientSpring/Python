import numpy as np
import tensorflow as tf
import random as python_random

np.random.seed(42)
python_random.seed(42)
tf.random.set_seed(42)

'''adapted from Supplementary materials/Keras/Obtaining reproducible results.py'''

# Rest of code follows ...
from keras.layers import Dense
import keras

# Create a keras sequential model by passing a list of layer instances to the model constructor.
# The passed layer instances include two fully connected layers with 20 and 8 nodes, respectively.
model = \
    keras.Sequential([Dense(units=20, activation='relu'), Dense(units=8, activation='relu'),
                      Dense(units=1)])

# Compile the model.
model.compile(loss='mean_squared_error', optimizer=keras.optimizers.Adam(learning_rate=0.02))

import dataset

model.fit(x=dataset.X_train, y=dataset.y_train, epochs=300)
