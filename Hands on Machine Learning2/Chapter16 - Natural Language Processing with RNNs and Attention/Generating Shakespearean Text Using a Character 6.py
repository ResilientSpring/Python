import tensorflow as tf
import numpy as np

shakespeare_url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
filepath = tf.keras.utils.get_file("shakespeare.txt", shakespeare_url)
with open(filepath) as f:
    shakespeare_text = f.read()


print(shakespeare_text[:148])

# Initialize Java's tokenizer
tokenizer = tf.keras.preprocessing.text.Tokenizer(char_level=True)

# Fit a tokenizer to the text - tokenizer will find all the characters in the text and map them to
# a different character ID, as char_level = True, from 1 to the number of distinct characters.
# 0 is reserved for masking.
tokenizer.fit_on_texts([shakespeare_text])

# Print to see how 'First' is represented in numbers.
print(tokenizer.texts_to_sequences(['First']))

print(tokenizer.sequences_to_texts([[20, 6, 9, 8, 3]]))

max_id = len(tokenizer.word_index) # number of distinct characters
dataset_size = tokenizer.document_count # total number of characters.

print("max_id: ", max_id)
print('dataset_size: ', dataset_size)

# Only top num_words-1 most frequent words will be taken into account. [1]
# If the num_words argument was specific, the maximum possible index value is num_words - 1.[2]
encoded = tokenizer.texts_to_sequences([shakespeare_text]) - 1

# Take the first 90% of text as training set
train_size = dataset_size * 90 // 100

# Reference:
# 1. https://www.tensorflow.org/api_docs/python/tf/keras/preprocessing/text/Tokenizer#texts_to_sequences
# 2. https://www.tensorflow.org/api_docs/python/tf/keras/datasets/imdb/load_data
