import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN

tf.random.set_seed(1)

rnn_layer = SimpleRNN(units=2, use_bias=True, return_sequences=True)

rnn_layer.build(input_shape=(None, None, 5))

w_xh, w_oo, b_h = rnn_layer.weights

print('W_xh shape:', w_xh.shape)
print('W_oo shape:', w_oo.shape)
print('b_h shape:', b_h.shape)
