import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN

# ## Hidden-recurrence vs. output-recurrence

tf.random.set_seed(1)

rnn_layer = SimpleRNN(units=2, use_bias=True, return_sequences=True)

rnn_layer.build(input_shape=(None, None, 5))

w_xh, w_oo, b_h = rnn_layer.weights

print('W_xh shape:', w_xh.shape)
print('W_oo shape:', w_oo.shape)
print('b_h shape:', b_h.shape)

x_sequence = tf.convert_to_tensor(
    [[1.0]*5, [2.0]*5, [3.0]*5],
    dtype=tf.float32)

x_sequence = tf.reshape(x_sequence, shape=(1, 3, 5))

## output of SimepleRNN:
output = rnn_layer(x_sequence)

print(output)

# Source:
# https://github.com/rasbt/python-machine-learning-book-3rd-edition/blob/master/ch16/ch16_part1.py