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
