import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN
import numpy as np

tf.random.set_seed(1)

rnn_layer = SimpleRNN(units=2, use_bias=True, return_sequences=True)

rnn_layer.build(input_shape=(None, None, 5))

weight_xhidden, w_oo, bias_hidden = rnn_layer.weights

print('W_xh shape:', weight_xhidden.shape)
print('W_oo shape:', w_oo.shape)
print('b_h shape:', bias_hidden.shape)
print()

X_sequence = tf.convert_to_tensor([[1.0] * 5, [2.0] * 5, [3.0] * 5], dtype=tf.float32)

# Output of simple RNN
output = rnn_layer(tf.reshape(X_sequence, shape=(1, 3, 5)))

# Manually computing the output
out_manually = []
for t in range(len(X_sequence)):
    xt = tf.reshape(X_sequence[t], (1, 5))

    print('Time step{}=>'.format(t))
    print('Input :', xt.numpy())
    ht = tf.matmul(xt, weight_xhidden) + bias_hidden
    print('Hidden:', ht.numpy())

    if t > 0:
        prev_o = out_manually[t-1]
    else:
        prev_o = tf.zeros(shape=(ht.shape))

    ot = ht + tf.matmul(prev_o, w_oo)
    ot = tf.math.tanh(x=ot)
    out_manually.append(ot)

    print('Output (manual):', ot.numpy())
    print('SimpleRNN output:'.format(t), output[0][t].numpy())
    print()
