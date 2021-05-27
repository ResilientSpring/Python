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
