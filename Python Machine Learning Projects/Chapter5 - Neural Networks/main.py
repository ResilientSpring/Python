import tensorflow as tf

print("Num of GPUs available", len(tf.config.list_physical_devices("GPU"))); # [2][3][4]

mnist = tf.keras.datasets.mnist # [1]

print(mnist);

# References
# 1. https://github.com/tensorflow/tensorflow/issues/32790#issuecomment-594816297
# 2. https://www.tensorflow.org/guide/gpu
# 3. https://www.tensorflow.org/install/gpu
# 4. https://stackoverflow.com/questions/51306862/how-do-i-use-tensorflow-gpu