import Time_Series_Generator as time
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, SimpleRNN
import matplotlib.pyplot as plt
from tensorflow.keras.losses import mean_squared_error
import numpy as np
import tensorflow as tf
import matplotlib as mpl

number_of_steps = 50
series = time.generate_time_series(batch_size=10000, number_of_steps=number_of_steps + 1)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :number_of_steps], series[9000:, -1]

np.random.seed(42)
tf.random.set_seed(42)

model2 = Sequential([SimpleRNN(units=1, input_shape=[None, 1], return_sequences=True)])
model2.compile(loss='mse', optimizer='adam')
history2 = model2.fit(x=X_train, y=y_train, epochs=20, validation_data=(X_valid, y_valid))
model2.evaluate(x=X_test, y=y_test)

plt.figure()
plt.plot(history2.history['loss'])
plt.plot(history2.history['val_loss'])
plt.title('Learning curves')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['loss', 'val_loss'])
plt.show()
