import tensorflow_datasets as tfds

test_split, valid_split, train_split = tfds.Split.TRAIN.subsplit([10, 15, 75])

test_set = tfds.load("cifar10", split=test_split, as_supervised=True)
valid_set = tfds.load("cifar10", split=valid_split, as_supervised=True)
train_set = tfds.load("cifar10", split=train_split, as_supervised=True)

# Reference:
# 1. https://github.com/tensorflow/datasets/issues/291#issuecomment-474668134