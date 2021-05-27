import tensorflow as tf

X = tf.range(10)  # Any data tensor

dataset = tf.data.Dataset.from_tensor_slices(X)

print(dataset)

dataset2 = tf.data.Dataset.range(10)

print(dataset2)

dataset_pipeline = dataset.repeat(3).batch(batch_size=3)

for item in dataset_pipeline:
    print(item)
