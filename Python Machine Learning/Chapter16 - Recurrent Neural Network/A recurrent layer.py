from tensorflow.keras.layers import SimpleRNN
import tensorflow as tf
from tensorflow.keras.models import Sequential

tf.random.set_seed(1)

model = Sequential([SimpleRNN(units=2, return_sequences=True, input_shape=(None, None, 5),
                              use_bias=True)])

model.summary()

# Create a sequence
X_sequence = tf.convert_to_tensor([[1.0] * 5, [2.0] * 5, [3.0] * 5], dtype=tf.float32)

X_sequence = tf.reshape(X_sequence, shape=(1, 3, 5))

# Output of a the model after it is fed with the sequence just created.
output = model(X_sequence)

print(output)
