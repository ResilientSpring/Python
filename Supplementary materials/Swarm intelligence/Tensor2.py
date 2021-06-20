import tensorflow as tf
import numpy as np

w1 = tf.get_variable("w1", shape=[5, 1], initializer=tf.truncated_normal_initializer())
w2 = tf.get_variable("w2", shape=[5, 1], initializer=tf.truncated_normal_initializer())
w3 = tf.get_variable("w3", shape=[5, 1], initializer=tf.truncated_normal_initializer())
x = tf.placeholder(tf.float32, shape=[None, 5], name="x")

a1 = tf.matmul(x, w1)
a2 = tf.matmul(x, w2*w3)
a2 = tf.stop_gradient(a2)
loss = tf.reduce_mean(tf.square(a1 - a2))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
gradients = optimizer.compute_gradients(loss)
train_op = optimizer.apply_gradients(gradients)

# Source: https://stackoverflow.com/a/39356229/14900011
