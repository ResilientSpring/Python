import tensorflow as tf

tf.random.set_seed(1)

t_x = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

t_y = tf.range(4)

ds_x = tf.data.Dataset.from_tensor_slices(t_x)

ds_y = tf.data.Dataset.from_tensor_slices(t_y)

ds_joint = tf.data.Dataset.zip((ds_x, ds_y))

for example in ds_joint:
    print('x:', example[0].numpy(),
          'y:', example[1].numpy())


ds_joint2 = tf.data.Dataset.from_tensor_slices((t_x, t_y))

for example in ds_joint2:
    print('x:', example[0].numpy(),
          'y:', example[1].numpy())

