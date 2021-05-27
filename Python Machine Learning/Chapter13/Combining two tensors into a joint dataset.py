import tensorflow as tf

tf.random.set_seed(1)

t_x = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

t_y = tf.range(4)

ds_x = tf.data.Dataset.from_tensor_slices(t_x)
