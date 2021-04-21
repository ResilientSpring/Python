# Source: https://github.com/tensorflow/tensorflow/issues/44683#issuecomment-723641548

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))