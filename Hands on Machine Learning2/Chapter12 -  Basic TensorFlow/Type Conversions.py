import tensorflow as tf

# You cannot add a float tensor and an integer tensor
addition = tf.constant(2.) + tf.constant(40)

print(addition)

# You cannot add a 32-bit float and a 64-bit float:
addition2 = tf.constant(40., dtype=tf.float64) + tf.constant(2.) # tensor's dtype defaults to tf.float32

print(addition2)

# You can use tf.cast() when you really need to convert types:
t2 = tf.constant(40.0, dtype=tf.float64)

## addition3 = tf.constant(2.0) + t2
addition3 = tf.constant(2.0) + tf.cast(t2, dtype=tf.float32)
print(addition3)
