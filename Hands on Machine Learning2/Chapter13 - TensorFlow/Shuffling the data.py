import tensorflow as tf

"""
The following code creates and displays a dataset containing the integers 0 to 9, repeated 3 times,
shuffled using a buffer of size 5 and a random seed of 42 and batched with a batch size of 7.

"""

dataset = tf.data.Dataset.range(10).repeat(3)

dataset = dataset.shuffle(buffer_size=5, seed=42).batch(batch_size=7)

for item in dataset:
    print(item)


