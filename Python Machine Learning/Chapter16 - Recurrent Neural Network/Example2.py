import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd
import os
from collections import Counter
from tensorflow.keras.layers import Embedding
from tensorflow.keras import Sequential
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

# ## Hidden-recurrence vs. output-recurrence

tf.random.set_seed(1)

rnn_layer = SimpleRNN(units=2, use_bias=True, return_sequences=True)

rnn_layer.build(input_shape=(None, None, 5))

rnn_layer.summary()

w_xh, w_oo, b_h = rnn_layer.weights

print('W_xh shape:', w_xh.shape)
print('W_oo shape:', w_oo.shape)
print('b_h shape:', b_h.shape)

x_seq = tf.convert_to_tensor([[1.0]*5, [2.0]*5, [3.0]*5], dtype=tf.float32)

## output of SimepleRNN:
output = rnn_layer(tf.reshape(x_seq, shape=(1, 3, 5)))

print(output)

# Source:
# https://github.com/rasbt/python-machine-learning-book-3rd-edition/blob/master/ch16/ch16_part1.py