import tensorflow as tf

tf.random.set_seed(1)

X = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

y = tf.range(4)

