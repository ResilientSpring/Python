import tensorflow as tf
import numpy as np

a = np.array([1, 2, 3, 4], dtype=np.int32)

tensor_a = tf.convert_to_tensor(a)

print(tensor_a)

# tf.case() can be used to change the data type of a tensor to a desired type.
tensor_a_new = tf.cast(tensor_a, tf.int64)

print(tensor_a_new.dtype)

# Transposing a tensor
t = tf.random.uniform(shape=(3, 5))
print(t)

t_tr = tf.transpose(t)

print(t_tr)

# Reshaping a tensor
t = tf.zeros((30, ))
t_reshape = tf.reshape(t, shape=(5, 6))

print(t_reshape)

# Removing the unnecessary dimensions (dimensions that have size 1, which are not needed.)
t = tf.zeros((1, 2, 1, 4, 1))
print(t)

t_sqz = tf.squeeze(t, axis=(2, 4))

print(t.shape, '-->', t_sqz.shape)
