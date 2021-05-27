import tensorflow as tf

X = tf.range(10)  # Any data tensor

dataset = tf.data.Dataset.from_tensor_slices(X)

print(dataset)

dataset2 = tf.data.Dataset.range(10)

print(dataset2)

# Iterate over a dataset's items:
for item in dataset:
    print(item)


for item in dataset2:
    print(item)


