import tensorflow as tf

X = tf.range(10)  # Any data tensor

dataset = tf.data.Dataset.from_tensor_slices(X)

print(dataset)

dataset2 = tf.data.Dataset.range(10)

print(dataset2)

dataset_pipeline = dataset.repeat(3).batch(batch_size=7)

for item in dataset_pipeline:
    print(item)


print(dataset_pipeline)

# You can also transform the items by calling the map() method.
# For example, this creates a new dataset with all items doubled:
dataset3 = dataset.map(lambda x: x * 2, num_parallel_calls=2)

print(dataset3)

for item in dataset3:
    print(item)


# While map() applies a transformation to each item,
# the apply() method applies a transformation to the dataset as a whole.
dataset4 = dataset_pipeline.unbatch() # undo batch()

print(dataset4)

for item in dataset4:
    print(item)


# Simply filter the dataset using filter()
dataset5 = dataset3.filter(lambda x: x < 10)  # keep only items < 10

# To lok at at just a few items from a dataset, use take()
for item in dataset5.take(3):
    print(item)
