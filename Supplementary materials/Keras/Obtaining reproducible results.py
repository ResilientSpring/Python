# How can I obtain reproducible results using Keras during development?

# During development of a model, sometimes it is useful to be able to obtain reproducible results
# from run to run in order to determine if a change in performance is due to an actual model or
# data modification, or merely a result of a new random seed.

# The below snippet of code provides an example of how to obtain reproducible results:

import numpy as np
import tensorflow as tf
import random as python_random

# The below is necessary for starting Numpy generated random numbers
# in a well-defined initial state.
np.random.seed(123)

# The below is necessary for starting core Python generated random numbers
# in a well-defined state.
python_random.seed(123)

# The below set_seed() will make random number generation
# in the TensorFlow backend have a well-defined initial state.
# For further details, see:
# https://www.tensorflow.org/api_docs/python/tf/random/set_seed
tf.random.set_seed(1234)

# Rest of code follows ...

## Note that you don't have to set seeds for individual initializers in your code if you do
## the steps above, because their seeds are determined by the combination of the seeds set above.


# References:
# 1. https://stackoverflow.com/a/52897216/14900011
# 2. https://keras.io/getting_started/faq/#how-can-i-obtain-reproducible-results-using-keras-during-development