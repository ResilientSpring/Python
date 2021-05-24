import tensorflow as tf
import numpy as np

np.set_printoptions(precision=3)

a = np.array([1, 2, 3], dtype=np.int32)

b = [4, 5, 6]

tensor_a = tf.convert_to_tensor(a)

b = [4, 5, 6]

tensor_b = tf.convert_to_tensor(b)

print(tensor_a)

print(tensor_b)

tensor_ones = tf.ones((2, 3))

print(tensor_ones.shape)

# To get access to the values that a tensor refers to, we can simply call the .numpy() method on a
# tensor.
print(tensor_ones.numpy())

# creating a tensor of constant values can be done as follows
const_tensor = tf.constant([1.2, 5, np.pi], dtype=tf.float32)

print(const_tensor)
