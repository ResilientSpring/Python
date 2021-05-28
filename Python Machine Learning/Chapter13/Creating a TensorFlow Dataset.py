import tensorflow as tf

a = [1.2, 3.4, 7.5, 4.1, 5.0, 1.0]

ds = tf.data.Dataset.from_tensor_slices(a)

print(ds)

# Iterate through a dataset entry by entry
for item in ds:
    print(item)


# Creating batches from the dataset above, with a desired batch size of 3
ds_batch = ds.batch(batch_size=3)

for i, elem in enumerate(ds_batch, 1):
    print('batch{}:'.format(i), elem.numpy())

