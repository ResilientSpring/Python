import pandas as pd
import Time_Series_Generator
import tensorflow as tf
import matplotlib.pyplot as plt

number_of_steps = 50

series = Time_Series_Generator.generate_time_series(batch_size=10000,
                                                    number_of_steps=number_of_steps + 10)

print(series)
print(series.shape)

X_train, y_train = series[:7000, :number_of_steps], series[:7000, -10, 0]

print(X_train.shape)

X_valid, Y_valid = series[7000:9000, :number_of_steps], series[7000:9000, -10:, 0]
X_test, Y_test = series[9000:, :number_of_steps], series[9000:, -10:, 0]

# X_train_df = pd.DataFrame(data=X_train)
# print(X_train_df)

# series_pd = pd.Series(series)
# print(series_pd)

model = tf.keras.models.Sequential([
    tf.keras.layers.SimpleRNN(20, return_sequences=True, input_shape=[None, 1]),
    tf.keras.layers.SimpleRNN(20),
    tf.keras.layers.Dense(10)
])

model.compile(loss="mse", optimizer="adam")
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_valid, Y_valid))

model.evaluate(X_test, Y_test)

y_prediction = model.predict(x=X_test)

pd.DataFrame(history.history).plot(figsize=(8, 5))
plt.grid(True)
plt.gca().set_ylim(0, 1)
plt.show()
