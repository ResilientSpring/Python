import tensorflow as tf

tf.random.set_seed(1)

t_x = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

t_y = tf.range(4)
