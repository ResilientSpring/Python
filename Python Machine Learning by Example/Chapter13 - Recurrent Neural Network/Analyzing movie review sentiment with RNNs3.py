import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras import layers, models, losses, optimizers
from tensorflow.keras.preprocessing.sequence import pad_sequences
import matplotlib.pyplot as plt

vocabulary_size = 5000

(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocabulary_size)

# Check whether the training set is balanced, that is,
# having the same number of positive and negative samples.
print('Number of training samples: ', len(y_train))
print('Number of positive samples: ', sum(y_train))
print('Number of test samples: ', len(y_test))

# Print a training sample
print(X_train[0])

word_index = imdb.get_word_index()
index_word = {index: word for word, index in word_index.items()}
print([index_word.get(i, ' ') for i in X_train[0]])

review_length = [len(x) for x in X_train]

plt.hist(x=review_length, bins=10)
plt.show()
