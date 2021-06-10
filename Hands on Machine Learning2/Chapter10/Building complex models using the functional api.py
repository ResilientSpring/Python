import tensorflow as tf

input = tf.keras.layers.Input(shape=X_train.shape[1:])
hidden1 = tf.keras.layers.Dense(units=30, activation='relu')(input)
hidden2 = tf.keras.layers.Dense(units=30, activation='relu')(hidden1)
concatenation = tf.keras.layers.Concatenate()([input, hidden2])
output = tf.keras.layers.Dense(units=1)

model = tf.keras.Model(inputs=[input], outputs=[output])
