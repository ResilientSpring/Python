import tensorflow as tfds

iris, iris_info = tfds.load("iris", with_info=True)
print(iris_info)

tfds.random.set_seed(1)

# Split the dataset into training and testing partitions ( and validation for proper machine
# learning practice) on our own.
ds_orig = iris["train"]
ds_orig = ds_orig.shuffle(150, reshuffle_each_iteration=False)
ds_train_orig = ds_orig.take(100)
ds_test = ds_orig.skip(100)

ds_train_orig = ds_train_orig.m