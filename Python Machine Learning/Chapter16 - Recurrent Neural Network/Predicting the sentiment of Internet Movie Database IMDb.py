import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import pandas as pd
from collections import Counter

dataframe = pd.read_csv('movie_data.csv', encoding = 'utf-8')
print(dataframe)

target = dataframe.pop('sentiment')
print(target)

# Create a tensorflow dataset
dataset_raw = tf.data.Dataset.from_tensor_slices((dataframe.values, target.values))

for ex in dataset_raw.take(3):
    print(ex[0].numpy()[0][0:50], ex[1])


tf.random.set_seed(1)

dataset = dataset_raw.shuffle(buffer_size=50000, reshuffle_each_iteration=False)

dataset_test = dataset.take(25000)
dataset_train_validation = dataset.skip(25000)
dataset_train = dataset_train_validation.take(20000)
dataset_validation = dataset_train_validation.skip(20000)

tokenizer = tfds.deprecated.text.Tokenizer()
token_counts = Counter()

for example in dataset_train:
    tokens = tokenizer.tokenize(example[0].numpy()[0])
    token_counts.update(tokens)

print('Vocab-size:', len(token_counts))

# Encoding unique tokens to integers
encoder = tfds.deprecated.text.TokenTextEncoder(token_counts)

example_str = 'This is an example!'

print(encoder.encode(example_str))

def encode(text_tensor, label):
    text = text_tensor.numpy()[0]
    encoded_text = encoder.encode(text)

    return encoded_text, label


def encode_map_fn(text, label):
    return tf.py_function(encode, inp=[text, label], Tout=(tf.int64, tf.int64))


processed_dataset_train = dataset_train.map(encode_map_fn)
processed_dataset_validation = dataset_validation.map(encode_map_fn)
processed_dataset_test = dataset_test.map(encode_map_fn)

# Look at the shape of some examples:
tf.random.set_seed(1)
for example in processed_dataset_train.shuffle(1000).take(5):
    print('Sequence length:', example[0].shape)

train_data = []
processed_dataset_train.padded_batch(batch_size=32, padded_shapes=([-1], []))

validation_data = []
processed_dataset_validation.padded_batch(batch_size=32, padded_shapes=([-1], []))

test_data = []
processed_dataset_test.padded_batch(batch_size=32, padded_shapes=([-1], []))

