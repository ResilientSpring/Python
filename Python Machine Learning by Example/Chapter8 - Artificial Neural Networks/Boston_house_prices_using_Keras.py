import numpy as np
import tensorflow as tf
import random as python_random

np.random.seed(42)
python_random.seed(42)
tf.random.set_seed(42)

'''adapted from Supplementary materials/Keras/Obtaining reproducible results.py'''

# Rest of code follows ...
import keras

model = keras.Sequential()



