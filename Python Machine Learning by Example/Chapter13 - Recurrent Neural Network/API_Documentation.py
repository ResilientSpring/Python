import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras import layers, models, losses, optimizers
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

# num_words:
# integer or None.
# Words are ranked by how often they occur (in the training set) and
# only the num_words most frequent words are kept.
# Any less frequent word will appear as oov_char value in the sequence data.
# If None, all words are kept. Defaults to None, so all words are kept.

# "only consider the top 10,000 most common words, but eliminate the top 20 most common words".
(X_train, y_train), (X_test, y_test) = imdb.load_data(
    path='imdb.npz', num_words=10000, skip_top=20, maxlen=None, seed=113,
    start_char=1, oov_char=2, index_from=3
)

#  If the num_words argument was specific, the maximum possible index value is num_words - 1.
#  If the maxlen argument was specified, the largest possible sequence length is maxlen.

#  As a convention, "0" does not stand for a specific word,
#  but instead is used to encode any unknown word.

# Reference: https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data
