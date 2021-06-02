import tensorflow as tf

tf.random.set_seed(1)

X = tf.random.uniform(shape=[4, 3], dtype=tf.float32)

y = tf.range(4)

joint_dataset = tf.data.Dataset.from_tensor_slices((X, y))

print(joint_dataset)

for individual_dataset in joint_dataset:
    print('X:', individual_dataset[0].numpy(), 'y:', individual_dataset[1].numpy())


# Next, we will see how to apply transformations to individual element of a dataset.
# For this, we will use the previous joint_dataset and apply feature-scaling to scale the values
# to the range [-1, 1), as currently the values of X are in the range [0, 1) based on
# a random uniform distribution.
transformed_joint_dataset = joint_dataset.map(lambda X, y: (X * 2 - 1.0, y))

for individual_dataset in transformed_joint_dataset:
    print('X:', individual_dataset[0].numpy(), 'y:', individual_dataset[1].numpy())

