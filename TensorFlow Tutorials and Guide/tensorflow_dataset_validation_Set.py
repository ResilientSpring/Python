import tensorflow_datasets as tfds

test_split, valid_split, train_split = tfds.Split.TRAIN.subsplit([10, 15, 75])

test_set = tfds.load("cifar10", split=test_split, as_supervised=True)
valid_set = tfds.load("cifar10", split=valid_split, as_supervised=True)
train_set = tfds.load("cifar10", split=train_split, as_supervised=True)

label_train = []  # [1]
for image, label in tfds.as_numpy(train_set):
    label_train.append(label)

label_test = []
for image, label in tfds.as_numpy(test_set):
    label_test.append(label)

label_validation = []
for image, label in tfds.as_numpy(valid_set):
    label_validation.append(label)


print(label_train)
print(label_test)
print(label_validation)

# Reference:
# 1. https://github.com/tensorflow/datasets/issues/291#issuecomment-474668134