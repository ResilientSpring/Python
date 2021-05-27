import tensorflow as tf

tf.random.set_seed(1)

t = tf.random.uniform((6,))

print(t.numpy())

t_split = tf.split(t, num_or_size_splits=3)

print(t_split)

# Providing the sizes of different splits:
t2 = tf.random.uniform((5, ))

print(t2)

t2_splits = tf.split(t2, num_or_size_splits=[3, 2])

print(t2_splits)

# Concatenate tensors: 1 dimension + 1 dimension = 1 dimension
A = tf.ones((3, ))
B = tf.zeros((2, ))
C = tf.concat([A, B], axis=0)

print(C)

# Stack tensors: 1 dimension + 1 dimension = 2 dimensions
A = tf.ones((3, ))
B = tf.zeros((3, ))
Stack = tf.stack([A, B], axis=1)

print(Stack)
