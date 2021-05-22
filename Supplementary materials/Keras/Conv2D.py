import tensorflow as tf

# The inputs are 28x28 RGB images with `channels_last` and the batch size is 4.
input_shape = (4, 28, 28, 3)

y = tf.keras.layers.Conv2D(filters=2, knernel_size=3, activation='relu', input_shape=input_shape[1:])

# filters = Integer, the dimensionality of the output space
# (i.e. the number of output filters in a convolutional layer).

# Kernel_size = An integer or tuple/list of 2 integers,
# specifying the height and width of the 2D convolution window.
# Can be a single integer to specify the same value for all spatial dimensions.

print(y.shape)

# Reference: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv2D