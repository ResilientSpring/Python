import tensorflow as tf
import numpy as np

a = np.array([2., 4., 5.])

tensor1 = tf.constant(a)

print(tensor1)

tensor2 = tensor1.numpy()

print(tensor2)