import tensorflow as tf

input_A = tf.keras.layers.Input(shape=[5], name='Input_A')
input_B = tf.keras.layers.Input(shape=[6], name='Input_B')
hidden1 = tf.keras.layers.Dense(units=30, activation='relu')
hidden2 = tf.keras.layers.Dense(units=30, activation='relu')
concatenation = tf.keras.layers.Concatenate([input_A, hidden2])
output = tf.keras.layers.Dense(units=1, name='main_output')(concatenation)

auxiliary_output = tf.keras.layers.Dense(units=1, name='auxiliary output')(hidden2)

model = tf.keras.Model(inputs=[input_A, input_B], outputs=[output, auxiliary_output])
