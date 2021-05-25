import tensorflow as tf

tf.random.set_seed(1)

# Instantiate two random tensors, one with uniform distribution in the range [-1, 1)
t1 = tf.random.uniform(shape=(5, 2), minval=-1.0, maxval=1.0)
print(t1)

# and the other with a standard normal distribution.
t2 = tf.random.normal(shape=(5, 2), mean=0.0, stddev=1.0)
print(t2)

# To compute the element-wise product of t1 and t2, we can use the following:
t3 = tf.multiply(x=t1, y=t2)
print(t3)

# To compute the mean, sum, and standard deviation along a certain axis (or axes), we can use
t4 = tf.math.reduce_mean(t1, axis=0)
t4_1 = tf.math.reduce_sum(input_tensor=t1, axis=0)
t4_2 = tf.math.reduce_std(input_tensor=t1, axis=0)
print(t4)
print(t4_1)
print(t4_2)

# Matrix-matrix product between t1 and t2
t5 = tf.linalg.matmul(t1, t2, transpose_b=True)
t6 = tf.linalg.matmul(t1, t2, transpose_a=True)

print(t5)
print(t6)
