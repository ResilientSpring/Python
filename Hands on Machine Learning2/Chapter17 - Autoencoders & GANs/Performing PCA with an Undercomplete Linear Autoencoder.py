import keras
import tensorflow as tf

encoder = tf.keras.Sequential([keras.Layer.Dense(2, input_shape=[3])])


