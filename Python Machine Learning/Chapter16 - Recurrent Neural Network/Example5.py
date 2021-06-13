import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN

# ## Hidden-recurrence vs. output-recurrence

tf.random.set_seed(1)

rnn_layer = SimpleRNN(units=2, use_bias=True, return_sequences=True,)
rnn_layer.build(input_shape=(None, None, 5))
# A layer is a callable object that takes as input one or more tensors and that outputs one
# or more tensors. It involves computation, defined in the call() method,
# and a state (weight variables), defined either in the constructor __init__() or in the build()
# method.[1]

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

# References:
# 1. https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer