import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

np.random.seed(0)

# Sample random numbers from a normal distribution with mean 1 and standard deviation of 0.1.
x_values = np.random.normal(1, 0.1, 100).astype(np.float)

print("x_values: ", x_values)

y_values = (x_values * (np.random.normal(loc=1, scale=0.05, size=100) - 0.5)).astype(np.float)

print("y_values: ", y_values)

# In order to get assurance that the target and input have a good correlation, plot a scatter plot
# of the two variables:
plt.scatter(x=x_values, y=y_values)
plt.show()


def my_output(X, weights, biases):
    return tf.add(tf.multiply(x=X, y=weights), biases)


def loss_function(y_true, y_prediction):
    return tf.reduce_mean(tf.square(y_prediction - y_true))


my_optimization_algorithm = tf.optimizers.SGD(learning_rate=0.02)

tf.random.set_seed(1)

weights = tf.Variable(tf.random.normal(shape=[1]))
biases = tf.Variable(tf.random.normal(shape=[1]))
history = list()

for i in range(100):
    random_index = np.random.choice(100)
    rand_x = [x_values[random_index]]
    rand_y = [y_values[random_index]]

    with tf.GradientTape() as tape:
        predictions = my_output(X=rand_x, weights=weights, biases=biases)
        loss = loss_function(y_true=rand_y, y_prediction=predictions)
