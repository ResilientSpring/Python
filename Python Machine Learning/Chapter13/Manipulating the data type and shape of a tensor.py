import tensorflow as tf
import numpy as np

a = np.array([1, 2, 3, 4], dtype=np.int32)

tensor_a = tf.convert_to_tensor(a)

print(tensor_a)

tensor_a_new = tf.cast(tensor_a, tf.int64)

print(tensor_a_new.dtype)
