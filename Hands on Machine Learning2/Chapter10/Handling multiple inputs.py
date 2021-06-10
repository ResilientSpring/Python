import tensorflow as tf

# You should name at least the most important layers, especially when the model gets
# a bit complex like this.
input_A = tf.keras.layers.Input(shape=[5], name='wide_input')
input_B = tf.keras.layers.Input(shape=[6], name='deep_input')

hidden1 = tf.keras.layers.Dense(units=30, activation='relu')(input_B)
hidden2 = tf.keras.layers.Dense(units=30, activation='relu')(hidden1)
concatenation = tf.keras.layers.Concatenate([input_A, hidden2])
output = tf.keras.layers.Dense(units=1, name='output')(concatenation)

model = tf.keras.Model(inputs=[input_A, input_B], outputs=[output])
